import pifacecad
import time

cad = pifacecad.PiFaceCAD()

cad.lcd.backlight_on()
cad.lcd.clear()

eye_1_index = 0
eye_1 = pifacecad.LCDBitmap([0, 0, 0, 0, 6, 6, 0, 0])

eye_2_index = 1
eye_2 = pifacecad.LCDBitmap([0, 0, 0, 0, 12, 12, 0, 0])

mouse_1_index = 2
mouse_1 = pifacecad.LCDBitmap([0, 24, 24, 7, 7, 0, 0, 0])

mouse_2_index = 3
mouse_2 = pifacecad.LCDBitmap([0, 3, 3, 28, 28, 0, 0, 0])

cad.lcd.write("       ")

cad.lcd.store_custom_bitmap(eye_1_index, eye_1)
cad.lcd.store_custom_bitmap(eye_2_index, eye_2)
cad.lcd.store_custom_bitmap(mouse_1_index, mouse_1)
cad.lcd.store_custom_bitmap(mouse_2_index, mouse_2)

cad.lcd.write_custom_bitmap(eye_1_index)
cad.lcd.write_custom_bitmap(eye_2_index)
cad.lcd.write("\n       ")
cad.lcd.write_custom_bitmap(mouse_1_index)
cad.lcd.write_custom_bitmap(mouse_2_index)

time.sleep(5)
cad.lcd.clear()
cad.lcd.backlight_off()
