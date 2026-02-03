#Keep in mind that the code below can be simplified even more, but it is more explicitly broken down in several lines for it to be easier for students to follow.
name = input("Please enter your name: ")
age = int(input("Please enter your age: ")) #Turning string input to int type so we can manipulate it later in the code
future_message = input("What is your message for your future self?: ")
length_of_name = len(name) 
#name[0] accesses the first letter of the string and .lower() makes it lowercase
first_letter = name[0].lower()
first_letter_count = name.lower().count(first_letter) #the .count method returns the number of occurrences.
decades = age/10
years_to_a_hundred = 100-age
calculated_year = 2026 + years_to_a_hundred
capitalized_message = future_message.upper()
print(f"Hello {name}!\nYour name has {length_of_name} letters.\nThe first letter of your name is found {first_letter_count} times in your name.\nYou are {age} years old! In other words, you have lived for {decades} decades! That means that in {years_to_a_hundred} years, you will be 100 years old: That is in the year {calculated_year}!\nThis is your message for your future self: {capitalized_message}")

