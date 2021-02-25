import os
import sys
import re
import subprocess
import encodings
import webbrowser
import tkinter as tk
from tkinter import filedialog
import settingslib

finder2 = 'sleep'
filename = ''
searchAgain = True
error_type = (  
				'error', 
				'Error',
				'walkaway mode (no dialog)',
				'Main - error; An error occurred',
				'Method has been aborted',
				'Warning',
				'MethodAborted - start;',
				'MethodAborted - complete;',
				'er99',
				#'add here any specific text to be found as error'
)		
def finder_check():
	global finder2
	finder2 = 'sleep'

class Errors:


	def mark_error(self, row):
		textbox.tag_add('yellow', '{}.0'.format(row), '{}.end'.format(row))
		textbox.tag_configure('yellow',  background = "yellow")
		
	def insert_error(self, string, row):
		textbox.insert('{}.0'.format(row), string)
		textbox.insert('{}.0'.format(row + 1), "-------------------------\n\n")			
		row += 3

parameter_prefix = '2018-12-07 10:53:50> TRACELEVEL : Trace_02 - complete; '
# parameter_type_eng = {
# 						0:' -------- _blnIsSimulationMode = 1',
# 						1:'o_strWorkingMode',
# 						2:'o_strExtractionKitName',
# 						3:'blnLC_Plasma: 1',
# 						4:'blnLC_Mites: 1',
# 						5:'blnLC_RespSwabs: 1',
# 						6:'blnLC_UroSwabs: 1',
# 						7:'blnLC_Sputum: 1',
# 						8:'blnLC_WBlood: 1',
# 						9:'-------- o_intSourceSamples = 1',
# 						10:'-------- o_intSourceSamples = 2',
# 						11:'-------- o_intSourceSamples = 3',	
# 						12:'-------- _intNumberOfSamples (+EC) =',
# 						13:'-------- _intECNumber =',
# 						14:'-------- _fltSampleVolume =',
# 						15:'-------- _fltElutionVolume =',
# 						16:'-------- _intStartPosExtractionPlate =',
# 						17:'-------- _blnElutionInTubes = 1',
# 						18:'-------- _blnElutionInExtractionPlate = 1',
# 						19:'-------- _blnElutionInPlate96 = ',
# 						20:'-------- _intStartPosElutionPlate =',
# 						21:'o_strPCRKitName',
# 						22:'OfPCRControls:',
# 						23:'strRBType:',
# 						24:'o_intNumberOfECSets'
# 						#add here any specific variable to be found in text and put into init params textbox2
# 						#put russian name in nex dict				
# }
# #print (parameter_type_eng.keys())
# parameter_type_rus = {
# 						0:'Симуляция!\n',
# 						1:'Режим работы: ',
# 						2:'Метод экстракции: ',				
# 						3:'Биоматериал: плазма\n',
# 						4:'Биоматериал: клещи\n',
# 						5:'Биоматериал: Респираторные мазки\n',
# 						6:'Биоматериал: Урогенитальные мазки\n',
# 						7:'Биоматериал: Мокрота\n',
# 						8:'Биоматериал: цельная кровь\n',
# 						9:'Исходная пробирка: эппендорф\n',
# 						10:'Исходная пробирка: вакутейнер13\n',
# 						11:'Исходная пробирка: вакутейнер16\n',	
# 						12:'Число образцов с контролями: ',
# 						13:'Число контролей экстракции: ',					
# 						14:'Объем образца: ',
# 						15:'Объем элюции: ',
# 						16:'Стартовая позиция экстракции: ',
# 						17:'Элюция в пробирки\n',
# 						18:'Элюат на магните\n',
# 						19:'Элюция в микроплашку',
# 						20:'Стартовая позиция элюции: ',
# 						21:'ПЦР набор: ',
# 						22:'Число контролей ПЦР: ',
# 						23:'Реакционный блок: ',
# 						24:'Число реакционных блоков: '
# }
		
counterlist = [] #couter array for initial_parameters function
class Parameters:
	
	def insert_parameter(self, string, row):
		with open('data/settings.txt', "rt") as settingsFile:
			mySettings = settingsFile.read().splitlines()

		with open('data/parameters_ru.txt', "rt") as parametersFile:
			myParameters = parametersFile.read().splitlines()
		settingsFile.close()
		parametersFile.close()
		if '\\n' in myParameters[row]:
			textbox2.insert('{}.0'.format(row),
							'{}'.format(myParameters[row][:-2]+'\n')
			)
		else:
			textbox2.insert('{}.0'.format(row),
							'{}'.format(myParameters[row] + str(string[len(parameter_prefix) + len(mySettings[row])+2:]))
			)
		row += 1
		

