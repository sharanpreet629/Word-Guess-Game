#Note making 

file_name = input("Please enter file name  :") + ".txt"
#now asking the user to write, read or append

f_mode= input("Do you want to read, write or append the file? select any one(w/r/a):")
folder = open(file_name, f_mode)

#asking for further steps:
if f_mode == "w":
    notes = int(input("How many times you want to write the notes?\n"))
    times = 1
    while times <= notes:
          folder.write(("Note {}: ".format(times)) +input("Enter your note:")+"\n")
          times+=1
    folder.close()
          
elif f_mode == "r":
    
    choice = "Note " + input("which note you want to read?") + ":"
    for line in folder:
        if choice in line:
            print(line, end=" ")
            break
    else:
        print("no note found")
 
            
    folder.close()   
    
else:


    append =  "what do you want to append? \n"+"\n"
    folder.write(input(append))
    
    folder.close()
  
