from mrowki import mrowki
import time

#wczytywanie z pliku

f=open("m50.txt", 'r')

# s=input("podaj nazwę pliku: ")
# f=open(s, 'r')

n=int(f.readline())
n_zad=int(f.readline())
l=[]
for i in range(n_zad):
    l.append(int(f.readline()))
f.close()


#algorytm zachłanny

def zachlanny(n,l):
    #l.sort(reverse=True)
    p=[[] for i in range(n)]
    for i in range(len(l)):
        min = 1000000
        for j in range(n):
            if sum(p[j])<min:
                min=sum(p[j])
                tmp=j
        p[tmp].append(l[i])
    return p

print("lista wejściowa zadań: ", l)

print("lower bound: ", sum(l)/n)

print("\n*zachlanny*")
p=zachlanny(n,l)
lp=[0]*len(p)
for i in range(len(p)):
    lp[i]=sum(p[i])
print(lp)
print("maksymalny czas wykonywania: ", max(sum(p[i]) for i in range(n)))

print("\n*mrowki*")
t1=time.time()
min=mrowki(len(l),n,l,50,0.5,0.5,1,1)
t2=time.time()
t=t2-t1
print("maksymalny czas wykonywania: ", min)
print("czas: ", t)
