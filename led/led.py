
# names
FELIX = 'Felix'
NELA = 'Nela'
# commands
ON = 'ON'
OFF = 'OFF'
ASKNAME = ''
# colors
RED = 'RED'
GREEN = 'GREEN'
BLUE = 'BLUE' 

COLOR_CODES = {
	RED: '\x1b[6;30;31m',
	GREEN: '\x1b[6;30;32m',
	BLUE: '\x1b[6;30;34m'
}

NC = '\x1b[0m' # No Color

PIN_NUMBER = {  (FELIX, RED): 11,
				(FELIX, GREEN): 12,
				(FELIX, BLUE): 13,
				(NELA, RED): 14,
				(NELA, GREEN): 15,
				(NELA, BLUE): 16}

def get_name():
    while True:
    	name = raw_input("---\nHello, what is your name? ")
    	nameUpper = name.upper()
    	if nameUpper == FELIX.upper():
    		return FELIX
    	elif nameUpper == NELA.upper():
    	    return NELA
    	print ">>> I don't know you {0}, please go away!\n".format(name)

def get_command(name):
    while True:
    	commandStr = raw_input("\n---\nOK {0}, what can I do for you today? ".format(name))
    	if not commandStr:
    		return (ASKNAME, '')
    	commandStrUpper = commandStr.upper()
    	command = ''
    	if ON in commandStrUpper:
    		command = ON
    	elif OFF in commandStrUpper:
    		command = OFF
    	color = ''
    	if RED in commandStrUpper:
    		color = RED
    	elif GREEN in commandStrUpper:
    		color = GREEN	
    	elif BLUE in commandStrUpper:
    		color = BLUE	

    	if not command or not color:
    		print ">>> Sorry, I don't understand that!"
    	else:
    		return (command, color)

def change_colors(name, command, color):
	color_code = COLOR_CODES[color]
	print ">>> OK {0}, {1}{2}{3} is turning {4}".format(name, color_code, color.lower(), NC, command.lower())
	pin = PIN_NUMBER[(name, color)]

	print "turning pin {0} {1}".format(pin, command.lower())


def main():
	name = get_name()
	while True:
		(command, color) = get_command(name)
		if command == ASKNAME:
			name = get_name()
		else:
			change_colors(name, command, color)

if __name__ == "__main__":
    main()  