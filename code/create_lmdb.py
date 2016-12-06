import sys
sys.path.append("/home/juran/caffe/python")
import os
import glob
import random
import numpy as np
import csv
import cv2
import logging
logging.basicConfig(filename='creating_lmdb.log',level=logging.DEBUG)
import caffe
from caffe.proto import caffe_pb2
import lmdb

#Size of images
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
with open('driver_imgs_list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    validation_img = []
    for row in reader:
        if row['subject'] == 'p002' or row['subject'] == 'p012':
            print row['img']
            validation_img.append(row['img'])
        

def transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT):

    #Histogram Equalization
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

    #Image Resizing
    img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)

    return img


def make_datum(img, label):
    #image is numpy.ndarray format. BGR instead of RGB
    return caffe_pb2.Datum(
        channels=3,
        width=IMAGE_WIDTH,
        height=IMAGE_HEIGHT,
        label=label,
        data=np.rollaxis(img, 2).tostring())

def check_validation(img):
    b = img.split("/")
    return b[-1] in validation_img

train_lmdb = '/home/juran/distracteddriver/input/train_lmdb'
validation_lmdb = '/home/juran/distracteddriver/input/validation_lmdb'

os.system('rm -rf  ' + train_lmdb)
os.system('rm -rf  ' + validation_lmdb)


train_data = [img for img in glob.glob("../input/train/c*/*jpg")]
test_data = [img for img in glob.glob("../input/test/*jpg")]

#Shuffle train_data
random.shuffle(train_data)

logging.debug('Creating train_lmdb')

in_db = lmdb.open(train_lmdb, map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx, img_path in enumerate(train_data):
        if check_validation(img_path):
            logging.debug('Validation:' + img_path)
            continue
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)
        if 'c0' in img_path:
            label = 0
        if 'c1' in img_path:
            label = 1
        if 'c2' in img_path:
            label = 2
        if 'c3' in img_path:
            label = 3
        if 'c4' in img_path:
            label = 4
        if 'c5' in img_path:
            label = 5
        if 'c6' in img_path:
            label = 6
        if 'c7' in img_path:
            label = 7
        if 'c8' in img_path:
            label = 8
        if 'c9' in img_path:
            label = 9
        datum = make_datum(img, label)
        in_txn.put('{:0>5d}'.format(in_idx), datum.SerializeToString())
        logging.debug('{:0>5d}'.format(in_idx) + ':' + img_path)
in_db.close()


logging.debug('\nCreating validation_lmdb')

in_db = lmdb.open(validation_lmdb, map_size=int(1e12))
with in_db.begin(write=True) as in_txn:
    for in_idx, img_path in enumerate(train_data):
        if not check_validation(img_path):
            logging.debug('Train:' + img_path)
            continue
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)
        if 'c0' in img_path:
            label = 0
        if 'c1' in img_path:
            label = 1
        if 'c2' in img_path:
            label = 2
        if 'c3' in img_path:
            label = 3
        if 'c4' in img_path:
            label = 4
        if 'c5' in img_path:
            label = 5
        if 'c6' in img_path:
            label = 6
        if 'c7' in img_path:
            label = 7
        if 'c8' in img_path:
            label = 8
        if 'c9' in img_path:
            label = 9
        datum = make_datum(img, label)
        in_txn.put('{:0>5d}'.format(in_idx), datum.SerializeToString())
        logging.debug('{:0>5d}'.format(in_idx) + ':' + img_path)
in_db.close()

logging.debug('\nFinished processing all images')
