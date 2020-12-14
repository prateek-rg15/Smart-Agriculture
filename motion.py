import time
import RPi.GPIO as GPIO

value1="OFF"
def status():
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(5,GPIO.IN)

 while True:
     i=GPIO.input(5)
     if i==0:
         print("OFF")
         time.sleep(0.1)
         value1="OFF"
         
     elif i==1:
         print("on")
         time.sleep(0.1)
         value1="ON"
         
     fileobj = open("/home/pi/Desktop/test2",'w')
     #fileobj.truncate(0)
     
     #print(str(x))
     fileobj.write(value1)
     fileobj.close()
  
   
  

def alarmstatus():
    
     return value1
     

if __name__ == '__main__':
    status()
        
