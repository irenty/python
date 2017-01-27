def get_name():
    while True:
    	name = raw_input("---\nHello, what is your name? ")
    	if name.upper() == 'FELIX':
    		return 'Felix'
    	elif name.upper() == 'NELA':
    	    return 'Nela'
    	print "I don't know you {0}, please go away!\n".format(name)

if __name__ == "__main__":
    get_name()  