import random

# s=input("podaj nazwę pliku: ")
# f=open(s, 'w')

f=open("losowe.txt", 'w')

n_proc=int(input("podaj ilość procesorów: "))
n_zad=int(input("podaj ilość zadań: "))

f.write(f"{n_proc}\n")
f.write(f"{n_zad}\n")

for i in range(n_zad):
    tmp = random.randint(1,100)
    f.write(f"{tmp}\n")

f.close()
