import cv2
import numpy as np


def getEntnumber(im):
    result = []

    for col in range(5):
        tmp_img = im[:, col * 100 + 25:(col + 1) * 100 - 25]
        area_sum = []
        # cv2.imwrite('%d' % col + '.png', tmp_img)
        for row in range(10):
            area_sum.append(
                np.sum(tmp_img[(row + 3) * 100 + 25:(row + 4) * 100 - 25, ]))
        # result.append(area_sum > np.median(area_sum) * 80)
        # 偏差値60以上を追加
        ans = np.round_(50+10*(area_sum-np.average(area_sum))/np.std(area_sum))
        result.append(ans > 60)
        # print(ans)
        # print(area_sum)
    return result


def getAnswer(im):
    result = []
    for row in range(10):
        tmp_img = im[(row+1) * 100 + 25:(row + 2) * 100 - 25, ]
        area_sum = []
        # cv2.imwrite('%d' % row + '_asw1.png', tmp_img)

        for col in range(3):
            area_sum.append(
                np.sum(tmp_img[:, (col + 1) * 100 + 25:(col + 2) * 100 - 25]))
        # result.append(area_sum > np.median(area_sum)*15)
        ans = np.round_(50+3*(area_sum-np.average(area_sum))/np.std(area_sum))
        result.append(ans > 50)
        # print(ans)
        # print(area_sum)
    return result
