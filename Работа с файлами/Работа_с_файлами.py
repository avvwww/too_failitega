

def sisestame_andmeid():#проверять введенные код на тип данных
    ik=""
    while type(ik)!=int:
        try:
            ik=int(input("Sisesta isikukood "))
        except:
            TypeError
    return ik #int

def len_ikoodis(ik):#кол-во символов в коде
    n=len(str(ik))
    if n==11:
        flag=True
    else:
        flag=False
    return flag

def esimene(ik):
    ik_list=list(str(ik)) #["4","2",...]
    print(ik_list)
    if ik_list[0] in ["1","2","3","4","5","6"]:
        flag=True
    else:
        flag=False
    return flag

def kontrollnumber(ik):
    ik_list=list(str(ik))
    summa=1*int(ik_list[0])+2*int(ik_list[1])+3*int(ik_list[2])+4*int(ik_list[3])+5*int(ik_list[4])+6*int(ik_list[5])+7*int(ik_list[6])+8*int(ik_list[7])+9*int(ik_list[8])+1*int(ik_list[9])
    suma=summa%11
    if summa==ik_list[10]:
        flag=True
    else:
        flag=False
    return flag

def sugu(ik):#пол человека 1,3,5-mees, 2,4,6-naine A%2=0
    ik_list=list(str(ik))
    if int(ik_list[0])%2==0:
        s="naine"
    else:
        s="mees"
    return s

def koht(ik):#место рождения
    ik_list=list(str(ik))
    k=int(ik_list[7]+ik_list[8]+ik_list[9])
    if k <=10:
        text='Kuressaare Haigla'
    elif k <=19:
        text='Tartu Ülikooli Naistekliinik, Tartumaa, Tartu'
    elif k <=220:
        text='Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla'  
    elif k <= 270:
        text='Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif k <=370:       
        text=' Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla'
    elif k <=420:       
        text='Narva Haigla'
    elif k <=470:       
        print('Pärnu Haigla')
    elif k <=490:       
        text='Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla'
    elif k <=520:       
        text='Järvamaa Haigla (Paide)'
    elif k <=570:       
        text='Rakvere, Tapa haigla'
    elif k <=600:       
        text='Valga Haigla'
    elif k <=650:       
        text='Viljandi Haigla'
    elif k ==700:
        text='Lõuna-Eesti Haigla (Võru), Põlva Haigla'
    else:
        text="Error"
    return k

def sunnipaev(ik):#ДР ik_list[1]+ik_list[2]-aasta,3,4-kuu,5,6-päev
    ik_list=list(str(ik))
    p=str(ik_list[5]+ik_list[6])
    k=str(ik_list[3]+ik_list[4])
    a=str(ik_list[1]+ik_list[2])
    su=int(str(p+k+a))
    return su

def valeik_file(ik):
    t=str(ik)
    f=open('valeik'+'.txt','a')
    f.write(t+'\n')
    f.close()

def oigeik_file(ik):
    t=str(ik)
    f=open('oigeik'+'.txt','a')
    f.write(t+'\n')
    f.close()

while True:
    ik=sisestame_andmeid()
    flag=len_ikoodis(ik)
    if flag:
        flag=esimene(ik)
        if flag:
            kon=kontrollnumber(ik)
            print(f"Kontrollnumber {kon}")
            pol=sugu(ik)
            print(f"Sugu - {pol}")
            ko=koht(ik)
            print(ko)
            sun=sunnipaev(ik)
            print(f'Sünnipäev - {sun}')
            oigeik_file(ik)
                            
        else:
            print("Esimene number on vale")
            valeik_file(ik)
    else:
        print(f"{ik}-valesti sisestatud (len)")
        valeik_file(ik)