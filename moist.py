import time
import RPi.GPIO as GPIO


def status():
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(13,GPIO.IN)
 x="dry"
 while True:
     i=GPIO.input(13)
     if i==0:
         print("wet")
         x="wet"
         time.sleep(0.1)
       
         
     elif i==1:
         print("dry")
         x="dry"
         time.sleep(0.1)

     f=open("/home/pi/Desktop/test3",'w')
     f.write(x)
     f.close()
       




if __name__ == '__main__':
    status()
