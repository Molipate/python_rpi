import pifacecad

class View:

	def __init__(self):
		self.cad = pifacecadPiFaceCAD()
		self.cad.lcd.backlight_on()
		self.cad.lcd.clear()

	def write(msg):
		self.cad.lcd.write(msg);

view = View()
view.write("salut")