#!/bin/env python


# Servo Control
import time
import wiringpi

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
#motor = 24
servo = 23
motor = 18


# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01


wiringpi.wiringPiSetupGpio()
OUTPUT = 1
val = 15
val2 = 15

wiringpi.pinMode(servo,OUTPUT)
wiringpi.softPwmCreate(servo,15,25)




writeval = 14
wiringpi.delay(20)
wiringpi.delay(20)




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
                if lr>=210:
                        lr-=1
        print lr
            

        try:


                valn=fb

                if(valn!=val):
                        val=valn
                        print "valn=",valn
                        id = valn/100
                        print "id=",id
                        pwmval = valn%100
                        print "pwmval=",pwmval


                        if(id==1):
                                wiringpi.pwmWrite(motor,pwmval*10)

                        elif(id==2):
                                wiringpi.softPwmWrite(servo,pwmval)


				valn2=lr

                if(valn2!=val2):
                        val2=valn2
                        print "valn=",valn
                        id = valn2/100
                        print "id=",id
                        pwmval = valn2%100
                        print "pwmval=",pwmval


                        if(id==1):
                                wiringpi.pwmWrite(motor,pwmval*10)

                        elif(id==2):
                                wiringpi.softPwmWrite(servo,pwmval)



        finally:
                print "finally ba"
