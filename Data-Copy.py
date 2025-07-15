import os
import shutil

#Variable assignment
Username = os.getenv("USERNAME")

###CUSTOMIZE COPY TARGET HERE###
Path = fr"C:\Users\{Username}\Videos"

###CUSTOMIZE YOUR OUTPUT DESTINATION HERE###
Output = r"N:\Output2"

line = "#" * 80

Start = input("Would You Like to Start? \n".lower)




#Function handling copy
def copy(Path, Output):
    
    print("Beginning Copy Now... \n")
    
    print("\n This may take some time, depending on the amount of data being copied.")
    
    shutil.copytree(Path, Output)   
    
    print("Transfer complete!")
    

#Introduction    
print(line,
      "\n",
      "Here is Tan's Terrific Transfer Tool".center(80, "-"),
      "\n",
      line)


#Using the Start variable to show introduction and collect user input
Start


#if-then-else to determine if the script should run
if Start == "yes":
    copy(Path, Output)
    
elif Start == "no":
    print("No process being started.")
    
else: 
    print("Please input a valid parameter")
    

