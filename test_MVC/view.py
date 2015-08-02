import pifacecad

class View:

	def __init__(self):

		self.cad = pifacecad.PiFaceCAD()

	def write(msg):
		self.cad.lcd.write(msg)