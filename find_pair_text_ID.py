# coding: utf-8

''' *After calculating the 100 most frecuent words in the entire forum, we got a list of key tourism tokens (from 100 tokens find words inside the OWL).
eg., bk_100_mostcommon -> España西班牙(Nc) 7541/ tiempo時間(Na) 4034/ Madrid馬德里(Nc) 3651/ Barcelona巴塞隆納(Nc) 3376/ billete票(Na) 3110/ itinerario行程(Na) 2829/ 
Barcelona(FW) 2735/ Madrid(FW) 2429/ autobús巴士(Na) 2387/ tren火車(Na) 2377/ Granada(FW) 2277.

*With the WordUtils module, we retrieved successfully top 10 pairs with high PMI (coocurrence>7)
in which contain previous terms in the list,eg., España: 
Clasificación分類2.03147815586/ iglesia教會2.03147815586/ pastel 餅 2.03147815586/ 
derecho penal刑法2.03147815586/ revolución革命 2.03147815586/ estadio體育場 2.03147815586/ 
India印度1.9136951202/ fax傳真1.9136951202/ ocio休閒1.9136951202/ parlamento國會1.9136951202

Now, we need to trackback the original contents (posts) which contain previous pairs to do sentimental analysis
The output data need to be a txt file to insert in CopeOpi.
'''

import pymongo
import pickle
import os
import logging
import sys

class UtilsContent(object):
	'''UtilsContent for content operations such as content extraction for individual pairs 
	or contentextraction for group (top 10 pairs). 
	'''
	def _init_(self, ):
		self.
		
'''
eg.,
search_pairs = [(u'分類', u'西班牙'),(u'教會', u'西班牙'),(u'西班牙', u'餅'),(u'刑法', u'西班牙'),(u'西班牙', u'革命'),(u'西班牙', u'體育場'),(u'印度',u'西班牙'),(u'傳真',u'西班牙'),(u'休閒', u'西班牙'),(u'國會',u'西班牙')]
'''
def find_pair_text_ID (search_pairs):
	mongo_cos = ['bk.posts', 'qy.posts']
	for mongo_co in mongo_cos:
		co =db[mongo_co] 
		
		for mdoc in co.find_one():### TypeError: string indices must be integers
			parsed = mdoc['parsed']
			
			for parsed_sent in mdoc['parsed']:
				spliited = parsed_sent.strip().split(u'　')
				
				for word_pos in spliited:
					token = '('.join(word_pos.split('(')[:-1])
					objective_post_id = {k: objective_post_id[k] for k in search_pair if k in token}
					
	def write_txt():
		print('Creating new text file')
		name = raw_input('Enter name of text file: ')+'.txt'  

		try:
			file = open(name,'w')   # Trying to create a new file 
			file.close()

		except:
			print('Something went wrong!')
			sys.exit(0) # quit Python

	write_txt()
