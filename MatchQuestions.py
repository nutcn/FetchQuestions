#!/usr/bin/python2.7
# coding=utf-8

import re
import codecs

with codecs.open('Chapters/Chapter60900', 'r', 'utf-8') as readFile:
	matchForQuestions = re.compile(r'^\d+.\s' + u"[\u0000-\ufffd]+" + r'(?=<\/dt>)')
	matchForOptions = re.compile(r'\s[A-G]' + u'\uff0e')
	lines = readFile.readlines()
	optionLine = 0 #记录选项行号，下一行就是选项文字
	mergeOptionString = ''
	for i, line in enumerate(lines): 
		matchQuestions = matchForQuestions.search(line, 0)
		matchOptions = matchForOptions.search(line, 0)
		if matchQuestions:
			print('\n' + matchQuestions.group(0))
		if matchOptions:
			optionLine = i + 1
			mergeOptionString = line.strip()
		if optionLine == i:
			mergeOptionString += line.strip()
			print(mergeOptionString)




