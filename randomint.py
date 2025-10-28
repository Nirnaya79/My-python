import random


def ran(min_num, max_num):
    count = 0
    print("Enter a number between " + str(min_num) + " and " + str(max_num))

    num = random.randint(min_num, max_num)
    # Uncomment the line below to test easily
    # print(f"DEBUG: Random number is {num}")

    while count < 3:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        count += 1

        if guess == num:
            print("You guessed it! You win!")
            break
        elif guess < num:
            print("Too low!")
        else:
            print("Too high!")

    else:
        print(f"You lost. The correct number was {num}.")


ran(min_num=1, max_num=10)


