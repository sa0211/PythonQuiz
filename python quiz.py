# QUIZ GAME 

print('Hello, Welcome to the Quiz Game')

ans = input('Are you ready to play the Quiz game (yes/no):')
score = 0
total_q = 7

if ans.lower() == 'yes' or ans.lower() == 'y':
    ans = input('1. What is your name? ')
    

    ans = input('2. A person who studies plants is called?\n')
    if ans.lower() == 'botanist':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

        
    ans = input('3.A person who studies animals is called?\n')
    if ans.lower() == 'zoologist':
        score += 1
        print('correct')
    else:
        print('incorrect')

    ans = input('4.How many years are there in a decade?\n')
    if ans.lower() == '10':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    ans = input('5.Which country is second biggest in the world?\n')
    if ans.lower() == 'canada':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
        

    ans = input('6.What is capital of Spain?\n')
    if ans.lower() == 'madrid':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('7.What is the capital of South Korea?\n')
    if ans.lower() == 'seoul':
        score += 1
        print('Correct')
    else:
        print('Incorrect')


    print('Thank you for playing the Quiz , you got',score,"questions correct.")
    mark = (score/total_q)*100

    print("Marks:",str(mark)+'%')
    print("You Passed")
   
   

print('Goodbye!!')
print('Have a Nice Day!!')

    


 
