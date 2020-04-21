import string
import random
chars = string.ascii_letters + string.digits
#print(random.choice(chars))
n = 8
s = ''
mystr = s.join([random.choice(chars) for i in range(n)])
print(mystr)