### Buttons Functions
# def initial_parameters(filename):
	
# 	logfile = open(filename, 'rt', encoding='latin1')
# 	parameter_type = Parameters()
	
# 	for line in logfile:
		
# 		for num in range(len(parameter_type_eng)):
# 			if parameter_type_eng[num] in line:
# 				if num not in counterlist:
					
# 					parameter_type.insert_parameter(line, num)
# 					counterlist.append(num)	
# 	logfile.close()

def initial_parameters(filename):
	
	with open('data/settings.txt', 'rt') as settingsFile:
		mySettings = settingsFile.read().splitlines()
	settingsFile.close()
	logfile = open(filename, 'rt', encoding='latin1')
	parameter_type = Parameters()
	for line in logfile:
		for num in range(len(mySettings)):
			if mySettings[num] in line:
				if num not in counterlist:
					parameter_type.insert_parameter(line, num)
					counterlist.append(num)	
	logfile.close()


def show_er_codes():

	textbox3.delete('1.0', 'end')
	row = 1
	i = 1
	for lines in textbox.get('1.0', 'end-1c').splitlines():
		result = re.findall('\d{2,3}'+'/'+'\d{2,3}', lines)
		
		if not result:
			pass
		else:
			pos = textbox3.search(result, '1.0', stopindex = tk.END)
			if pos == '':
				textbox3.insert('{}.0'.format(row), result)
				textbox3.insert('{}.0'.format(row+1),  "\n***\n\n")
				row += 3
	

#def print_er_codes():
#	textbox.config(state='normal')
#	textbox.delete('1.0', 'end')
#	
#	txtFile = open('error_codes.txt', 'rt')#, encoding='UTF-8').read()
#	txtFile.seek(3)  #перемещает курсор на 3й символ
#	textbox.insert('1.0','<html><body>123</body></html>')
#	textbox.insert('2.0', txtFile.read())
#	textbox.config(state='disabled')
	
def check_errors(filename):
	textbox.config(state='normal')
	textbox.delete('1.0', 'end')

	
	row = 1
	k = 0
	
	strError = Errors()
	
	logfile = open(filename, 'rt', encoding = 'latin1')
	
	for line in logfile:
		if "intErrorID" not in line:
			if "End method - progress; Object referenced:" not in line:
				if "retVal_CopyFile (0 - no error, 1 - error occured) = 0" not in line:
					if "Warning: Shaking on ML_Star node ( 1 ) not started, check of speed limit will be disabled!" not in line:
						if "Warning: Heating up on ML_Star node ( 1 ) not started, check of temperature limit will be disabled!" not in line:
							for k in range(len(error_type)):
								if error_type[k] in line:
						
									strError.insert_error(line, row)#(line.encode('utf-8'), row) давало баг непонятных символов в Microlab (R)
						
		row += 1
	logfile.close
	show_er_codes()
	
	textbox.mark_set('insert', '1.0')
	textbox.focus()
	#Отключение изменений в тексте
	textbox.config(state='disabled')

def check_log(filename):
	logfile = open(filename, 'rt', encoding='latin1')
	row = 0
	k = 0
	strError = Errors()
	for lines in logfile:
		row += 1
		if "intErrorID" not in lines:
			if "retVal_CopyFile (0 - no error, 1 - error occured) = 0" not in lines:
				for k in range(len(error_type)):
					if error_type[k] in lines:
						strError.mark_error(row)
			#row += 1
	logfile.close	

def LoadFile(event): #ev
	global counterlist
	global filename
	
	dialog = filedialog.Open(root, filetypes = [('*.trc files', '.trc')])
	filename = dialog.show()
	textbox.config(state='normal')
	textbox.delete('1.0', 'end')
	textbox2.delete('1.0', 'end')
	textbox3.delete('1.0', 'end')
	
	counterlist = []
	
	print (filename)
	if filename == '':
		return
	if not filename:
		return
	
	check_errors(filename)
	initial_parameters(filename)
	print ("Парсинг логфайла завершен")
	root.update_idletasks()
	textbox.mark_set('insert', '1.0')
	textbox.focus()
	textbox.config(state='disabled')

def LogBtn(event):#ev
	if filename == '':
		return

	global btnValue
	btnValue = 'Log'
	textbox.config(state='normal')
	textbox.delete('1.0', 'end') 
	logfile = open (filename, 'rt', encoding='latin1')

	textbox.insert('1.0', open(filename, 'rt', encoding='latin1').read())

	if btnValue == 'Log':
		check_log(filename)
		
	textbox.mark_set('insert', '1.0')
	textbox.focus()	
	textbox.config(state='disabled')


