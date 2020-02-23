import PySimpleGUI as sg
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import ebooklib
from ebooklib import epub
from book_loader import BookLoader as loader
from settings import Settings

class BookReader:	
	
	def start(self):
		mySettings = Settings()
		book = None

		sg.ChangeLookAndFeel('DarkAmber')
		layout = [	[sg.Button("Load")],
					[sg.Text("Open an EPUB", key="TITLE", size=(100, 1), font=("Helvetica", 20))],
					[sg.Button("Settings")],
					[sg.Text("Reader", size=(500,1), text_color=("white"), justification=("center"), font=("Helvetica", mySettings.TextSize), pad=(0, 380), key="WORD")],
					[sg.Button("Start", key="START/STOP")]	]


		mainWindow = sg.Window("EPUB reader", layout, size=(500,1000))

		def loadSettings(self):
			sg.ChangeLookAndFeel('DarkAmber')
			settingsLayout = [	[sg.Text("Speed (WPM)", size=(20,1)), sg.InputText(key="SPEED")],
								[sg.Text("Text size", size=(20,1)), sg.InputText(key="SIZE")],
								[sg.Button("Save"), sg.Button("Cancel")]	]

			settingsWindow = sg.Window("Settings", settingsLayout)
			settingsWindow.finalize()
			settingsWindow.FindElement("SPEED").Update(mySettings.Speed)
			settingsWindow.FindElement("SIZE").Update(mySettings.TextSize)

			while True:
				event, values = settingsWindow.read()
				if event in (None, "Cancel"):
					break
				if event in ("Save"): 
					newSpeed = values["SPEED"]
					newSize = values["SIZE"]
					mySettings.update(newSpeed, newSize)
					break

			settingsWindow.close()
			del settingsWindow

	
		def loadOpenBook(self):
			book = loader.openBook();
			if book != None:
				title = book.get_metadata("DC", "title")[0]
				print(title)
				mainWindow.FindElement("TITLE").Update(title)
			else:
				mainWindow.FindElement("TITLE").Update("No book loaded")


		while True:
			event, values = mainWindow.read()
			if event == "Load":
				loadOpenBook(self)
			if event == "Settings":
				loadSettings(self)
			if event == "START/STOP":
				if book != None:
					content = book.get_content()
					print(content)
			if event == None:
				mainWindow.close()
				exit()
			

		

			
	



