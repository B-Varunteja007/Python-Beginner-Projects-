user_input=input("ENTER THE USER INPUT PHRASE").lower()
phrase=user_input.replace("of","").split()
acronym=""
for word in phrase:
    acronym=acronym+word[0].upper()
print(f"THE ACRONYM OF {user_input} is {acronym}")
