from tkinter import filedialog
from tkinter import *
import re
import subprocess
import encodings
import os, sys

###  VARIABLES
global requestString
global requestField
global searchAgain
global error_type

filename = ''
loaded = False
searchAgain = True
error_type = (  
				'error', 
				'Error',
				'walkaway mode (no dialog)',
				'Main - error; An error occurred',
				'Method has been aborted',
				'Warning'
				#'add here any specific text to be found as error'
)


class Errors:

	def mark_error(self, row):
		
		textbox.tag_add('yellow', '{}.0'.format(row), '{}.end'.format(row))
		textbox.tag_configure('yellow',  background = "yellow")
		
	def insert_error(self, string, row):
	
		textbox.insert('{}.0'.format(row), string)
		textbox.insert('{}.0'.format(row + 1), "***\n\n")
						
		row += 3


parameter_prefix = '2018-12-07 10:53:50> TRACELEVEL : Trace_02 - complete; '
parameter_type_eng = {
						0:'o_strWorkingMode',
						1:'o_strExtractionKitName',
						2:'o_strPCRKitName',
						3:' -------- _blnIsSimulationMode = 1',
						4:'blnLC_Plasma: 1',
						5:'blnLC_Mites: 1',
						6:'blnLC_RespSwabs: 1',
						7:'blnLC_UroSwabs: 1',
						8:'blnLC_Sputum: 1',
						9:'blnLC_WBlood: 1',
						10:'-------- _intNumberOfSamples (+EC) =',
						11:'-------- _intECNumber =',
						12:'-------- _fltSampleVolume =',
						13:'-------- _fltElutionVolume =',
						14:'-------- o_intSourceSamples = 1',
						15:'-------- o_intSourceSamples = 2',
						16:'-------- o_intSourceSamples = 3',
						17:'-------- _intStartPosExtractionPlate =',
						18:'-------- _blnElutionInTubes = 1',
						19:'-------- _blnElutionInExtractionPlate = 1',
						20:'-------- _blnElutionInPlate96 = ',
						21:'-------- _intStartPosElutionPlate =',
						22:'OfPCRControls:',
						23:'strRBType:',
						24:'o_intNumberOfECSets'
						#add here any specific variable to be found in text and put into init params textbox2
						#put russian name in nex dict
}
parameter_type_rus = {
						0:'Режим работы: ',
						1:'Метод экстракции: ',
						2:'ПЦР набор: ',
						3:'Симуляция: ',
						4:'Биоматериал: плазма\n',
						5:'Биоматериал: клещи\n',
						6:'Биоматериал: Респираторные мазки\n',
						7:'Биоматериал: Урогенитальные мазки\n',
						8:'Биоматериал: Мокрота\n',
						9:'Биоматериал: цельная кровь\n',
						10:'Число образцов с контролями: ',
						11:'Число контролей экстракции: ',
						12:'Объем образца: ',
						13:'Объем элюции: ',
						14:'Исходная пробирка: эппендорф\n',
						15:'Исходная пробирка: вакутейнер13\n',
						16:'Исходная пробирка: вакутейнер16\n',
						17:'Стартовая позиция экстракции: ',
						18:'Элюция в пробирки\n',
						19:'Элюат на магните\n',
						20:'Элюция в микроплашку',
						21:'Стартовая позиция элюции: ',
						22:'Число контролей ПЦР: ',
						23:'Реакционный блок: ',
						24:'Число реакционных блоков: '
}
		
counterlist = [] #couter array for initial_parameters function
class Parameters:
	def insert_parameter(self, string, row):
		#pass
		textbox2.insert('{}.0'.format(row),
						'{}'.format(parameter_type_rus[row] + str(string[len(parameter_prefix) + len(parameter_type_eng[row])+2:]))
		)
		row += 1

### Buttons Functions
def initial_parameters(filename):
	textbox2.delete('1.0', 'end')
	logfile = open(filename, 'rt', encoding='latin1')
	parameter_type = Parameters()

	for line in logfile:
		pass
		for num in range(len(parameter_type_eng)):
			if parameter_type_eng[num] in line:
				if num not in counterlist:
					parameter_type.insert_parameter(line, num)
					counterlist.append(num)	

