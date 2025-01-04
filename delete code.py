import csv

def delete():
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
    print("data not exist or found")
   else:
       file=open("check.csv","w+",newline="")
       csvwriter=csv.writer(file)
       csvwriter.writerows(delty)
       file.seek(0)
       delete=csv.reader(file)
       for row in delete:
        print(row)
       file.close()

delete()