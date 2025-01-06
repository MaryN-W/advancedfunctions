# Lambda => A one line anonymous function; contains a single expression which is evaluated and returned
def add_ten(num):
    return num + 10

add_ten_lambda = lambda num: num + 10 # turn above into lambda

print(add_ten_lambda(10))