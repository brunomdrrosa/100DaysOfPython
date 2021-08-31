# Imports
import PyPDF2
import pyttsx3

# Objeto PdfFileReader 
path = open('arquivo.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(path)
from_page = pdfReader.getPage(0)

text = from_page.extractText()

# Lendo o texto
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
