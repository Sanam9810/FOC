def write_file(lap):
    lap_dictionary=lap
    file = open("laptops.txt","w")
    for values in lap_dictionary.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()
    
