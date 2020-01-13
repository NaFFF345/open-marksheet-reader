# -*- coding:utf8 -*-
#
import cv2
import numpy as np
import get_result

import fileSearch

marker_dpi = 72
scan_dpi = 300
marker_file = fileSearch.marker_file

w = []
h = []
for i in marker_file:
    shape = list(i.shape[::-1])
    w.append(shape[-1])
    h.append(shape[-2])

for i, j in enumerate(marker_file):
    marker_file[i] = cv2.resize(
        j, (int(h[i]*scan_dpi / marker_dpi), int(w[i]*scan_dpi / marker_dpi)))

res = []


def get_resource(img):
    global marker_file
    res.clear()
    for i in marker_file:
        res.append(cv2.matchTemplate(img, i, cv2.TM_CCOEFF_NORMED))


# 処理一元開始
threshold = 0.7


def imgConvert(match, count, img):
    # testのため暫定でsheetfileをimgに代入
    global threshold,  res

    loc = np.where(match >= threshold)
    mark_area = {}

    mark_area['top_x'] = min(loc[1])
    mark_area['top_y'] = min(loc[0])
    mark_area['bottom_x'] = max(loc[1])
    mark_area['bottom_y'] = max(loc[0])
    # マーカーで囲まれた範囲
    resource = img[mark_area['top_y']:mark_area['bottom_y'],
                   mark_area['top_x']: mark_area['bottom_x']]

    if count == 0:
        n_col = 5
        n_row = 13
    else:
        n_col = 4
        n_row = 11
    # match = cv2.resize(match, (n_col*100, n_row*100))
    resource = cv2.resize(resource, (n_col*100, n_row*100))

    # ブラー処理と白黒反転
    resource = cv2.GaussianBlur(resource, (7, 7), 50)
    # cv2.imwrite('test.png', resource)

    # 大津の二値化
    match, resource = cv2.threshold(
        resource, 30, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # 白黒の反転
    resource = 255 - resource
    # 最終結果はresource

    # 切り出しと取得,表示
    if n_col == 5:
        # cv2.imwrite('test101.png', resource)
        result = get_result.getEntnumber(resource)
    else:
        result = get_result.getAnswer(resource)

    # 解答をリストに入れてリターンする
    kekka = []
    for x in range(len(result)):
        a = np.where(result[x])[0]
        if len(a) > 1:
            # 多重解答は4
            # print('Q%d:' % (x + 1) + str(a) + '複数回答')
            kekka.append(4)
        elif len(a) == 1:
            # 正解答は回答した数字-1
            # print('Q%d:' % (x + 1) + str(a))
            kekka.extend(a)
        else:
            # 未回答は5
            # print('Q%d:未回答' % (x + 1))
            kekka.append(5)
    return kekka


# テストのためリスト決め打ち 実際はforを回す
def make_data(img):
    get_resource(img)
    person_data = []
    # 画像の白黒処理をforに書き換え
    for i, j in enumerate(res):
        person_data.append(imgConvert(j, i, img))
    return person_data