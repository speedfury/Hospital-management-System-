print("_______-WELCOME TO HOSPITAL DATA MANAGEMENT -________")
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
               print(" New Username and password registration of username will start soon.....")
               
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
                    
            elif choice==3:
                 file= open("patientreg.csv","r")
                 update=csv.reader(file)
                 upd=[]
                 pat_name=input("Enter patient Name  to Update=").upper()
                 found=0
                 for row in update:
                   if row[1]==pat_name:
                      print("chose option for updating:--")
                      print("1.NAME\n2.gender\n4.mobile no\n5.Address\n6.Disease\n7.Blood Group\n8.Doctor Name\n9.Room No\n10.To update all data")
                      w=int(input(" Enter choice to update?="))
        
                      if w==1:
        	                  row[1]=input("Enter new patient name=").upper()
                      elif  w==2:
        	                  row[2]=input("Enter coorected gender=").upper()
                      elif w==3:
        	                  row[3]=input("Enter corrected age=")
                      elif w==4:
        	                  row[4]=input("Enter corrected mobile number=")
                      elif w==5:
                           row[5]=input("Enter corrected address=").upper()
                      elif w==6:
                           row[6]=input("Enter corrected disease=").upper()
                      elif w==7:
        	                 row[7]=input("Enter corrected bloodgroup=").upper()
                      elif w==8:
                           row[8]=input("Enter doctor name corrected=").upper()
                      elif w==9:
        	                 row[9]=input("Enter corrected room no=")
                      elif w==10:
                           row[3]=input("Enter corrected age=")
                           row[4]=input("Enter corrected mobile number=")
                           row[1]=input("correct  patient name=").upper()
                           row[2]=input("correct patient gender=").upper()
                           row[5]=input("Enter corrected address=").upper()
                           row[6]=input("Enter corrected diesase=").upper()
                           row[7]=input("Enter corrected bloodgroup=").upper()
                           row[8]=input("Enter doctor name corrected=").upper()
                           row[9]=input("Enter corrected room no=")
                      else:
        	               print("__________")
        	               print("Please Enter correct choice\nINVALID CHOICE")
        	               print("__________")
                      found=found+1
                   upd.append(row)
                   file.close()
  
                   if found==0:
                     print("data not exist or found")
                   else:
                        file=open("patientreg.csv","w+",newline="")
                        csvwriter=csv.writer(file)
                        csvwriter.writerows(upd)
                        file.seek(0)
                        update=csv.reader(file)
                        for row in update:
                         print(row)
                        file.close()

                
                     
            elif choice==4:
                file= open("check.csv","r")
                delete=csv.reader(file)
                delty=[]
                pat_name=input("Enter Patient Name whose data want to delete=").upper()
                found=0
                for row in delete:
                 if row[1]==pat_name:
                    print("chose option for deleting:--")
                    print("1.NAME\n2.gender\n4.mobile no\n5.Address\n6.Disease\n7.Blood Group\n8.Doctor Name\n9.Room No\n10.To Delete all data")
                    w=int(input(" Enter choice to Delte?="))
        
                    if w==1:
        	                del row[1]
                    elif  w==2:
        	                del row[2]
                    elif w==3:
        	                del row[3]
                    elif w==4:
        	                del row[4]
                    elif w==5:
                            del row[5]
                    elif w==6:
                            del row[6]
                    elif w==7:
        	                del row[7]
                    elif w==8:
                            del row[8]
                    elif w==9:
                         	del row[9]
                    elif w==10:
                        del row[3]
                        del row[4]
                        del row[1]
                        del row[2]
                        del row[5]
                        del row[6]
                        del row[7]
                        del row[8]
                        del row[9]
                    else:
        	            print("__________")
        	            print("Please Enter correct choice\nINVALID CHOICE")
        	            print("__________")
                    found=found+1
                 delty.append(row)
                file.close()
  
                if found==0:
                   print("")
                else:
                     file=open("check.csv","w+",newline="")
                     csvwriter=csv.writer(file)
                     csvwriter.writerows(delty)
                     file.seek(0)
                     delete=csv.reader(file)
                     for row in delete:
                         print(row)
                         file.close()

            elif choice==5:
                field=["Doctorid","Name","Gender","Age","Mobno.","Graduate college","Spectalist","Patientsleft","Patienttoattend","Roomno"]
                file=open("Doctordata.csv","w",newline="")
                cwriter=csv.writer(file)
                cwriter.writerow(field)
                list4=[]
                while True:
                  Doctorid=input("Enter Doctor ID").upper()
                  Name=input("Enter Doctor name").upper()
                  Gender=input("Enter  gender").upper()
                  Age=input("Enter Doctor age")
                  Mno=input("Enter mobile number")
                  Graduatecollege=input("Enter Graduate college")
                  Spectialist=input("Enter speciality")
                  Patientsleft=input("Enter  number of patients left").upper()
                  Patientstoattend=input("Enter number of patients to attend").upper()
                  Room=input("Enter Room no")
                  lisn=[Doctorid,Name,Gender,Age,Mno,Graduatecollege,Spectialist,Patientsleft,Patientstoattend,Room]
                  list4.append(lisn)
                  ch=input("enter more so press.. y if not then press n")
                  if ch=="n": 
                      break
                cwriter.writerows(list4)
                file.close()

            elif choice==6:
                print("QUIT FROM SYSTEM")
                print("____VISIT AGAIN")
                break
        else:
            count=count+1
            print(f"Invalid Credentials : now {3-count} attempt left")
            if count==3:
                break

main_menu()




