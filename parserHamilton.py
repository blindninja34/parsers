print ("Поместите скрипт в папку со логфайлом. Скопируйте целиком имя логфайла вместе с расширением в консоль:\n")

log = input()
logfile = open(log)
parsefile = open('parse.txt', 'w')

error = "error"
Error = "Error"
no_Error = "No Error"
no_error = "No Error"
warning = "Warning"

for line in logfile:
	if error in line:
		if no_error not in line:
			parsefile.write(line + '\n\n\n')
	elif Error in line:
		if no_Error not in line:
			parsefile.write(line + '\n\n\n')
			
	if warning in line:
		
		parsefile.write(line + '\n\n\n')
		
parsefile.close
logfile.close
print ("Парсинг логфайла завершен, создан файл parse.txt.")

