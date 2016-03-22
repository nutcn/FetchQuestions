#!/usr/bin/python2.7
# coding=utf-8

import re
import codecs

# ^\d.\s

with codecs.open('Chapters/Chapter60900', 'r', 'utf-8') as readFile:
	matchForQuestions = re.compile(r'^\d.\s' + u"[\u0000-\ufffd]+" + r'(?=<\/dt>)')
	matchForOptions = re.compile(r'\s[A-G]' + u'\uff0e')
	for line in readFile.readlines(): 
		matchQuestions = matchForQuestions.search(line, 0)
		matchOptions = matchForOptions.search(line, 0)
		if matchQuestions:
			print(matchQuestions.group(0))
		if matchOptions:
			print(matchOptions.group(0))