#test of the git
from tkinter import filedialog
from tkinter import *
import re
from erlist import *

###  VARIABLES
filename =''
loaded = False

global requestString
global requestField

### Buttons Functions
#Load file and see bugs
def initial_parameters():
	textbox2.delete('1.0', 'end')
	textbox2.insert(INSERT, 'Info:\n\n')
	stringNum = 1
	logfile = open(filename, 'rt', encoding='latin1')
	for line in logfile:
		if 'TRACELEVEL : Trace_02 - complete; o_strWorkingMode' in line:
			textbox2.insert('{}.54'.format(stringNum), line[60:])
		if 'TRACELEVEL : Trace_02 - complete; o_strExtractionKitName:' in line:
			textbox2.insert('{}.54'.format(stringNum), line[60:])
		if 'TRACELEVEL : Trace_02 - complete; o_strPCRKitName:' in line:
			textbox2.insert('{}.54'.format(stringNum), line[60:])
		if 'TRACELEVEL : Trace_02 - complete; _strMethodName:' in line:
			textbox2.insert('{}.54'.format(stringNum), line[59:])
		if 'TRACELEVEL : Trace_02 - complete; _blnExtractionON:' in line:
			textbox2.insert('{}.54'.format(stringNum), line[59:])
		if 'TRACELEVEL : Trace_02 - complete; _blnPCROn:' in line:
			textbox2.insert('{}.54'.format(stringNum), line[59:])

		stringNum += 1

def show_er_codes():
	textbox3.delete('1.0', 'end')
	j = 1
	for rows in textbox.get('1.0', 'end-1c').splitlines():
		result = re.findall('\d{2,3}'+'/'+'\d{2,3}', rows)
	
		if not result:
			pass
		else:	
			textbox3.insert('{}.0'.format(j), result)
			textbox3.insert('{}.0'.format(j+1),  "\n***\n\n")
			j += 3
			
def print_er_codes():
	
	textbox.delete('1.0', 'end')
	textbox.insert('1.0', text_import())
	
