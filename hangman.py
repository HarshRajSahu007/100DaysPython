import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list=['dulal','minu','kumar','buron','sunny']
word=random.choice(word_list)
uscore=[]
lives=6
for let in word:
   uscore.append("_")
print(word)
end_of_game=False
while not end_of_game:
  choice=input("Enter a key: ")
  for position in range(len(word)):
     letter=word[position]
     if letter==choice:
        uscore[position]=letter
  print(uscore)
  if choice not in word:
     lives=lives-1 
     if lives<0:
       print("You lost") 
       break
  print(f"{' '.join(uscore)}")
  if "_" not in uscore:
    print("You win")
    break
  print(stages[lives])