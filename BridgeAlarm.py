import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
LED = 18
BUZ = 15

print "Bridge Saver Running"

GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUZ,GPIO.OUT)

GPIO.output(TRIG,False)
print "Waiting For Sensor To Settle"
time.sleep(2)

try:
 while True:
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
   pulse_start=time.time()

  while GPIO.input(ECHO)==1:
   pulse_end=time.time()

  pulse_duration=pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  print "Distance:",distance,"cm"

  if distance < 20:
   print "Bridge too low"
   GPIO.output(BUZ,GPIO.HIGH)
   GPIO.output(LED,GPIO.HIGH)
   time.sleep(3)
   GPIO.output(BUZ,GPIO.LOW)
   GPIO.output(LED,GPIO.LOW)
  else:
   print "Bridge is fine"

  time.sleep(1)

except KeyboardInterrupt:
 print "Interrupted!"

GPIO.cleanup()