def BugBtn(event):#ev
	if filename == '':
		return
		
	global btnValue
	btnValue = 'Bug'
	textbox.config(state='normal')
	textbox.delete('1.0', 'end') 
	textbox.insert('1.0', open(filename,'rt', encoding='latin1').read())

	if btnValue == 'Bug':
		check_errors(filename)
	textbox.mark_set('insert', '1.0')
	textbox.focus()
	textbox.config(state='disabled')

	
#def ErlstBtn(event): #ev
#
#	print_er_codes()
#	textbox.config(state='normal')
#	textbox.mark_set('insert', '1.0')
#	textbox.focus()
#	textbox.config(state='disabled')


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
							stopindex=tk.END,  #ends with END index, no case sensitivity
							nocase =1
		)
		pos_coords = pos.split(".")

		textbox.tag_delete('found_text')    #text found, coords are defined, try to set up a tag but before delete tags from previous search: (tag_name, start_coord, end_coord)
		textbox.tag_add(
						'found_text','{}'.format(pos),
						'{}.{}'.format(pos_coords[0], int(pos_coords[1])+len(requestString))
		)
		textbox.tag_configure('found_text', background = "#ccff99")		#color of found text is ccff99 - lblue
		textbox.mark_set('insert', '{}'.format(pos))    #move coursor to the beginning of found text and focus on textbox to move scrollbar
		textbox.focus()
		
		try:
			scrollbar.config(command=textbox.yview('{}.0'.format(int(pos_coords[0])-5)))	#scrollbar move has a shift of 5 rows, but if there is no 5 vacation rows script just passes it
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
		error = tk.Tk()
		error.update_idletasks()
		error.focus_force()
		error.title('red alert')
		error.geometry('200x50')
		message = tk.Label(error, text='text wasn\'t found')
		message.pack()
		
		okBtn = tk.Button(error, text='Ok')
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
	global error
	global searchAgain
	searchAgain = True	
	error.destroy()
			
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
	global finder2
	global root
	
	if finder2 == 'Summonned':
		pass
	else:		
		finder2 = 'Summonned'

		searchWindow = tk.Tk()
		searchWindowWidth = 450
		searchWindowHeight = 70
		
		searchWindow.geometry ('{}x{}'.format(searchWindowWidth, searchWindowHeight))
		
		screenWidth = root.winfo_screenwidth()
		screenHeight = root.winfo_screenheight()
		
		
		positionRight = int(screenWidth/2 - searchWindowWidth/2)
		positionDown = int(screenHeight/2 - searchWindowHeight/2)
		
		searchWindow.geometry("+{}+{}". format(positionRight, positionDown))
		
		searchWindow.update_idletasks()
		searchWindow.focus_force()
		searchWindow.title ('Find')
		
		
		panelFinder = tk.Frame(searchWindow)
		panelFinder.pack(fill = tk.X)
		
		panelFinder2 = tk.Frame(searchWindow)
		panelFinder2.pack(fill = tk.X, side = tk.BOTTOM)
		
		requestText = tk.Label(panelFinder, text='Search for:')
		requestText.pack(side=tk.LEFT)
		
		requestField = tk.Entry(panelFinder, width=63)
		requestField.pack(side=tk.RIGHT, pady = 10, fill =  tk.X)
		
		firstCoord = textbox.index(tk.INSERT).split('.')
	
		finderRowCoord = int(firstCoord[0])
		finderLetterCoord = int(firstCoord[1])
	
		previousBtn = tk.Button (panelFinder2, text = 'Previous')
		nextBtn = tk.Button (panelFinder2, text='  Next  ')
		
		def destr():
			global searchWindow
			global finder2
			searchWindow.destroy()
			finder2 = 'sleep'
			
		cancelBtn = tk.Button (
							panelFinder2,
							text='Cancel',
							command = destr
		)
		searchWindow.protocol("WM_DELETE_WINDOW", destr)
		
		requestField.bind('<Return>', findString)
		requestField.bind('<KP_Enter>', findString)
		
		previousBtn.bind('<Button-1>', findString_reverse)
		nextBtn.bind('<Button-1>', findString)
		finder_name = searchWindow
		
		cancelBtn.pack(side=tk.RIGHT)
		nextBtn.pack(side=tk.RIGHT)
		previousBtn.pack(side=tk.RIGHT)

		
		hintText =tk.Label(
							panelFinder2,
							text = 'Hint: try Ctrl-F',
							font='TkDefaultFont 7',
							fg='#808080'
		)	
		hintText.pack(side = tk.LEFT)
		searchWindow.lift()
		searchWindow.focus_force()
		searchWindow.grab_set()
		searchWindow.grab_release()
		requestField.focus()
		searchWindow.call('wm', 'attributes', '.', '-topmost', '1')

		searchWindow.mainloop()
		
