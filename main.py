'''
Created on Mar 24, 2013

@author: sushilthe
'''
import v4l2
import fcntl
import pygame.camera

pygame.camera.init()
cp = v4l2.v4l2_capability()
camlist = pygame.camera.list_cameras()
for item in camlist:
    vd = open(item, 'r')
    fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp)
    print "Camera = %s and Location = %s\n" %(cp.card, item[len(item)-1])
