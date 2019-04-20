
print ("Welcome to the Game")
name = input("What is your name? >")
print ("Hello" + name)
import random
random_number = random.randint(1, 100)
print (random_number)
count = 1

user_number = input("Tell me a number from 1 to 100 >")
while int(user_number) != int(random_number):
	user_number = input("Try again >")

	if int(user_number) > int(random_number):
		print ("too hight")
	elif int(user_number) < int(random_number):
		print ("too low")
	count += 1
	
print ("yes! " + name + " you are right! and it only took you " + str(count) + " times")






