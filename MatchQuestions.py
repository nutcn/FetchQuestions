import re
import codecs

# ^\d.\s

with codecs.open('./test', 'r') as readFile:
	print(readFile.read().encode('utf-8'))