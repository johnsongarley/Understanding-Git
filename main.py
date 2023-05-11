#Basic

my_firstname = "Johnson"
my_lastname = "Garley"
full_name = my_firstname + " " + my_lastname
This_year = 2023
my_birth_year = 2001
age = This_year - my_birth_year

print("My name is " + str(full_name) + " and I am " + str(my_birth_year) + " of age.")

# Counting letter in a string

quote = "I am Liberian, my family is from the city of Zwedru in Grand gedeh county"
letters_list = ['i', 'a']

for j in letters_list:
    count = 0
    for num in range(len(quote)):
        if num < len(quote):
            if quote[num] == j:
                count= count + 1
    print(count)

