def calculate(opt, f, s):
	opt = opt.lower()
	if opt == "add":
		return f + s
	elif opt == "substruct":
		return f - s
	elif opt == "multiply":
		return f * s
	elif opt == "divide":
		return f / s
	else:
		print "Operator Invalid"
		
print calculate("add", 5, 8)
	
			
