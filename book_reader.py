import PySimpleGUI as sg
import ebooklib
from ebooklib import epub
from book_loader import BookLoader as loader
from settings import Settings
import error_message

class BookReader:	
	TITLE_NO_BOOK = "No Book Loaded"
	mySettings = None
	
	MIN_TEXT_SIZE = 10
	MAX_TEXT_SIZE = 30

	MIN_SPEED = 60
	MAX_SPEED = 1000
	
	def __init__(self):
		
		mySettings = Settings()
		book = None

		sg.ChangeLookAndFeel('DarkAmber')
		menu_def = [['File', ['Open Book']],
					['Options', ['Settings']]]
		
		layout = [	[sg.Menu(menu_def)],
					[sg.Text(self.TITLE_NO_BOOK, key="TITLE", size=(100, 1), font=("Helvetica", 20))],
					[sg.Text("Reader", size=(500,1), text_color=("white"), justification=("center"), font=("Helvetica", mySettings.TextSize), pad=(0, 380), key="WORD")],
					[sg.Button("Start", key="START/STOP")]	]


		mainWindow = sg.Window("EPUB reader", layout, size=(500,1000))

		while True:
			event = mainWindow.read()
			
			if event == "Open Book":
				self.loadOpenBook(mainWindow)
			
			if event == "Settings":
				self.loadSettings(mainWindow)

			if event == "START/STOP":
			#	if self.mainWindow.FindElement("START/STOP").button_text == "Start":
			#		self.mainWindow.FindElement("START/STOP").Update("Stop")
			#	elif self.mainWindow.FindElement("START/STOP").button_text == "Stop":
			#		self.mainWindow.FindElement("START/STOP").Update("Start")
				
				if book != None:
					content = book.get_content()
					print(content)
			
			if event == None:
				mainWindow.close()
				exit()
			
	

	def loadSettings(self, callbackWindow):
		sg.ChangeLookAndFeel('DarkAmber')
		layout = [	[sg.Text("Speed (WPM)", size=(10,1)), sg.InputText(key="SPEED", size=(20,1))],
							[sg.Text("Text size", size=(10,1)), sg.InputText(key="SIZE", size=(20,1))],
							[sg.Button("Save"), sg.Button("Cancel")]	]

		settingsWindow = sg.Window("Settings", layout)
		settingsWindow.finalize()
		settingsWindow.FindElement("SPEED").Update(self.mySettings.Speed)
		settingsWindow.FindElement("SIZE").Update(self.mySettings.TextSize)

		while True:
			event, values = settingsWindow.read()
			if event in (None, "Cancel"):
				break
			if event in ("Save"): 
				newSpeed = int(values["SPEED"])
				newSize = int(values["SIZE"])
				if self.validateSettings(newSpeed, newSize):
					self.mySettings.update(newSpeed, newSize)
					break

		settingsWindow.close()
		del settingsWindow

		callbackWindow.FindElement("WORD").Update(font=("Helvetica", self.mySettings.TextSize))


	def validateSettings(self, newSpeed, newSize):
		msg = error_message.ErrorMsg()
		if not isinstance(newSpeed, int) or (newSpeed < self.MIN_SPEED or newSpeed > self.MAX_SPEED):
			errorString = "Speed must be an integer between {} and {}".format(self.MIN_SPEED, self.MAX_SPEED)
			msg.displayError(errorString)
			return False
		if not isinstance(newSize, int) or (newSize < 10 or newSize > 30):
			errorString = "Text size must be an integer between {} and {}".format(self.MIN_TEXT_SIZE, self.MAX_TEXT_SIZE)
			msg.displayError(errorString)
			return False

		return True

	
	def loadOpenBook(self, callbackWindow):
		book = loader.openBook()
		if book != None:
			title = book.get_metadata("DC", "title")[0]
			print(title)
			callbackWindow.FindElement("TITLE").Update(title)
		else:
			callbackWindow.FindElement("TITLE").Update(self.TITLE_NO_BOOK)
		

			
	



