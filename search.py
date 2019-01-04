#test
from tkinter import filedialog
from tkinter import *
import re
import tkinter
from erlist import *
###  VARIABLES
filename =''
loaded = False

### Buttons Functions

#Quit fu
def Quit(ev):
	global root
	root.destroy()
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
def tsearch():
	#tinput = input()
	tinput = 'error'
	textbox.tag_delete('finded_text')
	

	pos = textbox.search('{}'.format(tinput), '1.0', stopindex=END)
	pos_coords = pos.split('.')
	textbox.tag_add('finded_text', '{}'.format(pos), '{}.{}'.format(pos_coords[0], int(pos_coords[1])+len(tinput)))
	textbox.tag_configure('finded_text',  background = "#ccff99")
	textbox.mark_set('insert', '{}'.format(pos))
	textbox.focus()
	scrollbar.config(command=textbox.yview('{}.0'.format(pos_coords[0])))
	
	

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
searchBtn = Button(panelFrame, text = 'Find')
################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<


loadBtn.bind("<Button-1>", LoadFile)
logBtn.bind("<Button-1>", LogBtn)
bugBtn.bind("<Button-1>", BugBtn)
erlstBtn.bind("<Button-1>", ErlstBtn)
################# ДОБАВИТЬ В РЕЛИЗ!###########################>>>>>>>>>>>
searchBtn.bind('<Button-1>', tsearch)
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
def prntKey(event):
	print(event.keysym)
	print(event.keycode)

textbox.bind('<Control-f>', tsearch)
textbox.bind('<Control-F>', tsearch)
textbox.bind('<Key>', hullo)
################# ДОБАВИТЬ В РЕЛИЗ!###########################<<<<<<<<<<<<

root.mainloop()
