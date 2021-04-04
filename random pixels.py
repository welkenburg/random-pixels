from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from random import random
from kivy.core.window import Window

widthSquaresNumber = 100
heightSquaresNumber = 80
squareWidth = Window.width / widthSquaresNumber
squareHeight = Window.height / heightSquaresNumber

class Draw(Widget):
	def __init__(self, **kwargs):
		super(Draw, self).__init__(**kwargs)
		with self.canvas:
			for x in range(widthSquaresNumber):
				for y in range(heightSquaresNumber):
					Color(random(),random(), random())
					Rectangle(pos=(x * squareWidth, y * squareHeight), size=(squareWidth, squareHeight))
		
class EpicApp(App):
	def build(self):
		return Draw()

if __name__ == "__main__":
	EpicApp().run()
	pass

