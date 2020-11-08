from random import seed
from random import gauss

seed = int(input("Masukan Nilai N: "))

for i in range(seed):
    value = gauss(0,5)
    print ("Data ke ", i, ":", value)
