#os module interaction with your operating system
#navigating direction
import os
print(os.name)
if os.name=='nt':
    command='dir'
    print(command)
else:
    command='ls-l'
    print(command)

os.system(command)
#command is run via the operationg system's standard shell,and
#return the shell's exit status


#in command prompt if we want to cursor on the beggining
#import os
#os.system('cls')#it return 0 and put the cursor in begginig on cmd and python shell on 0 output ayega
