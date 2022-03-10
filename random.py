import random
computer_number = random.randint(10, 20)
attempts = 0
while True:
    user_number = int(input())
    attempts = attempts + 1
    if user_number == computer_number:
        print("Correct")
        break
    elif user_number < computer_number:
        print("Go up")
    elif user_number > computer_number:
        print("Come Down")
print("You try for:", attempts, "times.")