import random 
import string

pass_len=12
charValue=string.ascii_letters + string.digits + string.punctuation

password=" "
for i in range (pass_len):
    password=random.choice(charValue)

    print("The random password is:-", password)