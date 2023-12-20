import random

def feladat2():
    veletlen_szamok=[]
    for i in range(8):
        szam=random.randint(-100,859)
        veletlen_szamok.append(str(szam))
        if i <7:
            print(szam,end=";")
        else:
            print(szam,end="")    



def tizzel_oszthatoak_szama(veletlen_szamok):
    szamlalo=0
    for i in range(0,len(veletlen_szamok),1):
        if veletlen_szamok[i] % 10==0:
            szamlalo+=1
        i+=1
    print(f"A tízzel osztható számok összege:{szamlalo}")
    return szamlalo   


    