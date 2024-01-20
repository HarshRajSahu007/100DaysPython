import random
value=random.choice(range(1,101))
print("""\_    _/..__   __    /   __/ __   __   __/  ||  |_ |_| __    ___   
  |    | <   |  |\__ \/ _ \   \__  \ /  _ \ /     \/ _ \   _\  |  \|  |/    \  / _\  
  |    |  \_  ||  |> >  _/   /        (  <> )  Y Y  \  _/|  | |   Y  \  |   |  \/ /_/  > 
  |_|  / __||   _/ \_  > /___  /\_/|||  /\_  >_| |_|  /|_|  /\__  /  
          \/     |_|        \/          \/             \/     \/          \/        \//__/""")
def easy_func():
    guess=10
    print(f"You have {guess} guesses")
    while guess!=0:
        elem=int(input("Enter your choice:"))
        if elem>value:
            print("Too High")
            guess=guess-1
        elif elem<value:
            print("Too low")
            guess=guess-1
        else:
            print(f"You guessed correct in {guess} guesses")
            break
    if guess==0:
        print("You lost")
    else:
        print("You won")

def hard_func():
    guess=5
    print(f"you have {guess} guesses")
    while guess!=0:
        elem=int(input("Enter your choice:"))
        if elem>value:
            print("Too High")
            guess=guess-1
        elif elem<value:
            print("Too low")
            guess=guess-1
        else:
            print(f"You guessed correct in {guess} guesses")
            break

    if guess==0:
        print("You lost")
    else:
        print("You won")   



print("Welcome to the Number Guessing game!!!!")
diff=input("Enter the difficulty if hard type 'hard' or type 'easy' for easy: ")
if diff=='easy':
    easy_func()
else:
    hard_func()