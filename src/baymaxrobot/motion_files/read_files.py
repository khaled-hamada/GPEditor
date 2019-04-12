#!/usr/bin/env python

import sys 

if __name__ == '__main__':
	x = y = theta = 0.0
	file_data = open('location1.txt', 'r')
	file_out = open('result.txt','w')
	for line in file_data : 
		sp = line.split('\t')
		x =float( sp[0]) 
		y = float (sp[1]) 
		theta = float(sp[2])
	print "location is x = %f , y = %f , theta = %f " %(x,y,theta)
	print  >> file_out, "location is x = %f , y = %f , theta = %f " %(x,y,theta)
	file_out.close()