def check_errors():
	
	logfile = open(filename, 'rt', encoding = 'latin1')
	error = "error"
	Error = "Error"
	no_Error = "No Error"
	no_error = "No Error"
	warning = "Warning"

	i = 1
	k = 1
	j = 1
	textbox.delete('1.0', 'end')
	
	for line in logfile:
		if "intErrorID" not in line:
			
			
			if Error in line:
				textbox.insert('{}.0'.format(i), line)
				textbox.insert('{}.0'.format(i+1), "***\n\n")
								
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
			if error in line:
				textbox.insert('{}.0'.format(i), line)
				textbox.insert('{}.0'.format(i+1), "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
			if "	error;  >" in line:
				textbox.insert('{}.0'.format(i), line)
				textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
			if "walkaway mode (no dialog)" in line:
				textbox.insert('{}.0'.format(i), line)
				textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3	
					
			if "Main - error; An error occurred while running Vector" in line:
				#parsefile.write(line+'\n\n\n')
				textbox.insert('{}.0'.format(i), line)
				textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3	
									
			if "Method has been aborted " in line:
				#parsefile.write(line+'\n\n\n')
				textbox.insert('{}.0'.format(i), line)
				textbox.insert('{}.0'.format(i+2), "***\n\n")

				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")				
				i +=3
									
			if warning in line:
				textbox.insert('{}.0'.format(i), line)
				textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
		k += 1
	logfile.close
	show_er_codes()

def check_log():
	logfile = open(filename, 'rt', encoding='latin1')
	error = "error"
	Error = "Error"
	no_Error = "No Error"
	no_error = "No Error"
	warning = "Warning"
	i = 1
	k = 1

	#textbox.delete('1.0', 'end')

	#textbox3.delete('1.0', 'end') 
	for line in logfile:
		if "intErrorID" not in line:
			
			
			if Error in line:
				#textbox.insert('{}.0'.format(i), line)
				#textbox.insert('{}.0'.format(i+1), "***\n\n")
								
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
			if error in line:
				#textbox.insert('{}.0'.format(i), line)
				#textbox.insert('{}.0'.format(i+1), "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
			if "	error;  >" in line:
				#textbox.insert('{}.0'.format(i), line)
				#textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
			if "walkaway mode (no dialog)" in line:
				#textbox.insert('{}.0'.format(i), line)
				#textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3	
					
			if "Main - error; An error occurred while running Vector" in line:
				#parsefile.write(line+'\n\n\n')
				#textbox.insert('{}.0'.format(i), line)
				#textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3	
									
			if "Method has been aborted " in line:
				#parsefile.write(line+'\n\n\n')
				#textbox.insert('{}.0'.format(i), line)
				#textbox.insert('{}.0'.format(i+2), "***\n\n")

				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")				
				i +=3
									
			if warning in line:
				#textbox.insert('{}.0'.format(i), line)
				#textbox.insert('{}.0'.format(i+1),  "***\n\n")
				
				textbox.tag_add('yellow', '{}.0'.format(k), '{}.end'.format(k))
				textbox.tag_configure('yellow',  background = "yellow")
				i += 3
				
		k += 1
	logfile.close

def LoadFile(ev):
	#global names

	global filename
	global btnValue
	btnValue = 'Load'

	
	#filename = tkinter.filedialog.Open(root, filetypes = [('*.txt files', '.txt'), ('*.trc files', '.trc')]).show()
	dialog = filedialog.Open(root, filetypes = [('*.trc files', '.trc')])
	filename = dialog.show()
	if filename == '':
		return
	if not filename:
		return	
	if btnValue == 'Load':	
		check_errors()
	initial_parameters()
	textbox.mark_set('insert', '1.0')
	textbox.focus()	
	print ("Парсинг логфайла завершен")

def LogBtn(ev):
	if filename == '':
		return

	global btnValue
	btnValue = 'Log'

	textbox.delete('1.0', 'end') 
	textbox.insert('1.0', open(filename, 'rt', encoding='latin1').read())
	
	initial_parameters()
	if btnValue == 'Log':
		check_log()
	################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
	textbox.mark_set('insert', '1.0')
	textbox.focus()	
	################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<

def BugBtn(ev):
	if filename == '':
		return
		
	global btnValue
	btnValue = 'Bug'
	textbox.delete('1.0', 'end') 
	textbox.insert('1.0', open(filename, 'rt', encoding='latin1').read())
	initial_parameters()
	if btnValue == 'Bug':
		check_errors()
		
	################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
	textbox.mark_set('insert', '1.0')
	textbox.focus()	
	################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<
	
def ErlstBtn(ev):

	initial_parameters()
	#show_er_codes()
	print_er_codes()
	################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
	textbox.mark_set('insert', '1.0')
	textbox.focus()
	################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<

################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
#функция поиска текста, его выделения тэгом, установка курсора в начало слова, перемещение скроллбара
def tsearch(requestString):
	global finderLetterCoord
	global finderRowCoord
	global pos_coords
	#try to seach text 'requestString'; if there is no such text - rise error window 
	#starts with coords finderRowCoord and LetterCoord (initially these coords are 1.0 but they are changing as user moves coursor) 
	#ends with END index, no case sensitivity
	try:
		pos = textbox.search( 
							 '{}'.format(requestString),
							 '{}.{}'.format(finderRowCoord, finderLetterCoord),
							 stopindex=END,
							 nocase = 1
		)
		pos_coords = pos.split('.')
		#text found, coords are defined, try to set up a tag but before delete tags from previous search: (tag_name, start_coord, end_coord)
		textbox.tag_delete('found_text')	
		textbox.tag_add(
						'found_text',
						'{}'.format(pos),
						'{}.{}'.format(pos_coords[0], int(pos_coords[1])+len(requestString))
		)
		#color of found text is ccff99 - lblue
		textbox.tag_configure('found_text', background = "#ccff99")
		#move coursor to the beginning of found text and focus on textbox to move scrollbar
		#scrollbar move has a shift of 5 rows, but if there is no 5 vacation rows script just passes it
		textbox.mark_set('insert', '{}'.format(pos))
		textbox.focus()
		try:
			scrollbar.config(command=textbox.yview('{}.0'.format(int(pos_coords[0])-5)))
		except:
			pass
	except:
		global error
		global error_name
		#create new window
		#with message text
		#and OK button with focus on it.
		#If Enter is pressed window is closed
		error = Tk()
		error.title('red alert')
		error.geometry('200x50')
		message = Label(error, text='text was not found')
		message.pack()
		
		okBtn = Button(error, text='Ok', command=error.destroy)
		
		error_name = error	
		okBtn.bind('<Return>', destroy_error)
		okBtn.bind('<KP_Enter>', destroy_error)
		okBtn.pack()
		okBtn.focus_set()
		error.mainloop()
		
def tsearch_reverse(requestString):
	global finderLetterCoord
	global finderRowCoord
	global pos_coords
	try:
		#the only difference between regular search is bacwards=True option for th reverse search
		#this fuu need to be combined with tsearch somehow
		pos = textbox.search(
							 '{}'.format(requestString),
							 '{}.{}'.format(finderRowCoord,finderLetterCoord),
							 stopindex='1.0',
							 backwards=True,
							 nocase = 1
		)
		pos_coords = pos.split('.')
		textbox.tag_delete('found_text')	
		textbox.tag_add(
						'found_text', 
						'{}'.format(pos), 
						'{}.{}'.format(pos_coords[0], int(pos_coords[1])+len(requestString))
		)
		textbox.tag_configure('found_text',  background = "#ccff99")
		textbox.mark_set('insert', '{}'.format(pos))
		textbox.focus()
		scrollbar.config(command=textbox.yview('{}.0'.format(int(pos_coords[0])-5)))
	except:
		global error
		global error_name
		error = Tk()
		error.title('red alert')
		error.geometry('200x50')
		message = Label(error, text='text was not found')
		message.pack()
		
		okBtn = Button(error, text='Ok', command=error.destroy)
		
		error_name = error	
		okBtn.bind('<Return>', destroy_error)
		okBtn.bind('<KP_Enter>', destroy_error)
		okBtn.pack()
		okBtn.focus_set()
		error.mainloop()

def destroy_error(event):
		global error_name
		error_name.destroy()

def findString(event):
	requestString =  requestField.get()

	tsearch(requestString)

	global finderLetterCoord
	global finderRowCoord
	global pos_coords
	finderLetterCoord = int(pos_coords[1]) + 1
	finderRowCoord = int(pos_coords[0])
	
def findString_reverse(event):
	requestString =  requestField.get()
	tsearch_reverse(requestString)
	global finderLetterCoord
	global finderRowCoord
	global pos_coords
	finderLetterCoord = int(pos_coords[1]) - 1
	finderRowCoord = int(pos_coords[0])
	
def createFinder(event):
	global finderLetterCoord
	global finderRowCoord
	global requestField
	global finder_name
	global searchWindow
	print (textbox.index(INSERT))
	searchWindow = Tk()
	searchWindow.title ('Find')
	searchWindow.geometry ('450x70')
	
	panelFinder = Frame(searchWindow)
	panelFinder.pack(fill = X)
	
	panelFinder2 = Frame(searchWindow)
	panelFinder2.pack(fill = X, side = BOTTOM)
	
	requestText=Label(panelFinder, text='Search for:')
	requestText.pack(side=LEFT)
	
	requestField = Entry(panelFinder, width=48)
	requestField.pack(side=RIGHT, pady = 10)
	
	
	firstCoord = textbox.index(INSERT).split('.')
	finderLetterCoord = int(firstCoord[0])
	finderRowCoord = int(firstCoord[1])
	

	previousBtn = Button (panelFinder2, text = 'Previous')
	nextBtn = Button (panelFinder2, text='Next')
	cancelBtn = Button (panelFinder2, text='Cancel', command = searchWindow.destroy)
	
	requestField.bind('<Return>', findString)
	requestField.bind('<KP_Enter>', findString)
	
	previousBtn.bind('<Button-1>', findString_reverse)
	nextBtn.bind('<Button-1>', findString)
	finder_name = searchWindow
	
	cancelBtn.pack(side=RIGHT)
	previousBtn.pack(side=RIGHT)
	nextBtn.pack(side=RIGHT)
	
	hintText = Label(panelFinder2, text = 'Hint: try Ctrl-F', font='TkDefaultFont 7', fg='#ebebeb')	
	hintText.pack(side = LEFT)
	
	requestField.focus()
	
	searchWindow.mainloop()
		
root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry("{}x{}".format(screenWidth-50, screenHeight-150))
panelFrame = Frame(root,width=screenWidth-60, height = 27, bg = 'lightgrey')
panelFrame.grid(row = 0, columnspan=3)

### textbox1 declaration
textbox = Text(width = 150, height = 40,  wrap=WORD)
textbox.configure(font='courier 9')
scrollbar = Scrollbar(command = textbox.yview)
textbox['yscrollcommand'] = scrollbar.set

### textbox2 declaration
textbox2 = Text(width =30, height = 20, wrap=WORD)
textbox2.configure(font='courier 9')
scrollbar2 = Scrollbar(command = textbox2.yview)
textbox2['yscrollcommand'] = scrollbar2.set

### textbox3 declaration
textbox3 = Text(width = 30, height = 20, background = 'lightgrey',wrap=WORD)
textbox3.configure(font='courier 9')
scrollbar3 = Scrollbar(command = textbox2.yview)
textbox3['yscrollcommand'] = scrollbar3.set

### grid structure
textbox.grid(row = 1, rowspan=2, column = 0)
scrollbar.grid(row = 1, rowspan=2, column = 1, sticky='ns')

textbox2.grid(row = 1, column = 2)
scrollbar2.grid(row = 1, column = 3, sticky='ns')

textbox3.grid(row = 2, column = 2)
scrollbar3.grid(row = 2, column = 3, sticky = 'ns')

### buttons
loadBtn = Button(panelFrame, text = 'Open')
logBtn = Button(panelFrame, text = 'Log')
bugBtn = Button(panelFrame, text = 'Bug')
erlstBtn = Button(panelFrame, text = 'Error codes')
################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
#unicode_string=u'\u2315'
searchBtn = Button(panelFrame, text = 'Find')#, text = unicode_string)
################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<


loadBtn.bind("<Button-1>", LoadFile)
logBtn.bind("<Button-1>", LogBtn)
bugBtn.bind("<Button-1>", BugBtn)
erlstBtn.bind("<Button-1>", ErlstBtn)
################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
searchBtn.bind('<Button-1>', createFinder)
################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<

loadBtn.place(x = 10, y = 3, width = 40, height = 25)
logBtn.place(x = 60, y = 3, width = 40, height = 25)
bugBtn.place(x = 110, y = 3, width = 40, height = 25)


################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
erlstBtn.place(x = 160, y = 3, width = 80, height = 25)
################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<



################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
searchBtn.place(x = 250, y = 3, width = 40, height = 25)

#функция проверки был ли нажат ctrl (17) а затем а-кирилицей (70). Если оба условия выполнены то выполнить функцию tsearch
ctrlCounter = False
def hullo(event):
	global ctrlCounter
	if event.keysym == 'Control_L':
		ctrlCounter = True
		#print (ctrlCounter)
	else:
		pass
	if ctrlCounter == True:	
		if event.keycode == 70:	
			print('hullo')
			tsearch()
			ctrlCounter = False
		elif event.keycode == 17:
			ctrlCounter = True
		else:
			ctrlCounter = False
	else:
		pass
	
#функция для вывода кодов и имен нажатий клавиш используется с _.bind('<Key>', prntKey)
#def prntKey(event):
#	print(event.keysym)
#	print(event.keycode)

textbox.bind('<Control-f>', createFinder)
textbox.bind('<Control-F>', createFinder)
#textbox.bind('<Key>', prntKey)
#textbox.bind('<Return>', )
################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<<

root.mainloop()