def show_er_codes():

	textbox3.delete('1.0', 'end')
	row = 1
	i = 1
	for lines in textbox.get('1.0', 'end-1c').splitlines():
		result = re.findall('\d{2,3}'+'/'+'\d{2,3}', lines)
		
		if not result:
			pass
		else:
			pos = textbox3.search(result, '1.0', stopindex = END)
			
			if pos == '':
			
				textbox3.insert('{}.0'.format(row), result)
				textbox3.insert('{}.0'.format(row+1),  "\n***\n\n")
				row += 3
	

def print_er_codes():
		
	textbox.delete('1.0', 'end')
	
	txtFile = open('error_codes.txt', 'rt')#, encoding='UTF-8').read()
	txtFile.seek(3) 
	textbox.insert('1.0', txtFile.read())

def check_errors(filename):
	textbox.delete('1.0', 'end')
	
	row = 1
	k = 0
	
	strError = Errors()
	
	logfile = open(filename, 'rt', encoding = 'latin1')

	for line in logfile:
		if "intErrorID" not in line:
			if "End method - progress; Object referenced:" not in line:

				for k in range(len(error_type)):
					if error_type[k] in line:
						strError.insert_error(line.encode('utf-8'), row)
						
		row += 1
	logfile.close
	show_er_codes()
	
	textbox.mark_set('insert', '1.0')
	textbox.focus()

def check_log(filename):
	
	logfile = open(filename, 'rt', encoding='latin1')

	row = 1
	k = 0

	strError = Errors()
	for lines in logfile:
		if "intErrorID" not in lines:
			
			
			for k in range(len(error_type)-1):
				if error_type[k] in lines:
					strError.mark_error(row)
			row += 1
			
	logfile.close	

def LoadFile(ev):
	#global names

	global filename
	global btnValue
	btnValue = 'Load'

	dialog = filedialog.Open(root, filetypes = [('*.trc files', '.trc')])
	filename = dialog.show()
	print (filename)
	if filename == '':
		return
	if not filename:
		return	
	if btnValue == 'Load':	
		check_errors(filename)
	initial_parameters(filename)	
	print ("Парсинг логфайла завершен")
	root.update_idletasks()
	#root.focus_force()
	textbox.mark_set('insert', '1.0')
	textbox.focus()

def LogBtn(ev):
	if filename == '':
		return

	global btnValue
	btnValue = 'Log'
	
	textbox.delete('1.0', 'end') 
	logfile = open (filename, 'rt', encoding='latin1')
	textbox.insert('1.0', open(filename, 'rt', encoding='latin1').read())
		
	initial_parameters(filename)
	if btnValue == 'Log':
		check_log(filename)
		
	textbox.mark_set('insert', '1.0')
	textbox.focus()	

def BugBtn(ev):
	if filename == '':
		return
		
	global btnValue
	btnValue = 'Bug'
	textbox.delete('1.0', 'end') 
	textbox.insert('1.0', open(filename,'rt', encoding='latin1').read())
	initial_parameters(filename)
	if btnValue == 'Bug':
		check_errors(filename)
	textbox.mark_set('insert', '1.0')
	textbox.focus()
	
def ErlstBtn(ev):
	try:
		initial_parameters(filename)
	except Exception as ex:
		print(ex)
	print_er_codes()
		
	textbox.mark_set('insert', '1.0')
	textbox.focus()

def tsearch(requestString): #try to seach text 'requestString'; if there is no such text - rise error window 
	global finderLetterCoord #starts with coords finderRowCoord and LetterCoord (initially these coords are 1.0 but they are changing as user moves coursor) 
	global finderRowCoord
	global pos_coords
	global searchAgain
	
	try:
	#pos = textbox.search('{}'.format(requestString), '{}.{}'.format(finderRowCoord, finderLetterCoord), stopindex=END, nocase = 1)
		start = '{}.{}'.format(finderRowCoord,finderLetterCoord)
		pos = textbox.search(
							'{}'.format(requestString),
							start,
							stopindex=END,  #ends with END index, no case sensitivity
							nocase =1
		)
		pos_coords = pos.split(".")

		textbox.tag_delete('found_text')    #text found, coords are defined, try to set up a tag but before delete tags from previous search: (tag_name, start_coord, end_coord)
		textbox.tag_add(
						'found_text','{}'.format(pos),
						'{}.{}'.format(
										pos_coords[0],
										mint(pos_coords[1])+len(requestString)
						)
		)
		textbox.tag_configure('found_text', background = "#ccff99")		#color of found text is ccff99 - lblue
		textbox.mark_set('insert', '{}'.format(pos))    #move coursor to the beginning of found text and focus on textbox to move scrollbar
		textbox.focus()
		
		try:
			scrollbar.config(command=textbox.yview('{}.0'.format(int(pos_coords[0])-5)))#scrollbar move has a shift of 5 rows, but if there is no 5 vacation rows script just passes it
		except:
			pass
	except:
		global error
		global error_name
		
		#create new window
		#with message text
		#and OK button with focus on it.
		#If Enter is pressed window is closed
		searchAgain = False
		error = Tk()
		error.update_idletasks()
		error.focus_force()
		error.title('red alert')
		error.geometry('200x50')
		message = Label(error, text='text wasn\'t found')
		message.pack()
		
		okBtn = Button(error, text='Ok')
		error_name = error	
		okBtn.pack()
		okBtn.focus_set()
		okBtn.bind('<Key>', destroy_error)
		okBtn.bind('<Button-1>', destroy_error)
		
