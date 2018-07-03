def get_age():
	age = int(raw_input("What is your age please: "))
	return age
	
def get_name():
	name = raw_input("What is your name please: ")
	return name
	
user_name = get_name()
user_age = get_age()

print "Hello " + user_name
print "You are " + str(user_age) + " years old"
