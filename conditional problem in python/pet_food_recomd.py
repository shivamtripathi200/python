# Recommend a type of pet food based on the pets species and age(eg: Dog < 2 years - puppy food,cat > 5 years - senior cat food )
animal = 'cat'
age = 7

if animal.upper() == 'DOG': 
    if age < 2:
        print('give the dog puppy food')
    else:
        print('give the dog adult food')

elif (animal.upper() == 'CAT' and age > 5):
    print('give the cat senior cat food')
else:
    print('the cat is too  young to eat senior cat food')