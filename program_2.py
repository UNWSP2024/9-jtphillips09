# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

def write_random_numbers():
    ######################
    # Add your code here #
    ######################
    count = int(input('How many random numbers should the file hold (up to 1000)? '))
    if count < 1 or count > 1000:
        print('Please enter a number between 1 and 1000.')
        return

    with open('random_numbers.txt', 'w') as file:
        for _ in range(count):
            num = random.randint(1, 500)
            file.write(str(num) + '\n')

    print('random_numbers.txt has been created with', count, 'random numbers.')


# You don't need to change anything below this line:
if __name__ == '__main__':
    write_random_numbers()
