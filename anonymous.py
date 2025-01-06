# Callback => A function that you pass in to another function as an argument

def greet(name, callback): # callback is arbitrary / cb
    print(f'Hello, {name}!')
    callback()

# def say_bye():
#     print('Bye!!')

say_bye = lambda: print('Bye!!')

    # Main
greet('Wangari', say_bye) # No parenthesis say_bye() => not being called immediately

# refine say_bye further
# greet('Wangari', lambda: print('Bye!!')) # used once, otherwise use variable above
