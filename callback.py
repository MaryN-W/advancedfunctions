# Callback => A function that you pass in to another function as an argument
import time

def greet(name, callback): # callback is arbitrary / cb
    print(f'Hello, {name}!')
    # time.sleep(3)
    callback()

def say_bye():
    print('Bye!!')

def shout(): # another function that does something different
    for i in range(5):
        print('GOODBYE!!!!!')

    # Main
greet('Wangari', say_bye) # No parenthesis say_bye() => not being called immediately
greet('Njuguna', shout) # Once greet finishes


print('Continuining main ...')
# More statements