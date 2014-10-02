## make sure string is unicode
## if string is utf8: string.decode('utf8')


import re
z_t = re.findall(ur'[\u4e00-\u9fa5]+', z)
