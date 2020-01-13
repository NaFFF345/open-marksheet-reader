# -*- coding: utf-8 -*-
import csv

import fileSearch
import scn_settings
import cv2

with open('./master.csv') as f:
    reader = csv.reader(f)
    master_asw = [row for row in reader]
print(master_asw[0])
sheet_file = fileSearch.sheet_file

resultFile = 'result.csv'
dataFile = 'data.csv'


def scoring(file):
    i = cv2.imread(file,0)
    tokuten = 0
    tfData=[]
    markData = scn_settings.make_data(i)
    entr_number = ''.join(map(str, markData[0]))
    answer_data = markData[1] + markData[2]

    for i, j in enumerate(answer_data):
        # 取得した解答データは0baseなので+1で補正
        if i < 10:
            if master_asw[0][i] == str(j+1):
                tokuten += 3
                tfData.append('t')
            else:
                tfData.append('f')
        elif 9 < i and i < 14:
            if master_asw[0][i] == str(j+1):
                tokuten += 6
                tfData.append('t')
            else:
                tfData.append('f')
        elif 13 < i and i < 16:
            if master_asw[0][i] == str(j+1):
                tokuten += 7
                tfData.append('t')
            else:
                tfData.append('f')
        elif 15 < i and i < 20:
            if master_asw[0][i] == str(j+1):
                tokuten += 8
                tfData.append('t')
            else:
                tfData.append('f')
    data = [entr_number, tokuten]
   
    ## 結果ファイルがなければ生成 あれば追記
    print(data)
    with open(dataFile,'a') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerow(data)
        # writer.writerow(tfData)

    with open(resultFile,'a') as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerow(answer_data)


for i in sheet_file:
    scoring(i)
    print(i)