def openBrowser(event):
	filename='data/error_codes.html'
	webbrowser.open_new_tab('file://' + os.path.realpath(filename))


def opSettings(event):
	settingslib.openSettings(event, root)


root = tk.Tk()

root.title('HParser v1.0')
root.minsize(800, 500)

#root.update_idletasks()

#img = PhotoImage(file='hparser.gif') ПРОБЛЕМА изменения положения кнопок при добавлении иконки
#root.tk.call('wm', 'iconphoto', root._w, img)
#iconFile = tk.PhotoImage (file = 'hparser_small.png')
#root.iconphoto(False, iconFile)
root.state("zoomed")
#root.state('normal')

root.focus_force() 
root.configure(background="lightgrey", bd=1)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry("{}x{}".format(screenWidth-250, screenHeight-170))
panelFrame = tk.Frame(root, width=screenWidth, height = 32, bg = 'lightgrey')

panelFrame.pack(side=tk.TOP, fill=tk.X, expand = tk.NO)

logFrame = tk.Frame(bg = 'lightgrey')
logFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES, padx = 2, pady = 2)

textbox = tk.Text(logFrame, width = 20)
textbox.configure(font='courier 9')
scrollbar = tk.Scrollbar(logFrame, command = textbox.yview)
textbox['yscrollcommand'] = scrollbar.set
textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand = tk.YES)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand = tk.NO)

infoFrame = tk.LabelFrame(text='Информация о запуске', bg = 'lightgrey')
infoFrame.pack(side=tk.TOP, expand=tk.NO)

textbox2 = tk.Text(infoFrame, width=32, height = 18)
textbox2.configure(font='courier 9')
scrollbar2 = tk.Scrollbar(infoFrame, command = textbox2.yview)
textbox2['yscrollcommand'] = scrollbar2.set
textbox2.pack(side=tk.LEFT, expand = tk.NO)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y, expand = tk.NO)

erFrame = tk.LabelFrame (text='Коды ошибок', width = 35, bg = 'lightgrey')
erFrame.pack(side=tk.BOTTOM, fill=tk.Y, expand = tk.YES)

textbox3 = tk.Text(erFrame, width=32, background = 'lightgrey')
textbox3.configure(font='courier 9')
scrollbar3 = tk.Scrollbar(erFrame, command = textbox3.yview)
textbox3['yscrollcommand'] = scrollbar3.set,

textbox3.pack(side=tk.LEFT, fill=tk.BOTH, expand = tk.YES)
scrollbar3.pack(side=tk.RIGHT, fill=tk.Y, expand = tk.YES)


### buttons
loadBtn = tk.Button(panelFrame, text = 'Open')
logBtn = tk.Button(panelFrame, text = 'Log')
bugBtn = tk.Button(panelFrame, text = 'Bug')
erlstBtn = tk.Button(panelFrame, text = 'Error codes')
searchBtn = tk.Button(panelFrame, text = 'Find')#, text = unicode_string)
settingsBtn = tk.Button(panelFrame, text = 'Settings')

loadBtn.place(x = 2, y = 5, width = 42, height = 25)
logBtn.place(x = 52, y = 5, width = 42, height = 25)
bugBtn.place(x = 102, y = 5, width = 42, height = 25)
erlstBtn.place(x = 152, y = 5, width = 82, height = 25)
searchBtn.place(x = 242, y = 5, width = 42, height = 25)
settingsBtn.place(x = 342, y = 5, width = 82, height = 25)

textbox.bind('<Control-f>', createFinder)
loadBtn.bind("<Button-1>", LoadFile)
logBtn.bind("<Button-1>", LogBtn)
bugBtn.bind("<Button-1>", BugBtn)
erlstBtn.bind("<Button-1>", openBrowser)
searchBtn.bind("<Button-1>", createFinder)
settingsBtn.bind("<Button-1>", opSettings)
#функция для вывода кодов и имен нажатий клавиш используется с _.bind('<Key>', prntKey)
#def print_event(event):
#	print ("Event character code <char>: '%s'" % event.char)
#	print ("   Event key symbol <keysym>: '%s'" % event.keysym)
#	print ("   Event key code <keycode>: '%s'" % event.keycode)
#	if event.char == 'а':
#		if event.
#		print ("1")
#def search_bind(event):
#	if event.keycode == 70:# or event.keycode == 17:
#		createFinder()
#textbox.bind("<Key>", print_event)
		
#textbox.bind('<Key>', search_bind)
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
