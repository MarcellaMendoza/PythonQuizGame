print("Welcome to my computer quiz!")

playing = input("Would you like to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? " )
if answer.lower() == "central processing unit":
    print("That's CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does GPU stand for? " )
if answer.lower() == "graphics processing unit":
    print("That's CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does RAM stand for? " )
if answer.lower() == "random access memory":
    print("That's CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("What does PSU stand for? " )
if answer.lower() == "power supply":
    print("That's CORRECT!")
    score += 1
else:
    print("INCORRECT!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%!")