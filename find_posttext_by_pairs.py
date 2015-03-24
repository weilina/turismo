search_pairs = [(u'巴塞隆納', u'帆船'),(u'巴塞隆納',u'形狀'),(u'巴塞隆納',u'繪畫'),(u'巴塞隆納',u'格拉納達'),(u'協會',u'巴塞隆納'),(u'巴塞隆納',u'音樂廳'),(u'巴塞隆納',u'雕塑'),(u'巴塞隆納',u'建築師'),(u'巴塞隆納',u'紀念碑'),(u'巴塞隆納',u'藝人')]
db = pymongo.Connection('localhost')['espanol']
mongo_cos = ['bk.posts', 'qy.posts']

for mongo_co in mongo_cos:
	co = db[mongo_co]

	objective_post_contents = defaultdict(list)

	for mdoc in co.find():
		if 'parsed' not in mdoc or len(mdoc['parsed']) == 0:
			continue
		else:
			post_contents = ''.join(mdoc['parsed'])
			     
			for pair in search_pairs:
				w1, w2 = pair
				if w1 in post_contents and w2 in post_contents:
					objective_post_contents[pair].append(post_contents)


