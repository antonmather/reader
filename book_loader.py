import PySimpleGUI as sg
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askopenfile
from ebooklib import epub

class BookLoader:
	def openBook():
		sg.theme('DarkAmber')
		layout = [	[sg.Text("Locate epub to read")],
					[sg.Button("Browse...")], [sg.Button("Cancel")]	]

		window = sg.Window("Load an EPUB book", layout)

		Tk().withdraw()

		while True:
			event, values = window.read()
			if event in (None, 'Cancel'):
				break
			if event in ('Browse...'):
				file = askopenfile(mode = 'r', filetypes=[("EPUB files", "*.epub")])
				break

		window.close()
		del window

		try:	
			book = epub.read_epub(file.name)
			return book
		except:
			return None
		




