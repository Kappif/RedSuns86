# Servo Control
import time
import wiringpi

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
PIN_TO_PWM = 18
PIN_TO_PWM2 = 23


wiringpi.wiringPiSetupGpio()
OUTPUT = 1
val = 15
wiringpi.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM,15,25)

wiringpi.pinMode(PIN_TO_PWM2, 2)     # PWM mode
wiringpi.pwmWrite(PIN_TO_PWM2, 0)


writeval = 14
#wiringpi.softPwmWrite(PIN_TO_PWM2,writeval)
wiringpi.delay(20)
#wiringpi.softPwmWrite(PIN_TO_PWM2,writeval)
wiringpi.delay(20)

# set the PWM mode to milliseconds stype
while True:
	try:
#		val = 0
			

		valn=int(raw_input())
		
		if(valn!=val):
			val=valn
			print "valn=",valn
			id = valn/100
			print "id=",id
			pwmval = valn%100		
			print "pwmval=",pwmval

		
			if(id==1):
				wiringpi.softPwmWrite(PIN_TO_PWM,pwmval)

			elif(id==2):
				wiringpi.softPwmWrite(PIN_TO_PWM2,pwmval)



			'''while(pwmval!=writeval):
				if(pwmval>writeval):
					writeval+=1
				if(pwmval<writeval):
                                        writeval-=1
		 		wiringpi.softPwmWrite(pin,writeval)
				print "writeval=",writeval'''		




	finally:
#	        wiringpi.softPwmWrite(PIN_TO_PWM,15)
#		wiringpi.softPwmWrite(PIN_TO_PWM2,14)
		print "finally ba"
