import os
import random as r

def files():
    f=open("D:/Project.txt","a")
    while True:
        n=[]
        na=input("Enter Paragraph You Want to Write : ")
        n.append(na)
        f.writelines(n)
        fn=input("Do you want to continue (Y/N): ")
        if fn=='n' or fn=='N':
            break
    f.close()

def show():
    f=open("D:/Project.txt","r")
    data=f.read()
    print(data)
    f.close()

def search():
    while True:
        print(chr(29)*80)
        print(chr(16),"PRESS 1: Search by Words ")
        print(chr(16),"PRESS 2: Search by Character ")
        print(chr(16),"PRESS 3: Search by Number ")
        print(chr(16),"PRESS 4: Return to MAIN MENU ")
        print(chr(29)*80)
        cd=int(input("Enter Your Choice "))

        if cd==1:
            ce=input("Enter Word you want to search ")
            f=open("D:/Project.txt","r")
            data=f.read()
            words=data.split()
            f=0
            for word in words:
                if(word==ce):
                    print(word,)
                    f=1
            if f==0:
                print("Not Found ")

        elif cd==2:
            de=input("Enter Word you want to search ")
            f=open("D:/Project.txt","r")
            data=f.read()
            f=0
            for i in data:
                if(i==de):
                    print(i)
                    f=1
            if f==0:
                print("Not Found ")

        elif cd==3:
            ns=input("Enter Number you want to search: ")
            f1=0
            with open("D:/Project.txt", "r") as f:
                for line in f:
                    for i in line:
                        if i.isdigit() and i==ns:
                            print(i)
                            f1=1
            if f1==0:
                print("Not Found ",ns)

        elif cd==4:
            print("Back to Main Menu ")
            break
        else:
            print("Wrong Choice ")
    
def update():
    fn=input("Enter What you want to update ")
    with open("D:/Project.txt","r") as f:
        data=f.read()
        words=data.split()
        flag=0
    for i in range(len(words)):
        if words[i]==fn:
            mk=input("Enter the data you want to update ")
            words[i]=mk
            flag=1
    if flag==1:
        with open("D:/Project.txt","w") as t:
            for word in words:
                t.write(word+" ")
        print(" Data Updated ")
    else:
        print("No data found ")

def remove():
    dd=input("Enter the data you want to delete: ")
    lk=[]
    with open('D:/Project.txt', 'r') as file:
        for line in file:
            if dd not in line:
                lk.append(line)
        print("Data Deleted ")

    with open('D:/Project.txt', 'w') as file:
        file.writelines(lk)

def counter():
    while True:
        print(chr(31)*80)
        print(chr(16),"PRESS 1 >> No. of Alphabet ")
        print(chr(16),"PRESS 2 >> No. of Special  ")
        print(chr(16),"PRESS 3 >> No. of Uppercase  ")
        print(chr(16),"PRESS 4 >> No. of Lowercase  ")
        print(chr(16),"PRESS 5 >> No. of Digit ")
        print(chr(16),"PRESS 6 >> No. of Words ")
        print(chr(16),"PRESS 7 >> No. of Spaces ")
        print(chr(16),"PRESS 8 >> No. of Lines ")
        print(chr(16),"PRESS 9 >> Exit ")
        print(chr(30)*80)
        ab=int(input("Enter your choice...."))

        if ab==1:
            f=open("D:/Project.txt","r")
            k=0
            data=f.read()
            for i in data:
                if(i.isalpha()):
                    k=k+1
            print("No. of Alphabet ",k)
            f.close()

        elif ab==2:
            f=open("D:/Project.txt","r")
            k=0
            data=f.read()
            for i in data:
                if(i.isalnum()):
                    k=k+1
            print("No. of Special Character ",k)
            f.close()

        elif ab==3:
            f=open("D:/Project.txt","r")
            k=0
            data=f.read()
            for i in data:
                if(i.isupper()):
                    k=k+1
            print("No. of Uppercase ",k)
            f.close()

        elif ab==4:
            f=open("D:/Project.txt","r")
            k=0
            data=f.read()
            for i in data:
                if(i.islower()):
                    k=k+1
            print("No. of Lowercase ",k)
            f.close()

        elif ab==5:
            f=open("D:/Project.txt","r")
            k=0
            data=f.read()
            for i in data:
                if(i.isdigit()):
                    k=k+1
            print("No. of Digit ",k)
            f.close()

        elif ab==6:
            f=open("D:/Project.txt","r")
            k=0
            data=f.read()
            word=data.split()
            for i in word:
                if(i.isalpha()):
                    k=k+1
            print("No. of Words ",k)
            f.close()

        elif ab==7:
            f=open("D:/Project.txt","r")
            k=0
            data=f.read()
            word=data.split()
            for i in data:
                if(i==' '):
                    k=k+1
            print("No. of Spaces ",k)
            f.close()

        elif ab==8:
            f=open("D:/Project.txt","r")
            data=f.readlines()
            linecount=len(data)
            print(linecount,"Total lines ")
            f.close()

        elif ab==9:
            print("Return to Main Menu ")
            break

def random():
    while True:
        print(chr(15)*80)
        print(chr(16),"PRESS 1: Random Character ")
        print(chr(16),"PRESS 2: Random Word ")
        print(chr(16),"PRESS 3: Random Line ")
        print(chr(16),"PRESS 4: RETURN TO MAIN MENU ")
        print(chr(15)*80)
        cd=int(input("Enter Your Choice "))

        if cd==1:
            f=open("D:/Project.txt","r")
            data=f.read()
            x=r.randint(0,len(data)-1)
            print(data[x])
            f.close()

        if cd==2:
            f=open("D:/Project.txt","r")
            data=f.read()
            x=r.randint(0,len(data))
            print(data[x])
            f.close()

        if cd==3:
            f=open("D:/Project.txt","r")
            data=f.readlines()
            x=r.randint(0,len(data)-1)
            print(data[x])
            f.close()

        if cd==4:
            break

while True:
    print(chr(22)*80)
    print(' ' * 20, '|  | |~~| |~| |~\ |~| |~| |~\ ')
    print(' ' * 20, '|/\| |__| |~\ |_/ |~  |~| |_/ ')
    print(chr(22) * 80)
    print(chr(16),"PRESS 1 : Add New File ")
    print(chr(16),"PRESS 2 : Display all Text ")
    print(chr(16),"PRESS 3 : Search any Data")
    print(chr(16),"PRESS 4 : Delete any Data")
    print(chr(16),"PRESS 5 : Update any Data")
    print(chr(16),"PRESS 6 : Count Data")
    print(chr(16),"PRESS 7 : Random Switch ")
    print(chr(16),"PRESS 8 : Exit")
    print(chr(22)*80)
    ab=int(input("Enter your choice >>>>> "))

    if ab==1:
        files()
    elif ab==2:
        show()
    elif ab==3:
        search()
    elif ab==4:
        remove()
    elif ab==5:
        update()
    elif ab==6:
        counter()
    elif ab==7:
        random()
    elif ab==8:
        print("Thank you ! Visit Again")
        break
    else:
        print('Please Check The Number')
            
            
    
    
    
    
    
