# Servo Control
import time
import wiringpi


PIN_TO_PWM = 23
PIN_TO_PWM2 = 24

wiringpi.wiringPiSetupGpio()
OUTPUT = 1

wiringpi.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM,50,1000)
wiringpi.pinMode(PIN_TO_PWM2,OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM2,50,1000)

try:
	while True:
	
		val = int(raw_input())
		val2 = int(raw_input())
		val=val%100
		val2=val%100
		wiringpi.softPwmWrite(PIN_TO_PWM,val)
		wiringpi.delay(10)
	        wiringpi.softPwmWrite(PIN_TO_PWM2,val2)
		wiringpi.delay(10)


finally:
	wiringpi.softPwmWrite(PIN_TO_PWM,15)
	wiringpi.softPwmWrite(PIN_TO_PWM2,15)

