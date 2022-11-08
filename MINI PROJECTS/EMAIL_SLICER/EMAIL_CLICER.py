email=input("ENTER YOUR EMAIL ID:").strip()
username=email[:email.index('@')]
domain=email[email.index('@')+1:]
print("THE USERNAME IS:",username)
print("THE DOMAIN IS: ",domain)
