print('Welcome to VoteReg! A mandatory screening for voting inquirers will be held at this time. All provided information is and will remain confidential.')

age = int(input('Enter your age: '))
if age >= 90:
    print('You are too old to vote!')
elif age >= 18:
    print('You are old enough to vote!')
    name = input('Enter your first and last name: ')
    if name == '':
        print('You must enter a first and last name!')
    else:
        print(f'Hello {name}!')


    response = input('Are you a citizen? (yes/no): ')
    if response == 'yes':
        print('Continue with the questionnaire')
        state_name = input('What is your residential state?: ')
        print(f'Your residential state is {state_name}!')

        response = input('Are you active duty military or reserves? (yes/no): ')

        repsonse = input('Are you a veteran? (yes/no): ')

        repsonse = input('Have you traveled in the last ninety days? (yes/no): ')
        if repsonse == 'no':
            print('You are not subject to random illness testing!')
            print('Congratulations, you are a voter!')
        else:
            print('You are subject to random illness testing!')
            print('Please try registering after test results return negative.')
    elif response == 'no':
        print('Sorry, you are not eligible for voting.')





else:
    print('You must be 18+ to vote!')



