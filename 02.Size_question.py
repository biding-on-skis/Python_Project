
# function to check for yes or no input
def size_checker(question, valid_ans):
    while True:

        error = f"enter a valid option from {valid_ans}"

        user_response = input(question).lower()

        for item in valid_ans:
            # check if user response is a valid answer
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()

size_option = ["large", "medium", "small"]

# Ask for size
size = size_checker("What Size | Small | Medium | Large |: ", size_option)

if size == "large":
    print(f"You chose a large", 1, 18)

elif size == "medium":
    print(f"You chose a Medium", 1, 18)

else:
    print(f"you chose a Small", 1, 18)




