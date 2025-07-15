import shutil, os

#variable for intro format
line = "#" * 80

switch = 0

#Introduction
print(line,
      "\n",
      "Here is Tan's Terrific Transfer Tool".center(80, "-"),
      "\n",
      line,
      "\n")


#Function to handle the copy
def copy(Path, Output):    
    
    print("Beginning Copy Now... \n")
    
    print("\n This may take some time, depending on the amount of data being copied.")
    
    shutil.copytree(Path, Output)   
    
    print("Transfer complete!")


Start = input("Would you like to copy something?(yes or no) \n").lower()

if Start == "yes":
    switch += 1

elif Start == "no":
    print("No process being executed, closing program now.")

else:
    print("Input not understood, please answer in yes or no.")



if switch == 1:
    #Path variables
    Path = input("Please enter the path of your copy target. \n")
    Output = input("Please enter the path of where you would like the target stored. \n")
    
    print(rf"Beginning copy now, from {Path} - to {Output} ")
    
    copy(Path, Output)
    
