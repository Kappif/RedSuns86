# Servo Control
import time
import wiringpi

pin = 23
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

wiringpi.pwmWrite(pin,150)
try:
	while True:
	
		val = int(raw_input())
		wiringpi.pwmWrite(pin,val)
finally:
	wiringpi.pwmWrite(pin,150)

