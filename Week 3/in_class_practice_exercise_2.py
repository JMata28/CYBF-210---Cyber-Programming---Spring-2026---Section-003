my_phonebook= {
    "Ross" : "1112223333",
    "Ronald" : "9990007777",
    "Ryan" : "3334445555"
}
while(True):
    answer = input("Choose '1' to add a new number. Choose '2' to look up a person in the phonebook.")
    if (answer == "1"):
        key = input("Enter the name of the person: ").title()
        value = input(f"Enter the number of {key}: ")
        my_phonebook[key] = value
        print(f"The number for {key} was succesfully added to the phonebook!")
    elif (answer == "2"):
        name = input("Enter the name of the person you're looking for: ").title()
        if (name in my_phonebook):
            print(f"{name} has the phone number: {my_phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook. Please try again.") 
    else:
        print("Invalid input. Please try again.")