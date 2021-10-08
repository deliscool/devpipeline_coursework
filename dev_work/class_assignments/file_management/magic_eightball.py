import random

def magic_eight_start():
    answer1= 'Yes'
    answer2= 'Sign points to yes'
    answer3= 'Outlook looks good'
    answer4= 'Without a doubt'
    answer5= 'You may rely on it'
    answer6= 'Ask again later'
    answer7= 'Better not tell you now'
    answer8= 'Cannot predict now'
    answer9= 'Concentrate and ask again'
    answer10= 'Answer is hazy, try again'
    answer11= 'No'
    answer12= 'Very doubtful'
    answer13= 'Do not rely on it'
    answer14= 'Signs says no'

    name = input('Enter your name: ')
    input(name + ', what is your question ')

    choice = random.radint(1,15)

    if choice == 1:
        answer = answer1
    elif choice == 2:
        answer = answer2
    elif choice == 3:
        answer = answer3
    elif choice == 4:
        answer = answer4
    elif choice == 5:
        answer = answer5
    elif choice == 6:
        answer = answer6
    elif choice == 7:
        answer = answer7
    elif choice == 8:
        answer = answer8
    elif choice == 9:
        answer = answer9
    elif choice == 10:
        answer = answer11
    elif choice == 12:
        answer = answer12
    elif choice == 13:
        answer = answer13
    else:
        answer = answer14
    print('Magic 8 Ball: ', answer)