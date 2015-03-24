# coding: utf-8

"""
input: pairs of words
output: Dict <pair> -> <post content>
"""

import pymongo
from collections import defaultdict

search_pairs = [(u'巴塞隆納', u'帆船'),(u'巴塞隆納',u'形狀'),(u'巴塞隆納',u'繪畫'),(u'巴塞隆納',u'格拉納達'),(u'協會',u'巴塞隆納'),(u'巴塞隆納',u'音樂廳'),(u'巴塞隆納',u'雕塑'),(u'巴塞隆納',u'建築師'),(u'巴塞隆納',u'紀念碑'),(u'巴塞隆納',u'藝人')]

db = pymongo.Connection('localhost')['espanol']
mongo_cos = ['bk.posts', 'qy.posts']

objective_post_contents = defaultdict(list)

## search content by input pair
def search_content_by_pair(objective_post_contents, w1, w2):
    pair = (w1, w2)
    if pair in objective_post_contents:
        for index, post_content in enumerate(objective_post_contents[pair]):
            print '='*20,index+1,'='*20
            print post_content
        print '='*50
        print 'total',len(objective_post_contents[pair]),'post found for pair', w1, '+', w2
    else:
        print 'No post found for pair', w1, '+', w2

for mongo_co in mongo_cos:

    co = db[mongo_co]

    for mdoc in co.find():

        ## skip this mdoc if no parsed data
        if 'parsed' not in mdoc or len(mdoc['parsed']) == 0:
            continue

        ## get post content directly from mdoc['content']
        post_contents = '\n'.join(mdoc['content'])
        
        for w1, w2 in search_pairs:
            if w1 in post_contents and w2 in post_contents:
                objective_post_contents[(w1, w2)].append( post_contents )


search_content_by_pair(objective_post_contents, w1=u"巴塞隆納", w2=u"帆船")
