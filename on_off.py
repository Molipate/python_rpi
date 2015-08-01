import pifacecad
from time import sleep
time = 0.4
cad = pifacecad.PiFaceCAD()
while (True):
	cad.lcd.backlight_off()
	sleep(time)
	cad.lcd.backlight_on()
	sleep(time)
