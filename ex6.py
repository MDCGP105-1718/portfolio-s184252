print("Enter your details when prompted!")
name = input('Name: ')
age = int(input('Age: '))
height = int(input('Height(cm): '))
weight = int(input('Weight(kg): '))
eye_colour = input('Eye Colour: ')
hair_colour = input('Hair Colour: ')

print(f"Hello {name}! Let's discuss your details.")
print(f"You are {age} years old at the moment", end='')

# Trying ternary operator
print(" grandad!") if(age > 30) else print(".")
print(f"You are {height}cm tall, and weigh {weight}kg.", end='')
if(weight > 40):
    print(".. I'd slow down on the chips if I were you.")
print(f"Your eyes are {eye_colour} and your hair is {hair_colour}.")
