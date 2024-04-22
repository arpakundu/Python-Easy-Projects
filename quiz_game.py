print("Welcome to my python quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What method is used to remove the last element from a list in Python? ")
if answer.lower() == "pop()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What keyword is used to define a function in Python? ")
if answer.lower() == "def":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which data type is mutable in Python: tuple or list? ")
if answer.lower() == "list":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How do you check the length of a string in Python? ")
if answer.lower() == "len()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which keyword is used to define a conditional statement in Python? ")
if answer.lower() == "if":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does the import keyword do in Python? ")
if answer.lower() == "import modules":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What function is used to convert a string to lowercase in Python? ")
if answer.lower() == "lower()":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does the '%' operator do in Python? ")
if answer.lower() == "modulus":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")