import tkinter as tk
from tkinter import filedialog

def readSettingsFile(featureList):
	settingsFile = open('data/settings.txt', 'rt', encoding='latin1')
	for line in settingsFile:
		featureList.insert("end", line)
	settingsFile.close()

def readParametersFile(parameterList):
	parametersFile = open('data/parameters_ru.txt', 'rt')
	for line in parametersFile:
		parameterList.insert("end", line)
	parametersFile.close()

def writeSettingsFile(feature ,filepath):
	settingsFile = open(filepath, 'at')
	settingsFile.write(feature)
	settingsFile.truncate()
	settingsFile.close()

def removeLine(feature, filepath):
	with open(filepath, "r+") as settingsFile:
		lines = settingsFile.readlines()
		settingsFile.seek(0)
		for line in lines:
			if line != feature:
				settingsFile.write(line)
		settingsFile.truncate()
		settingsFile.close()

def addFeature(myList, myEntry, filepath):
	if not myEntry.get():
		pass
	else:
		entryString = myEntry.get()
		if entryString.isspace():
			pass
		else:
			myList.insert("end", myEntry.get())
			writeSettingsFile(entryString, filepath)
	myEntry.delete(0, "end")

def delFeature(myList, myEntry, filepath):
	try:
		removeLine(myList.get(myList.curselection()), filepath)
		myList.delete(myList.curselection())
	except tk.TclError as exception:
		pass
	myEntry.delete(0, "end")

def openSettings(event, root):

	settingsWindow = tk.Tk()
	settingsWindow.resizable(False, False)
	settingsWindow.configure(background='lightgrey')
	settingsWindowWidth = 600
	settingsWindowHeight = 600
	settingsWindow.geometry ('{}x{}'.format(settingsWindowWidth, settingsWindowHeight))
	screenWidth = root.winfo_screenwidth()
	screenHeight = root.winfo_screenheight()
	positionRight = int(screenWidth/2 - settingsWindowWidth/2)
	positionDown = int(screenHeight/2 - settingsWindowHeight/2)
	settingsWindow.geometry("+{}+{}". format(positionRight, positionDown))
	settingsWindow.update_idletasks()
	settingsWindow.focus_force()
	settingsWindow.title ('Settings')

	feature = tk.StringVar()
	parameter = tk.StringVar()
	upFrame = tk.Frame(settingsWindow)
	downFrame = tk.Frame(settingsWindow)
	bottomFrame = tk.Frame(settingsWindow)

	featureScrollbar = tk.Scrollbar(upFrame)
	parameterScrollbar = tk.Scrollbar(upFrame)
	featureList = tk.Listbox(upFrame, width=30 , height=20
								, yscrollcommand = featureScrollbar.set)
	parameterList = tk.Listbox(upFrame, width=30, height=20
								, yscrollcommand = parameterScrollbar.set)

	newParameter = tk.Entry(downFrame, width = 15, textvariable = parameter)
	newFeature = tk.Entry(downFrame, width = 15, textvariable = feature)
	
	addParameterBtn = tk.Button(bottomFrame
								, text ="Add parameter"
								, command = lambda: addFeature(parameterList
																, newParameter
																, 'data/parameters_ru.txt')
								)
	delParameterBtn = tk.Button(bottomFrame
								, text ="Del parameter"
								, command = lambda: delFeature(parameterList
																, newParameter
																, 'data/parameters_ru.txt')
								)
	addFeatureBtn = tk.Button(bottomFrame
								, text ="Add feature"
								, command = lambda: addFeature(featureList
																, newFeature
																, 'data/settings.txt')
								)
	delFeatureBtn = tk.Button(bottomFrame
								, text ="Del feature"
								, command = lambda: delFeature(featureList
																, newFeature
																, 'data/settings.txt')
								)

	upFrame.pack()
	downFrame.pack()
	bottomFrame.pack()
	parameterList.pack(side = tk.LEFT, fill = tk.X)
	parameterScrollbar.pack(side = tk.LEFT, fill = tk.Y)
	featureList.pack(side = tk.LEFT, fill = tk.X)
	featureScrollbar.pack(side = tk.LEFT, fill = tk.Y)

	newParameter.pack(side = tk.LEFT, fill = tk.X)
	addParameterBtn.pack(side = tk.LEFT)
	delParameterBtn.pack(side = tk.LEFT)

	newFeature.pack(side = tk.RIGHT, fill = tk.X)
	addFeatureBtn.pack(side = tk.RIGHT)
	delFeatureBtn.pack(side = tk.RIGHT)

	readSettingsFile(featureList)
	readParametersFile(parameterList)


	
	



