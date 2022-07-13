import string
import random
s=4
res=''.join(random.choices(string.ascii_uppercase + string.digits,k=s))
print("The generated random string :  " + str(res))
print("vcet"==str(res))