def tsearch_reverse(requestString):
	global finderLetterCoord
	global finderRowCoord
	global pos_coords
	global searchAgain

	try:

		#the only difference between regular search is bacwards=True option for th reverse search
		#this fuu need to be combined with tsearch somehow
		start = '{}.{}'.format(finderRowCoord,finderLetterCoord)
		pos = textbox.search(
							 '{}'.format(requestString),
							 start,
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
		try:
			scrollbar.config(
							command=textbox.yview(
													'{}.0'.format(int(pos_coords[0])-5)
							)
			)
		except:
			pass
	except:
		global errorCounter
		errorcounter = 1
		global error
		global error_name
		error = Tk()
		error.update_idletasks()
		error.focus_force()
		error.title('red alert')
		error.geometry('200x50')
		message = Label(error, text='text wasn\'t found')
		message.pack()
		searchAgain = False
		okBtn = Button(error, text='Ok')
		okBtn.pack()
		okBtn.focus_set()
		error_name = error	
		okBtn.bind('<Key>', destroy_error)
		okBtn.bind('<Button-1>', destroy_error)
		
def destroy_error(event):
		global error_name
		global searchAgain
		searchAgain = True
		
		error_name.destroy()
			
def findString(event):
	requestString =  requestField.get()
	global searchAgain
	if searchAgain == True:
		tsearch(requestString)
	else:
		print('wrong searchAgain: ' + str(searchAgain))
	
	global finderLetterCoord
	global finderRowCoord
	global pos_coords
	if pos_coords != ['']:
		finderRowCoord = int(pos_coords[0])
		finderLetterCoord = int(pos_coords[1]) + 1
		searchAgain = True
	else:
		finderRowCoord = 1
		finderLetterCoord = 0
			
def findString_reverse(event):
	requestString =  requestField.get()
	global searchAgain
	if searchAgain == True:
		tsearch_reverse(requestString)
	else:
		print('wrong searchAgain: ' + str(searchAgain))
	
	global finderLetterCoord
	global finderRowCoord
	global pos_coords
	if pos_coords != ['']:
		finderRowCoord = int(pos_coords[0])
		finderLetterCoord = int(pos_coords[1]) - 1
		searchAgain = True
	else:
		finderRowCoord = 1
		finderLetterCoord = 0

def createFinder(event):
	global finderLetterCoord
	global finderRowCoord
	global requestField
	global finder_name
	global searchWindow
	
	searchWindow = Tk()
	searchWindow.update_idletasks()
	searchWindow.focus_force()
	searchWindow.title ('Find')
	searchWindow.geometry ('450x70')
	
	panelFinder = Frame(searchWindow)
	panelFinder.pack(fill = X)
	
	panelFinder2 = Frame(searchWindow)
	panelFinder2.pack(fill = X, side = BOTTOM)
	
	requestText=Label(panelFinder, text='Search for:')
	requestText.pack(side=LEFT)
	
	requestField = Entry(panelFinder, width=60)
	requestField.pack(side=RIGHT, pady = 10, fill = X)
	
	firstCoord = textbox.index(INSERT).split('.')

	finderRowCoord = int(firstCoord[0])
	finderLetterCoord = int(firstCoord[1])

	previousBtn = Button (panelFinder2, text = 'Previous')
	nextBtn = Button (panelFinder2, text='Next')
	cancelBtn = Button (
						panelFinder2,
						text='Cancel',
						command = searchWindow.destroy
	)
	
	requestField.bind('<Return>', findString)
	requestField.bind('<KP_Enter>', findString)
	
	previousBtn.bind('<Button-1>', findString_reverse)
	nextBtn.bind('<Button-1>', findString)
	finder_name = searchWindow
	
	cancelBtn.pack(side=RIGHT)
	previousBtn.pack(side=RIGHT)
	nextBtn.pack(side=RIGHT)
	
	hintText = Label(
						panelFinder2,
						text = 'Hint: try Ctrl-F',
						font='TkDefaultFont 7',
						fg='#808080'
	)	
	hintText.pack(side = LEFT)
	requestField.focus()
	searchWindow.mainloop()

root = Tk()
root.title('HParser v0.5c')
root.minsize(800, 500)
root.state("zoomed")
#root.update_idletasks()
root.focus_force() 
#img = PhotoImage(file='hparser.gif') ПРОБЛЕМА изменения положения кнопок при добавлении иконки
#root.tk.call('wm', 'iconphoto', root._w, img)
#root.wm_iconbitmap('')

root.configure(background="lightgrey", bd=1)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry("{}x{}".format(screenWidth-250, screenHeight-170))
panelFrame = Frame(root, width=screenWidth, height = 32, bg = 'lightgrey')

panelFrame.pack(side=TOP, fill=X, expand = NO)

logFrame = Frame(bg = 'lightgrey')
logFrame.pack(side=LEFT, fill=BOTH, expand=YES, padx = 2, pady = 2)

textbox = Text(logFrame, width = 20)
textbox.configure(font='courier 9')
scrollbar = Scrollbar(logFrame, command = textbox.yview)
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side=LEFT, fill=BOTH, expand = YES)
scrollbar.pack(side=RIGHT, fill=Y, expand = NO)

