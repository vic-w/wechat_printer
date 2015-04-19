# -*- coding:utf-8 -*-
import urllib2
import urllib
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
	print imageUrl
	time.sleep(1)
    
	if(imageUrl != last_imageUrl):
		last_imageUrl = imageUrl
        
		#imageData = urllib2.urlopen(imageUrl).read()
		#if(imageData == 0):
		#	print "read image failed"
		#f = open(name,'wb')
		#f.write(imageData)
		#f.close()
		
		urllib.urlretrieve(imageUrl, 'img_web.jpg')
        
		img_web = Image.open('img_web.jpg')
		width = img_web.getbbox()[2]
		height = img_web.getbbox()[3]
		center_x = width/2
		center_y = height/2
		if(width > height):
			width = height
		left = center_x - width / 2 + 1
		top = center_y - width / 2 + 1
		right = center_x + width / 2 - 1
		bottom = center_y + width / 2 - 1
		
		img_square = img_web.crop((left, top, right, bottom))
		img_square.save('img_square.png')
		
		img_print = Image.open('bg.png')
		img_print.paste(img_square.resize((560,560), Image.ANTIALIAS), (60,60,620,620))
		img_print.save('img_print.png')
		
		img_display = img_print.crop((0,6,684,906))
		img_display.save('img_display.png')
		        
		img_display = pygame.image.load('img_display.png').convert()
		img_display_small = pygame.transform.scale(img_display, (450,500))
		screen.blit(img_display_small, (400,50))
		pygame.display.update()
        
		cmd = "lpr img_print.png"
		os.system(cmd)

pygame.quit()
