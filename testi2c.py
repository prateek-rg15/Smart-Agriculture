# connect LED to GPIO22  and  GPIO18(pin 15)
import time
import RPi.GPIO as GPIO
import smbus


bus = smbus.SMBus(1)
address=0x20



def startProcess(mrg):
  GPIO.setmode(GPIO.BCM)
  if mrg=='1':
    for x in range(0,5):
      GPIO.setup(27, GPIO.OUT)
      GPIO.output(27, True)
      time.sleep(0.05)
      GPIO.output(27, False)
      time.sleep(0.45)

  elif mrg=='2':
     GPIO.setup(27, GPIO.OUT)
     GPIO.output(27, True)

  elif mrg=='3':
     #Setting output, IODRA. IODRB
     bus.write_byte_data(address, 0x00, 0)
     bus.write_byte_data(address, 0x01, 0)
     #Setting 1/0 0x12 for A output and 0x13 for B, GPIOA, GPIOB   
     bus.write_byte_data(address, 0x13, 0x80)
     bus.write_byte_data(address, 0x12, 0xC0)
     print ((bus.read_byte_data(address, 0x12)))
     time.sleep(3)
     GPIO.cleanup()
     bus.write_byte_data(address, 0x12, 0x40)
     bus.write_byte_data(address, 0x13, 0x00)
     time.sleep(3)
     bus.write_byte_data(address, 0x12, 0x80)
     bus.write_byte_data(address, 0x13, 0x80)
     time.sleep(3)
     bus.write_byte_data(address, 0x12, 0x00)
     bus.write_byte_data(address, 0x13, 0x00)

  elif mrg=='4':
     #Setting output, IODRA. IODRB this is for setting input or output
     #value of IODR will be in hexadecimal IODRB B7 has been set as input 0x80 
     bus.write_byte_data(address, 0x00, 0)
     #bus.write_byte_data(address, 0x01, 0x80)
     bus.write_byte_data(address, 0x01, 0x00)

     #Setting 1/0 0x12 for A output and 0x13 for B, GPIOA, GPIOB
     #GPIOB ports B1-B4 are used for CONTROL
     #Things worked in stepper motor drive without common GRD
     #However ENA and ENB are having lnks could be reason for working
     # Forward movement 
     for x in range(0,50):
       bus.write_byte_data(address, 0x13,0xD0)
       time.sleep(.05)
       bus.write_byte_data(address, 0x13, 0xB0)
       time.sleep(0.05)
       bus.write_byte_data(address, 0x13, 0xA8)
       time.sleep(0.05)
       bus.write_byte_data(address, 0x13, 0xC8)
       time.sleep(0.05)
     # Reverse movement 
     for x in range(0,50):
       bus.write_byte_data(address, 0x13, 0xC8)
       time.sleep(.06)
       bus.write_byte_data(address, 0x13, 0xA8)
       time.sleep(0.06)
       bus.write_byte_data(address, 0x13, 0xB0)
       time.sleep(0.06)
       bus.write_byte_data(address, 0x13, 0xD0)
       time.sleep(0.06)
     GPIO.cleanup()  
     bus.write_byte_data(address, 0x13, 0x00)

  elif mrg=='5':
     #Setting output, IODRA. IODRB
     bus.write_byte_data(address, 0x00, 0)
     bus.write_byte_data(address, 0x01, 0)
     #Setting 1/0 0x12 for A output and 0x13 for B, GPIOA, GPIOB   
     bus.write_byte_data(address, 0x13, 0x80)
     bus.write_byte_data(address, 0x12, 0xC0)
     print ((bus.read_byte_data(address, 0x12)))
     time.sleep(3)
     GPIO.cleanup()
     bus.write_byte_data(address, 0x12, 0x40)
     bus.write_byte_data(address, 0x13, 0x00)
     time.sleep(3)
     bus.write_byte_data(address, 0x12, 0x80)
     bus.write_byte_data(address, 0x13, 0x80)
     time.sleep(3)
     bus.write_byte_data(address, 0x12, 0x00)
     bus.write_byte_data(address, 0x13, 0x00)
  elif mrg=='6':
     print("server motor")
     #Setting output, IODRA. IODRB this is for setting input or output
     #value of IODR will be in hexadecimal IODRB B7 has been set as input 0x80 
     bus.write_byte_data(address, 0x00, 0)
     #bus.write_byte_data(address, 0x01, 0x80)
     bus.write_byte_data(address, 0x01, 0x00)

     #Setting 1/0 0x12 for A output and 0x13 for B, GPIOA, GPIOB
     #GPIOB ports B1-B4 are used for CONTROL
     #Things worked in stepper motor drive without common GRD
     #However ENA and ENB are having lnks could be reason for working
     # Forward movement 
     for x in range(0,50):
       bus.write_byte_data(address, 0x13,0xD0)
       time.sleep(.1)
       bus.write_byte_data(address, 0x13, 0xC8)
       time.sleep(0.1)
       bus.write_byte_data(address, 0x13, 0xA8)
       time.sleep(0.1)
       bus.write_byte_data(address, 0x13, 0xB0)
       time.sleep(0.1)
     GPIO.cleanup()
     bus.write_byte_data(address, 0x13, 0x00)
  elif mrg=='7':
     #Setting output, IODRA. IODRB
     bus.write_byte_data(address, 0x00, 0)
     bus.write_byte_data(address, 0x01, 0X00)
     #Setting 1/0 0x12 for A output and 0x13 for B, GPIOA, GPIOB   
     
     bus.write_byte_data(address, 0x12, 0xC0)
     print ((bus.read_byte_data(address, 0x12)))
        
     bus.write_byte_data(address, 0x12, 0x20)
     print ("LED")
     time.sleep(3)
     GPIO.cleanup()
     bus.write_byte_data(address, 0x12, 0x00)     


if __name__ == '__main__':
    startProcess('6')

