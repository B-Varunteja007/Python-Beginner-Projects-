import random
pass_len=int(input("Enter the length of Password"))
pass_input="qwertyuiopasdfghjklzxcvbnm[]{};:<>,.?/*-+|"
password="".join(random.sample(pass_input,pass_len))
print(password)