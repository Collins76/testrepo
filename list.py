import random

list_of_names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

random_names = list_of_names
random_names = random.randrange(0, 5)
if random_names == 0:
    print("Angela is going to buy the meal today!")
elif random_names == 1:
    print("Ben is going to buy the meal today!")
elif random_names == 2:
    print("Jenny is going to buy the meal today!")
elif random_names == 3:
    print("Michael is going to buy the meal today!")
else:
    print("Chloe is going to buy the meal today!")

row1 = ["◻️", "◻️", "◻️"]
row2 = ["◻️", "◻️", "◻️"]
row3 = ["◻️", "◻️", "◻️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")


print("Welcome to Rock, Paper, Scissors game!")
choice = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.").lower()

random_choice = choice
random_choice = random.randint(0, 2)

if random_choice == "Rock" == 0:
    print(''' Computer chose rock:             
            
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
  
    ''')


else:
    print(''' You choose paper:
            _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
  You win  ''')


if random_choice == "Rock" == 0:
    print(''' Computer chose rock:             

---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    ''')


else:
    print(''' You chose Scissors:
       _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

  You loose  ''')


if random_choice == "Paper" == 1:
    print('''  Computer chose paper:            
            _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''')


else:
    print(''' You chose rock:
    
 ---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    You loose!
    ''')


    if random_choice == "Paper" == 1:
        print('''  Computer chose paper:            
                _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
        ''')


    else:
        print(''' You chose Scissors:

         _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

        You win!
        ''')


if random_choice == "Scissors" == 2:
    print('''   Computer chose Scissors:          
         _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

else:
    print(''' You chose paper:  
               _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)      
   
    You loose!
    ''')

if random_choice == "Scissors" == 2:
    print('''   Computer chose Scissors:          
         _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

else:
    print(''' You chose rock:  
 ---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)     

    You win!
    ''')
