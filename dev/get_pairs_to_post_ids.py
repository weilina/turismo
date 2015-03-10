# coding: utf-8

"""
https://github.com/weilina/turismo/blob/master/find_pair_text.py
"""

import pymongo
from collections import defaultdict

# search_pairs = [(u'海鮮', u'加泰羅尼亞'), (u'分類', u'西班牙'), (u'海鮮', u'自助餐')]
search_pairs = [(u'分類', u'西班牙'),(u'教會', u'西班牙'),(u'西班牙', u'餅'),(u'刑法', u'西班牙'),(u'西班牙', u'革命'),(u'西班牙', u'體育場'),(u'印度',u'西班牙'),(u'傳真',u'西班牙'),(u'休閒', u'西班牙'),(u'國會',u'西班牙')]

# collect unique words in search_pairs
unique_words = set(reduce(lambda x,y:list(x)+list(y), search_pairs))

def get_objective_post_ids(co, search_pairs):
    """
    Parameters
    ==========
        co: mongo collection pointer
        search_pairs: (list) target keyword pairs
    Returns
    =======
        objective_post_ids: (dict) ids of posts containing corresponding keywords in the search_pairs
    """

    objective_post_ids = defaultdict(list)

    for mdoc in co.find():
        if 'parsed' not in mdoc or len(mdoc['parsed']) == 0:
            # cannot find the key 'parsed' in the current document
            continue
        else:
            # concatenate list item to a single string
            post_contents = ''.join(mdoc['parsed'])

            # tokenize 
            # tokens: 
            # [u'\u8acb\u554f(VE)',
            #  u'Balcelona(FW)',
            #  u'\u8fd1\u52a0\u6cf0\u7f85\u5c3c\u4e9e(Nb)',
            #  u'\u5ee3\u5834(Nc)',
            #  u'\u6709(V_2)',
            # ...]           
            tokens = post_contents.replace('\n', u'　').split(u'　')

            # tokens_trim:
            # [u'\u8acb\u554f',
            #  u'Balcelona',
            #  u'\u8fd1\u52a0\u6cf0\u7f85\u5c3c\u4e9e',
            #  u'\u5ee3\u5834',
            #  u'\u6709',            
            tokens_trim = [t.split('(')[0] for t in tokens] # this is just a quick but not the best solution

            # find paris occurring in this post
            matched_pairs = find_matching(tokens_trim, search_pairs)

            # get str id
            post_id = str(mdoc['_id'])

            # append this post id in the corresponding pairs
            for matched_pair in matched_pairs:
                objective_post_ids[matched_pair].append(post_id)

    return objective_post_ids

def find_matching(tokens_trim, search_pairs, exactly_match=False):
    """
    Parameters
    ==========
        tokens_trim: (str) tokens in the parsed article
        search_pairs: (list) target keyword search_pairs 
    Returns
    =======
        matching: (dict) pair -> true/false
    """
    global unique_words

    # build up an `exist` dictionary to speed up the process of recording the word occurrence in each post
    exist = { w:0 for w in unique_words}

    # build exist dict
    if exactly_match:

        unique_tokens = set(tokens_trim)

        for token in unique_tokens:
            if token in exist:
                exist[token] = 1

    else: # partial match, the progress will become much slower
        whole_post = ''.join(tokens_trim)
        for word in unique_words:
            if word in whole_post:
                exist[word] = 1

    # build up final matching dict
    matched_pairs = []
    for pair in search_pairs:
        w1, w2 = pair
        if exist[w1] > 0 and exist[w2] > 0:
            matched_pairs.append( pair )

    return matched_pairs


if __name__ == '__main__':

    db = pymongo.Connection('localhost')['espanol']
    mongo_cos = ['bk.posts', 'qy.posts']

    results = {}

    for mongo_co in mongo_cos:
        post_ids = get_objective_post_ids(mongo_co, search_pairs)

        results[mongo_co] = post_ids
