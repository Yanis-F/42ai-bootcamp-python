import random

def guess_game():
    answer = random.randint(1, 99)

    print("What's your guess between 1 and 99?")
    while True:
        user_input = input()

        if user_input == "exit":
            return
        
        try:
            guess = int(user_input)
            
            if guess < 1 or guess > 99:
                raise Exception("Guess must be between 1 and 99 included")

            if guess < answer:
                print("Too low!")
            elif guess > answer:
                print("Too high!")
            else:
                if answer == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulation, you've got it!")
                return
        except Exception as e:
            print("Invalid input : " + e)


if __name__ == "__main__":
    guess_game()
