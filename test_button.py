import pifacecad
import time

def action(event):
	listener.deactivate()
	cad.backlight_off()
	time.sleep(1)


cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()

listener = pifacecad.SwitchEventListener()
listener.register(0, pifacecad.IODIR_ON, action)
listener.activate()
