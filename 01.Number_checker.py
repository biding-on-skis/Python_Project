# functions go here

# num checker
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter a number")




