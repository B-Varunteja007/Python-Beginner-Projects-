import random
while True:
    print("DICE SI ROLLING...")
    print("THE CHOICE IS ..:",random.randint(1,6))
    repeat=input("Do yoy wish to continue?if yes press y else press n")
    if repeat=='n':
        break