infoFrame = LabelFrame(text='Информация о запуске', bg = 'lightgrey')
infoFrame.pack(side=TOP, expand=NO)

textbox2 = Text(infoFrame, width=32, height = 18)
textbox2.configure(font='courier 9')
scrollbar2 = Scrollbar(infoFrame, command = textbox2.yview)
textbox2['yscrollcommand'] = scrollbar2.set
textbox2.pack(side=LEFT, expand = NO)
scrollbar2.pack(side=RIGHT, fill=Y, expand = NO)

erFrame = LabelFrame (text='Коды ошибок', width = 35, bg = 'lightgrey')
erFrame.pack(side=BOTTOM, fill=Y, expand = YES)

textbox3 = Text(erFrame, width=32, background = 'lightgrey')
textbox3.configure(font='courier 9')
scrollbar3 = Scrollbar(erFrame, command = textbox3.yview)
textbox3['yscrollcommand'] = scrollbar3.set
textbox3.pack(side=LEFT, fill=BOTH, expand = YES)
scrollbar3.pack(side=RIGHT, fill=Y, expand = YES)


### buttons
loadBtn = Button(panelFrame, text = 'Open')
logBtn = Button(panelFrame, text = 'Log')
bugBtn = Button(panelFrame, text = 'Bug')
erlstBtn = Button(panelFrame, text = 'Error codes')
#unicode_string=u'\u2315'
searchBtn = Button(panelFrame, text = 'Find')#, text = unicode_string)


loadBtn.bind("<Button-1>", LoadFile)
logBtn.bind("<Button-1>", LogBtn)
bugBtn.bind("<Button-1>", BugBtn)
erlstBtn.bind("<Button-1>", ErlstBtn)

searchBtn.bind('<Button-1>', createFinder)

loadBtn.place(x = 2, y = 5, width = 42, height = 25)
logBtn.place(x = 52, y = 5, width = 42, height = 25)
bugBtn.place(x = 102, y = 5, width = 42, height = 25)
erlstBtn.place(x = 152, y = 5, width = 82, height = 25)
searchBtn.place(x = 242, y = 5, width = 42, height = 25)

#функция проверки был ли нажат ctrl (17) а затем а-кирилицей (70). Если оба условия выполнены то выполнить функцию tsearch
ctrlCounter = False
def hullo(event):
	global ctrlCounter
	if event.keysym == 'Control_L':
		ctrlCounter = True

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

#блок для открытия файлов программой  (open with)
if len(sys.argv) > 1:
	try:
		path = sys.argv[1]
		filename = path
		print (filename)
		check_errors(filename)
		initial_parameters(filename)
		
	except Exception as ex:
		print (ex)
		print ('error')


root.mainloop()
