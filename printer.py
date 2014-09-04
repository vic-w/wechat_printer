# -*- coding:utf-8 -*-
import urllib2
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
	name ="1.png"
	print imageUrl
	time.sleep(1)
    
	if(imageUrl != last_imageUrl):
		last_imageUrl = imageUrl
        
		imageData = urllib2.urlopen(imageUrl).read()
		if(imageData == 0):
			print "read image failed"
		f = open(name,'wb')
		f.write(imageData)
		f.close()
        
		img1 = Image.open('1.png')
		width = img1.getbbox()[2]
		height = img1.getbbox()[3]
		center_x = width/2
		center_y = height/2
		if(width > height):
			width = height
		left = center_x - width / 2 + 1
		top = center_y - width / 2 + 1
		right = center_x + width / 2 - 1
		bottom = center_y + width / 2 - 1
		
		img2 = img1.crop((left, top, right, bottom))
		img2.save('2.png')
		
		img3 = Image.open('bg.png')
		img3.paste(img2.resize((560,560), Image.ANTIALIAS), (88,60,648,620))
		img3.save('3.png')
		
		img4 = img3.crop((56,6,684,906))
		img4.save('4.png')
		        
		image = pygame.image.load('4.png').convert()
		image_s = pygame.transform.scale(image, (628/2,900/2))
		screen.blit(image_s, (100,20))
		pygame.display.update()
        
		cmd = "lpr " + name
		os.system(cmd)

pygame.quit()
