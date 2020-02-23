class Settings:
	def __init__ (self):
		self.Speed = 300
		self.TextSize = 25

	def update(self, newSpeed, newTextSize):
		self.Speed = newSpeed
		self.TextSize = newTextSize
