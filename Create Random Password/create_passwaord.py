import random
import string

pass_len  = 12
value = string.ascii_letters + string.digits +string.punctuation

password = ""


for i in range(pass_len):
     password += random.choice(value)

print("Your Random Password Is :" , password)
  