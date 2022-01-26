def SwappingFiles():
    file1 = input ("Enter The File Name " )
    
    with open(file1,'r') as a:
        data_a = a.read()

    file2 = input ("Enter The File Name " )
    
    with open(file2,'w') as a:
         a.write(data_b)

    

SwappingFiles()

