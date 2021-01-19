def loe_failist(file):
    f=open(file,'r')
    list_n=[]
    for line in f:
        list_n.append(line.strip())
    f.close()
    return list_n

def salvesta_failisse():

   text=input("Sisesta tekts failisse lisamiseks")
   file=input("Faili nimetus...")
   f=open(file+'.txt','a') #дозапись
   f.write(text+'\n')
   f.close()


list_n=loe_failist(r"Nimed.txt")
print(list_n)

salvesta_failisse()