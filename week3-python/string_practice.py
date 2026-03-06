# Task 1

first_name = "Asantewa"
last_name = "Appiah"
age = 21
favorite_concept = "Linux CLI"

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Age: {age}")
print(f"Favorite Concept: {favorite_concept}")


# Task 2

full_name = first_name + " " + last_name
print(f"Full Name with + operator: {full_name}")

full_name_fstring = f"{first_name} {last_name}"
print(f"Full Name with f-string: {full_name_fstring}")


# Task 3

print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Count of letter 'a': {full_name.lower().count('a')}")
print(f"Index of first space: {full_name.find(' ')}")
print(f"Replaced Name: {full_name.replace(first_name, 'Coder')}")


# Task 4

intro = f"Hi, I am {full_name}. I am {age} years old and my favourite concept so far is {favorite_concept}."
print(intro)


# Task 5

space_index = full_name.find(" ")
print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")
print(f"First name only: {full_name[:space_index]}")


'''Task 1: Declare variables for your first name, last name, age (as a number),
and your favourite programming concept learned so far. Print each one.
• Task 2: Concatenate your first and last name with a space between them using
the + operator. Print the result. Then do the same using an f-string.
• Task 3: Using your full name variable from Task 2, use string methods to:
print it in all uppercase, all lowercase, count how many times the letter 'a'
(any case) appears (hint: apply lower() first), find the index of the first
space, and replace your first name with 'Coder'.
• Task 4: Write an f-string that forms a complete sentence introducing yourself,
including your name, age, and favourite concept. Example structure: 'Hi, I
am [name]. I am [age] years old and my favourite concept so far is
[concept].'
• Task 5: Use string indexing and slicing on your full name to print: the first
character, the last character (use a negative index), and only your first name
(slice from 0 up to where the space is)'''
'''#Task 1
first_name = "John"
last_name = "Doe"
age = 30
favourite_concept = "functions"
print(first_name)
print(last_name)
print(age)
print(favourite_concept)

#Task 2
full_name_concat = first_name + " " + last_name
print(full_name_concat)
full_name_fstring = f"{first_name} {last_name}"
print(full_name_fstring)

#Task 3
print(full_name_fstring.upper())
print(full_name_fstring.lower())
print(full_name_fstring.lower().count('a'))
print(full_name_fstring.find(' '))
print(full_name_fstring.replace(first_name, 'Coder'))'''


