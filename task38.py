# We're going to make our own rock-paper-python game, where paper beats rock, rock beats python, and python beats paper. 
computer_choice= 'rock'
user_choice= input('enter rock, paper, or python:\n')
if computer_choice == user_choice :
    print('TIE')
# IMPROVE on the code we just wrote to add some cases where a user can win.
# else: 
#    print('you lose :( computer wins :D)')
if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'python':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'python' and computer_choice == 'paper':
    print('WIN')    
