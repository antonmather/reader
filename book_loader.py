import PySimpleGUI as sg
from tkinter.filedialog import askopenfilename, askopenfile
from ebooklib import epub

class BookLoader:
	
	def openBook():
		bookFile = sg.popup_get_file('Open which file?', file_types=[("EPUB files", "*.epub")])

		try:
			print(bookFile)	
			book = epub.read_epub(bookFile)
			return book
		except:
			return None
		




