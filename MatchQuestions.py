#!/usr/bin/python2.7
# coding=utf-8

import re
import codecs

with codecs.open('Exam.md', 'w', 'utf-8') as writeFile:
	for chapter in range(62641, 62645):
		fileName = 'MockExam/Exam' + str(chapter)
		with codecs.open(fileName, 'r', 'utf-8') as readFile:
			matchForChapterTitle = re.compile(r'\"' + u'\u7b2c' + r'\d' + u"[\u0000-\ufffd]+" + r'(?=\/>)')
			matchForQuestions = re.compile(r'^\d+.\s' + u"[\u0000-\ufffd]+" + r'(?=<\/dt>)') # 匹配题目问题
			matchForOptions = re.compile(r'\s[A-G]' + u'\uff0e') #匹配 A B C D 选项

			lines = readFile.readlines()
			optionLine = -20 #记录选项行号，下一行就是选项文字
			mergeOptionString = ''
			for i, line in enumerate(lines): 
				# 标题
				titleMatch = matchForChapterTitle.search(line, 0)
				if titleMatch:
					title = titleMatch.group(0)
					# 去除两边引号
					Ltitle = re.split(r'\"', title)
					LtitleR = re.split(r'\"', Ltitle[1])
					chapterTitle = '<br>\n### ' + LtitleR[0] + '\n\n'
					writeFile.write(chapterTitle)
				#问题
				matchQuestions = matchForQuestions.search(line, 0)
				if matchQuestions:
					questionWithNumberSpace = re.split(r'\.', matchQuestions.group(0))
					question = '<br>\n\n\n**' + questionWithNumberSpace[0] +' .' + questionWithNumberSpace[1] + '**<br>'
					writeFile.write(question)
				#答案选项
				matchOptions = matchForOptions.search(line, 0)
				if matchOptions:
					optionLine = i + 1
					mergeOptionString = line.strip()
				if optionLine == i:
					mergeOptionString += line.lstrip()
					writeFile.write(mergeOptionString)




