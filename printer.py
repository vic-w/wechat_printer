# -*- coding:utf-8 -*-
import urllib2
import urllib
import pyexiv2
import pygame
import os
from pygame.locals import *
from sys import exit
import time
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((0,0),0,32)

last_imageUrl = ""

while True:
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			break

	url = "http://1.virtualshop.sinaapp.com/photo.php"
	imageUrl = urllib2.urlopen(url).read()
	time.sleep(1)
    
	if(imageUrl != last_imageUrl):
		last_imageUrl = imageUrl
	
		print imageUrl

		#imageData = urllib2.urlopen(imageUrl).read()
		#if(imageData == 0):
		#       print "read image failed"
		#f = open(name,'wb')
		#f.write(imageData)
		#f.close()
		
		urllib.urlretrieve(imageUrl, 'img_web.jpg')
		print 'image downloaded'

		img_web = Image.open('img_web.jpg')
		
		# check the orientation of the image

		meta = pyexiv2.metadata.ImageMetadata('img_web.jpg')
		meta.read()
		print 'metadata = ', meta.exif_keys
		

		if 'Exif.Image.Orientation' in meta.exif_keys:
			tag = meta['Exif.Image.Orientation']
			orientation = tag.value 
			if orientation == 1:
				# Nothing
				img_web_mirror = img_web.copy()
			elif orientation == 2:
				# Vertical Mirror
				img_web_mirror = img_web.transpose(Image.FLIP_LEFT_RIGHT)
			elif orientation == 3:
				# Rotation 180°
				img_web_mirror = img_web.transpose(Image.ROTATE_180)
			elif orientation == 4:
				# Horizontal Mirror
				img_web_mirror = img_web.transpose(Image.FLIP_TOP_BOTTOM)
			elif orientation == 5:
				# Horizontal Mirror + Rotation 90° CCW
				img_web_mirror = img_web.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_90)
			elif orientation == 6:
				# Rotation 270°
				img_web_mirror = img_web.transpose(Image.ROTATE_270)
			elif orientation == 7:
				# Horizontal Mirror + Rotation 270°
				img_web_mirror = img_web.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_270)
			elif orientation == 8:
				# Rotation 90°
				img_web_mirror = img_web.transpose(Image.ROTATE_90)
		else:
			
			img_web_mirror = img_web.copy()

		print 'Orientation fixed'

		width = img_web_mirror.getbbox()[2]
		height = img_web_mirror.getbbox()[3]
		center_x = width/2
		center_y = height/2
		if(width > height):
			width = height
		left = center_x - width / 2 + 1
		top = center_y - width / 2 + 1
		right = center_x + width / 2 - 1
		bottom = center_y + width / 2 - 1
		
		img_square = img_web_mirror.crop((left, top, right, bottom))
		#img_square.save('img_square.png')
		
		print 'Image cropped'

		img_print = Image.open('bg.png')
		img_print.paste(img_square.resize((560,560), Image.ANTIALIAS), (60,60,620,620))
		img_print.save('img_print.png')
		
		print 'Image pasted'

		img_display = img_print.crop((0,6,684,906))
		img_display.save('img_display.png')
			
		print 'Image going to be displayed'

		img_display = pygame.image.load('img_display.png').convert()
		img_display_small = pygame.transform.scale(img_display, (230,360))
		screen.blit(img_display_small, (200,20))
		pygame.display.update()
	
		print 'Image displayed'

		cmd = "lpr img_print.png"
		os.system(cmd)

		print 'Sent to print'
pygame.quit()
