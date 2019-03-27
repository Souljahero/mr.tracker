import os
import sys
import termcolor
from termcolor import colored
os.system(" figlet Mr. Tracker ")
print (colored(" ========================= ", "green"))
print (colored(" 01. Bull-Attack ", "red"))
print (colored(" 02. BillCipher ", "red"))
print (colored(" 03. RED_HAWK ", "red"))
print (colored(" 04. ReconDog ", "red"))
print (colored(" 05. IPGeoLocation ", "red"))
print (colored(" ======================== ", "green"))
tracker = input(">>>")
if tracker == "01" or tracker == "1" :
            print(" ##### INSTALLING Bull-Attack \n ") 
            os.system(" apt update && apt upgrade ")
            os.system(" pkg install python2 ")
            os.system(" git clone https://github.com/Bhai4You/Bull-Attack ")
            os.system(" mv Bull-Attack ~")
            print (colored("\n INSTALATION complete!!! ", "green"))
            print (colored("youtube tutorial for usage \n  https://youtu.be/mnQj_Weparc ", "cyan"))
elif tracker == "02" or tracker == "2" :
            print(" ##### INSTALLING BillCipher \n")
            os.system("apt upgrade && apt update ")
            os.system(" pkg install python ")
            os.system(" git clone https://github.com/GitHackTools/BillCipher ")
            os.system(" mv BillCipher ~ ")
            print (colored(" \n ##### INSTALATION Completed!!!", "green"))
            print (colored(" youtube tutorial for usage \n https://youtu.be/Xzmjqx7YXY ", "cyan"))
elif tracker == "03" or tracker == "3" :
           print(" ##### INSTALLING RED_HAWK \n")
           os.system(" apt upgrade && apt update ")
           os.system(" pkg install php ")
           os.system(" git clone https://github.com/Tuhniushubra/RED_HAWK ")
           os.system(" mv RED_HAWK ~ ")
           print (colored(" INSTALATION Complete!! ", "green"))
           print (colored(" youtube tutorial for usage \n https://youtu.be/XoW08s6leTK ", "cyan"))
elif tracker == "04" or tracker == "4" :
           print(" ##### INSTALLING ReconDog ")
           os.system(" apt upgrade && apt update ")
           os.system(" pkg install python2 ")
           os.system(" git clone https://github.com/S0md3v/ReconDog ")
           os.system(" mv ReconDog ~ ")
           print (colored("\n INSTALATION Complete!! ", "green"))
           print (colored(" youtube tutorial for usage \n https://youtu.be/K6unovN21ao ", "cyan"))
elif tracker == "05" or tracker == "5" :
           print(" ##### INSTALLING IPGeoLocation ")
           os.system(" apt upgrade && apt update ")
           os.system(" pkg install python ")
           os.system(" git clone https://github.com/maldevel/IPGeoLocation ")
           os.system(" mv IPGeoLocation ~ ")
           print (colored(" INSTALATION Completed!! ", "green"))
           print (colored("Youtube tutorial for usage \n https://youtu.be/f_brlucTTxg ", "cyan"))
else :
            print(" Enter valid number from 1 to 5 ")

print (colored(" \n This code is created by ista id - @indian_hacker_ninja \n", "red"))
print (colored("For more tools and commands subscribe my youtube channel - https://bit.ly/2um6cLb ", "green"))
