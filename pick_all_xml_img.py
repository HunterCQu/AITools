# -*- coding: utf-8 -*-
# Author : Andy Liu
# Last modified: 2018-8-10

# This tool is used to pick xml and image from the some folder
# This file should put on the same path with the folder
# input: python pick_all_xml_img.py "/home/andy/data/img"
# output:
# 	./pickedLabel
# 	./pickedImg

import os
import shutil
import sys
import argparse


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('srcdir', help='file directory', type=str)

	args = parser.parse_args()
	return args



def pick(srcdir):
	pickedLabel_dir = "./pickedLabel"
	pickedImg_dir = "./pickedImg"

	# remake folder
	if os.path.exists(pickedLabel_dir):
		shutil.rmtree(pickedLabel_dir)
	os.makedirs(pickedLabel_dir) 

	if os.path.exists(pickedImg_dir):
		shutil.rmtree(pickedImg_dir)
	os.makedirs(pickedImg_dir)

	filelist = os.listdir(srcdir)

	for file in filelist:
		print(file)
		fileInfor = file.split(".")
		if fileInfor[-1] != "xml":
			continue
		if not os.path.exists(srcdir+"/"+fileInfor[0]+".jpg"):
			continue

		dst_label = pickedLabel_dir + "/" + fileInfor[0] + ".xml"
		dst_img = pickedImg_dir + "/" + fileInfor[0] + ".jpg"
		shutil.copyfile(srcdir + "/" + fileInfor[0] + ".xml", dst_label)
		shutil.copyfile(srcdir + "/" + fileInfor[0] + ".jpg", dst_img)

if __name__ == '__main__':
	args = parse_args()
	srcdir = args.srcdir
  
	if not os.path.exists(srcdir):
		print("Error !!! %s is not exists, please check the parameter"%srcdir)
		sys.exit(0)

	pick(srcdir)
	print("Done!")
