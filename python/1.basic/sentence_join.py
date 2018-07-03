x = "go"

word_list = []

while x != "stop":
	word = raw_input("Add new Word, stop to end : ")
	x = word
	if x != "stop":
		word_list.append(word)

new_sentence = ""

for wrd in word_list:
	new_sentence += wrd + " "

print "The word joined into a sentence become"
print new_sentence
	
