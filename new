# -*- coding: utf-8 -*-

__author__ = "Saad Bin Shahid"

import sys
import cv

def print_usage(exit=False):
	print '----------------------------------------------------------------------------'
	print '- howtouse : ' + script_name + ' /path/to/image.jpg int \n- example : ' + script_name + ' lena.jpg'
	print '----------------------------------------------------------------------------'
	if exit:
		sys.exit()

"""

Parameters:	
filename – Name of file to be loaded.
flags –
Flags specifying the color type of a loaded image:

CV_LOAD_IMAGE_ANYDEPTH - If set, return 16-bit/32-bit image when the input has the corresponding depth, otherwise convert it to 8-bit.
CV_LOAD_IMAGE_COLOR - If set, always convert image to the color one
CV_LOAD_IMAGE_GRAYSCALE - If set, always convert image to the grayscale one
>0 Return a 3-channel color image.
Note In the current implementation the alpha channel, if any, is stripped from the output image. Use negative value if you need the alpha channel.
=0 Return a grayscale image.
<0 Return the loaded image as is (with alpha channel).

"""


try:
	script_name = sys.argv[0]
	image = sys.argv[1]
	flag = sys.argv[2]
	flag = int(flag)
except IndexError, e:
	print print_usage(exit=True)
except ValueError:
	# if flag == 'CV_LOAD_IMAGE_ANYDEPTH':
	# 	flag = CV_LOAD_IMAGE_ANYDEPTH
	# elif flag == 'CV_LOAD_IMAGE_COLOR':
	# 	flag = CV_LOAD_IMAGE_COLOR
	# elif flag == 'CV_LOAD_IMAGE_GRAYSCALE':
	# 	flag = CV_LOAD_IMAGE_GRAYSCALE
	pass


def converter(image, flag):

	before = cv.LoadImage(image)
	converted = cv.LoadImage(image, flag)

	cv.NamedWindow("Before",cv.CV_WINDOW_AUTOSIZE)
	cv.ShowImage("Before",before)

	cv.NamedWindow("After",cv.CV_WINDOW_AUTOSIZE)
	cv.ShowImage("After",converted)

	cv.WaitKey(0)

	cv.DestroyWindow("Before")
	cv.DestroyWindow("After")


try:
	converter(image=image, flag=flag)
except Exception, e:
	print '\nERROR : ' + str(e)
	print_usage(exit=True)

