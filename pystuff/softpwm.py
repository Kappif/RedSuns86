
# Pulsates an LED connected to GPIO pin 1 with a suitable resistor 4 times using softPwm
# softPwm uses a fixed frequency
import wiringpi

OUTPUT = 1

PIN_TO_PWM = 23
PIN_TO_PWM2 = 24

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM,0,100) # Setup PWM using Pin, Initial Value and Range parameters
wiringpi.pinMode(PIN_TO_PWM2,OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM2,0,100)
wiringpi.softPwmWrite(PIN_TO_PWM,15)
wiringpi.softPwmWrite(PIN_TO_PWM2,15)
wiringpi.delay(20)

try:
	while True:
		for brightness in range(5,25):
			wiringpi.softPwmWrite(PIN_TO_PWM,brightness) # Change PWM duty cycle
			wiringpi.delay(20) # Delay for 0.2 seconds
		for brightness in reversed(range(5,25)):
			wiringpi.softPwmWrite(PIN_TO_PWM2,brightness)
			wiringpi.delay(20)
		for brightness in range(5,25):
                        wiringpi.softPwmWrite(PIN_TO_PWM2,brightness) # Ch$
                        wiringpi.delay(20) # Delay for 0.2 seconds
                for brightness in reversed(range(5,25)):
                        wiringpi.softPwmWrite(PIN_TO_PWM,brightness)
                        wiringpi.delay(20)




finally:
	wiringpi.softPwmWrite(PIN_TO_PWM, 15)
	wiringpi.softPwmWrite(PIN_TO_PWM2, 15)

