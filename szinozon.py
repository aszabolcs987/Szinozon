import random
tabla=[]
szinek=["piros", "sárga", "kék", "zöld", "fehér", "fekete"]
def jatek(tabla, szinek):
        i=1
        while i<=4:
            szin=random.choice(szinek)
            tabla.append(szin)
            i+=1
        lehetoseg=0
        eredmeny=False
        print()
        print("="*40)
        print("SZÍNÖZÖN")
        print("A játékban ki kell tálnod melyik 4 színre gondoltam, de csak 3 esélyed van!")
        print("A lehetséges színek: ", ", ".join(szinek))
        print("="*40)
        while lehetoseg<3:
            a=input("Első szín? ")
            db=0
            for x in szinek:
                if x==a:
                    db+=1
            if db==0:
                print("Nem megfelelő! Kérlek a fenti színekből válassz! :)")
                print("-"*40)
                print()
                a=input("Első szín? ")
                
            b=input("Második szín? ")
            db=0
            for x in szinek:
                if x==b:
                    db+=1
            if db==0:
                print("Nem megfelelő! Kérlek a fenti színekből válassz! :)")
                print("-"*40)
                print()
                b=input("Második szín? ")
                
            c=input("Harmadik szín? ")
            db=0
            for x in szinek:
                if x==c:
                    db+=1
            if db==0:
                print("Nem megfelelő! Kérlek a fenti színekből válassz! :)")
                print("-"*40)
                print()
                c=input("Harmadik szín? ")
                
            d=input("Negyedik szín? ")
            db=0
            for x in szinek:
                if x==d:
                    db+=1
            if db==0:
                print("Nem megfelelő! Kérlek a fenti színekből válassz! :)")
                print("-"*40)
                print()
                d=input("Negyedik szín? ")
            if a==tabla[0] and b==tabla[1] and c==tabla[2] and d==tabla[3]:
                print("="*40)
                print("Eltaláltad! :)")
                eredmeny=True
                lehetoseg+=4         
            elif a==tabla[0] or b==tabla[1] or c==tabla[2] or d==tabla[3]:
                print("="*40)
                if a==tabla[0]:
                    print("Első:✓")
                if a!=tabla[0] and a==tabla[1] or a==tabla[2] or a==tabla[3]:
                    print("Az első szín nem jó helyen van!")
                elif a!=tabla[0]:
                    print("Első: X")
                    
                if b==tabla[1]:
                    print("Második:✓ ")
                if b!=tabla[1] and b==tabla[0] or b==tabla[2] or b==tabla[3]:
                    print("A második szín nem jó helyen van!")
                elif b!=tabla[1]:
                    print("Második: X")
                    
                if c==tabla[2]:
                    print("Harmadik: ✓")
                if c!=tabla[2] and c==tabla[0] or c==tabla[1] or c==tabla[3]:
                    print("A harmadik szín nem jó helyen van!")
                elif c!=tabla[2]:
                    print("Harmadik: X")
                    
                if d==tabla[3]:
                    print("Negyedik: ✓")
                if d!=tabla[3] and d==tabla[0] or d==tabla[1] or d==tabla[2]:
                    print("A negyedik szín nem jó helyen van!")
                elif d!=tabla[3]:
                    print("Negyedik: X")
                lehetoseg+=1
                eredmeny=False
                print("="*40)
                if lehetoseg<3:
                    print("Csak", 3-lehetoseg, "lehetőséged maradt! :(")
                    print("Próbáld újra! :)")
                if lehetoseg==3:
                    print("="*40)
                    print("Sajnos vesztettél! :(")
                print("="*40)
            elif a!=tabla[0] and b!=tabla[1] and c!=tabla[2] and d!=tabla[3]:
                print("="*40)
                if a!=tabla[0] and a==tabla[1] or a==tabla[2] or a==tabla[3]:
                    print("Az első szín nem jó helyen van!")
                elif a!=tabla[0]:
                    print("Első: X")
                    
                if b!=tabla[1] and b==tabla[0] or b==tabla[2] or b==tabla[3]:
                    print("A második szín nem jó helyen van!")
                elif b!=tabla[1]:
                    print("Második: X")
                
                if c!=tabla[2] and c==tabla[0] or c==tabla[1] or c==tabla[3]:
                    print("A harmadik szín nem jó helyen van!")
                elif c!=tabla[2]:
                    print("Harmadik: X")
                    
                if d!=tabla[3] and d==tabla[0] or d==tabla[1] or d==tabla[2]:
                    print("A negyedik szín nem jó helyen van!")
                elif d!=tabla[3]:
                    print("Negyedik: X")
                
                lehetoseg+=1
                eredmeny=False
                if lehetoseg<3:
                    print("="*40)
                    print("Csak", 3-lehetoseg, "lehetőséged maradt! :(")
                    print("Próbáld újra! :)")
                if lehetoseg==3:
                    print("="*40)
                    print("Sajnos vesztettél! :(")
                print("="*40)
        print("A megoldás: ", ", ".join(tabla))
        print("="*40)
        print()
jatek(tabla, szinek)
c=input("Szeretnél újra játszani? :) igen/nem    ")
print()
if c!="igen" and c!="nem":
    print("igen-nel vagy nem-el válaszolj! -_-    ")
    print()
    while c!="igen" and c!="nem":
        c=input("Szeretnél újra játszani? :) igen/nem    ")
if c=="igen":
    jatek(tabla, szinek)
app.run()