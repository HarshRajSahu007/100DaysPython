rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissors = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''
import random
game=[rock,paper,scissors]
compy=random.choice(game)
select=int(input("Enter 0 for Rock,1 for paper,2 for scissors: "))
if(select==0):
    if(compy==rock):
        value1=game.index(rock)
        print(f"Computer's choice:{value1}")
        print(compy)
        print("Your choice:")
        print(rock)
        print("Match Draw")

    elif(compy==paper):
        value2=game.index(paper)
        print(f"Computer's choice:{value2}")
        print(compy)
        print("Your choice:")
        print(rock)
        print("Match lost")

    elif(compy==scissors):
        value3=game.index(scissors)
        print(f"Computer's choice:{value3}")
        print(compy)
        print("Your choice:")
        print(rock)
        print("Match Win")
if(select==1):
    if(compy==rock):
        print("Computer's choice: ")
        print(compy)
        print("Your choice:")
        print(paper)
        print("Match Win")
    elif(compy==paper):
        print("Computer's choice: ")
        print(compy)
        print("Your choice:")
        print(paper)
        print("Match Draw")   
    elif(compy==scissors):
        print("Computer's choice: ")
        print(compy)
        print("Your choice:")
        print(paper)
        print("Match lost") 
if(select==2):
    if(compy==rock):
        print("Computer's choice: ")
        print(compy)
        print("Your choice:")
        print(scissors)
        print("Match lost")
    elif(compy==paper):
        print("Computer's choice: ")
        print(compy)
        print("Your choice:")
        print(scissors)
        print("Match Win") 
    elif(compy==scissors):
        print("Computer's choice: ")
        print(compy)
        print("Your choice:")
        print(scissors)
        print("Match Draw") 

print("Thank you for playing")