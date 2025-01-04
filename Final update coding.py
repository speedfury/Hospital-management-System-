#print("______FORM GENERATOR_____")

#import csv

#def make():
    #field=["pat ID","name","gender","age","mob",#"adderss","disease","bloodgroup","drname","roomno"]
   # file=open("patientreg.csv","w",newline="")
   # cwriter=csv.writer(file)
   # cwriter.writerow(field)
    #list4=[]
    #while True:
     #   patientid=input("Enter patient ID").upper()
      #  pname=input("Enter patient name").upper()
      #  gender=input("Enter patient gender").upper()
      #3  age=input("enter patient age")
      #  mno=input("Enter mobile number")
    ###    address=input("Enter patient address")
       # disease=input("Enter your disease")
      #  bloodgp=input("Enter blood group").upper()
      # doctorname=input("Enter doctor name").upper()
      #  room=input("Enter room no")
     #   lisn=[patientid,pname,gender,age,mno,address,disease,bloodgp,doctorname,room]
     #   list4.append(lisn)
     #   ch=input("enter more so press.. y if not then press n")
      #  if ch=="n": 
      #     break
   # cwriter.writerows(list4)
    #file.close()
  
    
#make()
    
#import csv

#def update():
 #  file= open("patientreg.csv","r")
  # update=csv.reader(file)
  # upd=[]
  # pat_name=input("Enterpatient Name  to Update").upper()
  # found=0
  # for row in update:
  ##   if row[1]==pat_name:
   #     row[1]=input("Enter new patient name").upper()
    #    row[2]=input("Enter coorected gender").upper()
    #    row[3]=input("Enter corrected age")
    #    row[4]=input("Enter corrected mobile number")
    #    row[5]=input("Enter corrected address").upper()
       # row[6]=input("Enter corrected diesase").upper()
    #    row[7]=input("Enter corrected bloodgroup").upper()
       # row[8]=input("Enter doctor name corrected").upper()
    #  #  row[9]=input("Enter corrected room no")
      #  found=found+1
     #upd.append(row)
   #file.close()
  
   #if found==0:
   # print("data not exist or found")
   #else:
   #    file=open("patientreg.csv","w+",newline="")
      # csvwriter=csv.writer(file)
    #   csvwriter.writerows(upd)
     #  file.seek(0)
     #  update=csv.reader(file)
       #for row in update:
     ##   print(row)
      ## file.close()

#update()






import csv

def update():
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

update()