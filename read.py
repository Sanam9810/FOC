def read_file():
    file= open("laptops.txt","r")
    laptop_dictionaryy={}
    laptop_id= 1
    for line in file:
        line=line.replace("\n","")
        laptop_dictionaryy[laptop_id]=line.split(",")
        laptop_id+=1
    file.close()
    return laptop_dictionaryy
