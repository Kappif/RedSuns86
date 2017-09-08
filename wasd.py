#!/bin/env python


lr = 215
fb = 115

print lr
print fb

while 1:

	c = raw_input()

	if c == "w":
		if fb<=120: 
			fb+=1
		print fb

	if (c == "s"):
		if fb>=110:
			fb-=1
        print fb
            
	if (c == "a"):
		if lr<=220:
			lr+=1
        print lr
            
	if (c == "d"):
		if lr>=220:
			lr-=1
        print lr
            
