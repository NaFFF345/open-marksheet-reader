# -*- coding: utf8 -*-

import cv2
import glob

sheet_file =[i for i in glob.glob('./scn-asw*.jpg')]

marker_file = []
# marker_file.sort()
for i in glob.glob('./marker*.jpg'):
    marker_file.append(cv2.imread(i, 0))
