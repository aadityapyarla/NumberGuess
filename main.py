import random
print("You have to guess a number b/w 1 to 9")
print("You all have is 3 chances to guess!")
secret_num = random.randint(1, 9)
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("> "))
    guess_count += 1
    if guess == secret_num:
        print("Hurray....!")
        print("You won!")
        break
else:
    print("Sorry you lose...")
    print(f"The number was {secret_num}")
