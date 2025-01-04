
#import csv
#def login():
 # user=input("Enter username=  ").upper()
  #pwd=input("Enter password= ").upper()
  

  
  #file=open("projecte.csv", "r")
  #csvwriter=csv.reader(file)
 
 # l=csvwriter
 # next(l)
    
  #for row in l:
   # if (row[0]==user and row[1]==pwd):
    
   #   return 1
      
  #else:
  # return 0


#def main_menu():
    #count=0
    #while True:
       # if login()==1:
       #     print("____________________welcome_________")
         #   print("login sucessfully")
         #   print("_____________get ready for further process__________.")
         ##   print("1.REGISTRATION")
          #  print("2.QUIT")
           
          #  choice=int(input("Enter choice : "))
            
         #   if choice==1:
           #    print(" New  registration of username will start soon.....")
               
           #    file=open("projecte.csv","a",newline="")
            #   lis4=[]
           #    while True:
            #     user2=input("Enter new Username=").upper()
           #      pwd2=input(" Enter new password").upper()
             #    csvwriter=csv.writer(file)
              #   lst=[user2,pwd2]
             #    lis4.append(lst)
             #    ch=input("enter more so press.. y if not then press n")
              #   if ch=="n": 
               #      break
              # for i in lis4:  
                  #csvwriter.writerow(i)
                  #print("____DATA WRITTEN SUCCESSFULLY!!!____")
              # file.close()

              # break
           # elif choice==2:
             #  print("Thanks ")         
            #   break
        #else:
         #   count=count+1
           # print(f"Invalid Credentials : now {3-count} attempt left")
           # if count==3:
          #      break






#import csv

#def make():
  
  #patientid=input("enter patient ID")
  #pname=input("enter patient name")
  #gender=input("enter patient gender")
  #age=input("enter patient age")
 # mno=input("enter mobile number")
 # address=input("enter patient address")
  #disease=input("enter your disease")
  #bloodgp=input("enter blood group")
  #doctorname=input("enter doctor name")
  #room=input("enter room no")
  #list6=[patientid,pname,gender,age,mno,address,disease,bloodgp,doctorname,room]
  #choice=input("enter choice")
  #if choice=="n":
   # filen=open("patientregistration.csv","w",newline="")
  #l=csv.writer(filen)
 #for i in list6:
  #  next(l)
  #  l.writerows(i)

  #filen.close()
#make()


#print("______FORM GENERATOR_____")

import csv

def make():
    field=["pat ID","name","gender","age","mob","adderss","disease","bloodgroup","drname","roomno"]
    file=open("patientreg.csv","w",newline="")
    cwriter=csv.writer(file)
    cwriter.writerow(field)
    list4=[]
    while True:
        patientid=input("Enter patient ID").upper()
        pname=input("Enter patient name").upper()
        gender=input("Enter patient gender").upper()
        age=input("enter patient age")
        mno=input("Enter mobile number")
        address=input("Enter patient address")
        disease=input("Enter your disease")
        bloodgp=input("Enter blood group").upper()
        doctorname=input("Enter doctor name").upper()
        room=input("Enter room no")
        lisn=[patientid,pname,gender,age,mno,address,disease,bloodgp,doctorname,room]
        list4.append(lisn)
        ch=input("enter more so press.. y if not then press n")
        if ch=="n": 
            break
    cwriter.writerows(list4)
    file.close()
  
    
make()
    






  
        