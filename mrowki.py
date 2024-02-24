import random

def zachlanny(n,l):
    p=[[] for i in range(n)]
    droga=[]
    for i in range(len(l)):
        min = sum(l)
        for j in range(n):
            if sum(p[j])<min:
                min=sum(p[j])
                tmp=j
        p[tmp].append(l[i])
        droga.append(tmp+1)
    return droga

def max_listy(l):
    max_i = 0
    max = l[0]
    for i in range(len(l)):
        if (max < l[i]):
            max = l[i]
            max_i = i
    return max, max_i

def min_listy(l):
    min_i = 0
    min = l[0]
    for i in range(len(l)):
        if (min > l[i]):
            min = l[i]
            min_i = i
    return min, min_i

def max_czas(x,np,l,droga):
    czas=0
    p=[]
    for i in range(np):
        for j in range(len(l)):
            if droga[x][j]==i+1:
                czas+=l[j]
        p.append(czas)
        czas=0
    tmp=max_listy(p)[0]
    return tmp,p

def random_droga(nz,np):
    lista=[]
    tmp=1
    for i in range(nz):
        if tmp>np:
            tmp=1
        lista.append(tmp)
        tmp+=1
    random.shuffle(lista)
    return lista

def wybierz_zad(p,nz,np):
    los=random.random()
    sum=0
    for i in range(nz):
        for j in range(np):
            sum+=p[i][j]
            if los<=sum:
                return j+1
    return los

# m - liczba mrowek
# np - liczba procesorow
# l - lista zadan
# ncmax - maksymalna liczba cykli
# c - intensywnosc feromonu
# ro - wspolczynnik parowania feromonu
# alfa - wspolczynnik atrakcyjnosci sciezki
# beta - wspolczynnik widocznosci sciezki

def mrowki(m,np,l,ncmax,c,ro,alfa,beta):
    nc=0   # nc - liczba cykli
    nz=len(l) # nz - liczba zadań
    min = sum(l)
    tau=[[c]*np for _ in range(nz)]
    delta_tau=[[0]*np for _ in range(nz)]
    while(nc<ncmax):
        #print("nastepna iteracja")
        if nc!=0:
            droga=[[] for k in range(m)]
            proc=[[[] for _ in range(np)] for k in range(m)]
            p=[[0]*np for _ in range(nz)] # prawdopodobienstwo
            while(len(droga[0])<nz):
                for k in range(m):
                    for i in range(nz):
                        lp=[]
                        for j in range(np):
                            lp.append(sum(proc[k][j]))
                        if 0 not in lp:
                            for j in range(np):
                                p[i][j]=(tau[i][j]**alfa)*((min_listy(lp)[0])**beta)
                            nast_proc = max_listy(p[i])[1] + 1
                        else:
                            nast_proc=random.randint(1,np)
                            p[i][nast_proc-1]=(tau[i][nast_proc-1]**alfa)*((1/np)**beta)
                        droga[k].append(nast_proc)
                        proc[k][nast_proc-1].append(l[i])
        else:
            droga = []
            for k in range(m):
                if k == 0:
                    droga.append(zachlanny(np, l))
                else:
                    droga.append(random_droga(nz, np))
        for k in range(m):
            tmp,proc1=max_czas(k,np,l,droga)
            if tmp<min:
                min=tmp
                print("nastepny min: ",min)
            for i in range(nz):
                for j in range(np):
                    if max_listy(proc1)[0]-min_listy(proc1)[0]==0:
                        return min
                    elif droga[k][i]==j+1 and (max_listy(proc1)[0]-min_listy(proc1)[0])!=0:
                        delta_tau[i][j]+=c/(max_listy(proc1)[0]-min_listy(proc1)[0])
        for i in range(nz):
            for j in range(np):
                tau[i][j]=ro*tau[i][j]+delta_tau[i][j]
                delta_tau[i][j]=0
        nc+=1
    return min
