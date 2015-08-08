import pifacecad
import time

def action(event):
	if event.pin_num == 4:
		cad.lcd.backlight_off()
	else:
		cad.lcd.backlight_on()


cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()

listener = pifacecad.SwitchEventListener()
for i in range(5):	
	listener.register(i, pifacecad.IODIR_ON, action)
listener.activate()
