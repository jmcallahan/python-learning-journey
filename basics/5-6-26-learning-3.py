

keyword = "chupacabra"

user_word = str(input("Enter a word, human!: "))
while user_word != keyword:
	print("No, no, no, human, that is not correct! Try entering \"chupacabra\"")
	user_word = str(input("Try again, human: "))
	continue
if user_word == keyword:
	print("You've successfully left the loop")



