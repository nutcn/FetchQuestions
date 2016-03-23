#!/usr/bin/python2.7

import requests
import codecs

URLString = 'http://usertk.100xuexi.com/PracticeCenter/Chapter/Index'
queryParams = {
    'TQuestionPlanID': 2554,
    'GroupUserName' : '',
    'code' : '',
    'tb_l_PaperQuePlanID' : 60900,
    'Model' : 'chapter',
    'TypeMenuFlag' : 2
}


for planID in range(60900, 60950):
	queryParams['tb_l_PaperQuePlanID'] = planID

	r = requests.get(URLString, params=queryParams)
	r.encoding = 'utf-8'

	fileName = 'Chapters/Chapter' + str(planID)
	print(fileName)

	with codecs.open(fileName, 'w', 'utf-8') as htmlfile:
		if r.status_code == requests.codes.ok:
			htmlfile.write(r.text)
