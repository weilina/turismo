
def find_tag(pairs_in_sent, tag):
	''' find_tag(s[2], "N") --- tag =  Na   -->朋友 Na	人 Na
	照片 Na'''
	return filter(lambda x:x[1].startswith(tag), pairs_in_sent)

for w in parsed_sentences:
	for n_tag in noun_list:
		nouns = find_tag(w, n_tag)
		print nouns	
	
### input:
### noun_list =["Na","Nb","Nc","Nd","Nv"]
### parsed_sentences =
[[('<', 'PARENTHESISCATEGORY'),
  ('!', 'EXCLAMATIONCATEGORY'),
  ('--', 'DASHCATEGORY'),
  ('--', 'DASHCATEGORY'),
  ('>', 'PARENTHESISCATEGORY')],
 [('\xe7\x9c\x9f', 'D'),
  ('\xe5\xb7\xa7', 'VH'),
  ('\xef\xbc\x8c', 'COMMACATEGORY'),
  ('\xe6\x89\x8d', 'Da'),
  ('\xe5\x89\x9b\xe5\x89\x9b', 'D'),
  ('\xe8\xb7\x9f', 'P'),
  ('\xe6\x9c\x8b\xe5\x8f\x8b', 'Na'),
  ('\xe6\x8e\xa8\xe8\x96\xa6', 'VC'),
  ('Silken', 'FW'),
  ('Puerta', 'FW'),
  ('Castilla', 'FW'),
  ('\xef\xbc\x8c', 'COMMACATEGORY'),
  ('\xe5\xb0\xb1', 'D'),
  ('\xe6\x9c\x89', 'V_2'),
  ('\xe4\xba\xba', 'Na'),
  ('po', 'FW'),
  ('\xe7\x85\xa7\xe7\x89\x87', 'Na'),
  ('\xe4\xba\x86', 'T'),
  ('\xef\xbc\x81', 'EXCLAMATIONCATEGORY')]]

### output:
[]
[]
[]
[]
[]
[('\xe6\x9c\x8b\xe5\x8f\x8b', 'Na'), ('\xe4\xba\xba', 'Na'), ('\xe7\x85\xa7\xe7\x89\x87', 'Na')]
[]
[]
[]
[]
[('\xe4\xbd\x8d\xe7\xbd\xae', 'Na'), ('\xe4\xba\xa4\xe9\x80\x9a', 'Na'), ('\xe6\x9c\x8b\xe5\x8f\x8b', 'Na'), ('\xe4\xba\xba', 'Na'), ('\xe8\xa1\x9b\xe7\x94\x9f', 'Na'), ('\xe6\xb0\xb4\xe5\xb9\xb3', 'Na')]
[('4\xe6\x98\x9f', 'Nb'), ('4\xe6\x98\x9f', 'Nb')]
[('\xe9\x96\x93', 'Ncd'), ('\xe9\xa6\xac\xe5\xbe\xb7\xe9\x87\x8c', 'Nc'), ('\xe9\xa3\xaf\xe5\xba\x97', 'Nc'), ('\xe6\xad\x90', 'Nc'), ('\xe6\xad\x90', 'Nc'), ('\xe6\xb0\x91\xe5\xae\xbf', 'Nc'), ('\xe6\xb5\xb4\xe5\xae\xa4', 'Nc'), ('\xe9\xa3\xaf\xe5\xba\x97', 'Nc')]
[('\xe5\x85\x83', 'Nd'), ('\xe5\x85\x83', 'Nd')]
[]
