import random
import string

n = 100

val_str = ''.join([random.choice(string.ascii_lowercase) for i in range(n)])
