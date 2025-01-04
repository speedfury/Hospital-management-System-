import csv
def doc():
    field=["Doctorid","Name","Gender","Age","Mobno.","Graduate college","Spectalist","Roomno"]
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
        Room=input("Enter Room no")
        lisn=[Doctorid,Name,Gender,Age,Mno,Graduatecollege,Spectialist,Room]
        list4.append(lisn)
        ch=input("enter more so press.. y if not then press n")
        if ch=="n": 
            break
    cwriter.writerows(list4)
    file.close()
  
    
doc()
    