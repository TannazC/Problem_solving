import random
target = random.randint(100, 999)
print("I'm thinking of a three-digit number.")
print("Each digit that matches one of mine earns a point.")

while True:
    user_num = int(input("Enter a three-digit positive number: "))
    
    if user_num>=100 and user_num<=999:
        print("The number is ", target, ".", sep="")
        correct = 0
        if user_num % 10 == target % 10:
            print("The last digits match.")
            correct += 1
        if user_num // 10 == target // 10:
            print("The middle digits match.")
            correct += 1
        if user_num // 100 == target // 100:
            print("The first digits match.")
            correct += 1
        if correct == 0:
            print("Nothing matches.")
        print("You scored", correct, "points.")
        break
    else:
        print("Your Input is inavlid. Try again.")
