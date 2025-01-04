print("_______-WELCOME TO HOSPITAL SYSTEM-________")
import csv
def login():
  user=input("Enter username=  ").upper()
  pwd=input("Enter password= ").upper()
  

  
  file=open("projecte.csv", "r")
  csvwriter=csv.reader(file)
 
  l=csvwriter
  next(l)
    
  for row in l:
    if (row[0]==user and row[1]==pwd):
    
      return 1
      
  else:
   return 0


def main_menu():
    count=0
    while True:
        if login()==1:
            print("____________________welcome_________")
            print("login sucessfully")
            print("_____________get ready for further process__________.")
            print("1.USERNAME AND PASSWORD REGISTRATION")
            print("2.patient registration")
            print("3.update patient data")
            print("4.DELTE PATIENT DATA")
            print("5.doctor data")
            print("6.QUIT")
           
            choice=int(input("Enter choice : "))
            
            if choice==1:
               print(" New Username and registration of username will start soon.....")
               
               file=open("projecte.csv","a",newline="")
               lis4=[]
               while True:
                 user2=input("Enter new Username=").upper()
                 pwd2=input(" Enter new password").upper()
                 csvwriter=csv.writer(file)
                 lst=[user2,pwd2]
                 lis4.append(lst)
                 ch=input("enter more so press.. y if not then press n")
                 if ch=="n": 
                     break
               for i in lis4:  
                  csvwriter.writerow(i)
                  print("____DATA WRITTEN SUCCESSFULLY!!!____")
               file.close()

               break
            elif choice==2:
                      
               break
        else:
            count=count+1
            print(f"Invalid Credentials : now {3-count} attempt left")
            if count==3:
                break

main_menu()