# -*- coding: UTF-8 -*-

import cv2

import glob
import csv
import re
from object import Object
from image import Image
import const

if __name__ == "__main__":
    def getAns(path, dataset_for):
        return 1 if path.find('_{0}'.format(dataset_for)) is not -1 else 0

    paths = glob.glob("image/trimmed_*.png")

    for dataset_for in ['car', 'track']:
        cnt = 1
        data = []
        for path in paths:
            image = Image(path)
            object = Object(0, 0, image.height, image.width)

            data.append([
                cnt,
                round(object.compactness, 4),
                round(object.hwr, 4),
                getAns(path, dataset_for)
            ])

            cnt+=1

        with open('dataset/dataset_for_{0}.csv'.format(dataset_for), 'w') as f:
            w = csv.writer(f, lineterminator='\n')
            w.writerows(data)