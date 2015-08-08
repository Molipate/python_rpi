import pifacecad

class View:

	def __init__(self):
		self.cad = pifacecad.PiFaceCAD()
		self.cad.lcd.backlight_on()
		self.cad.lcd.clear()

	def write(self, msg):
		self.cad.lcd.write(msg);

view = View()
view.write("salut")
