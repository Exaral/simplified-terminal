#!/usr/bin/env python3

while True:
         try:
            import os
            import subprocess
            import time
            print('Welcome to Simplified Terminal.')
            print('Choose a option')
            print('')
# Here goes the options
            print('1- Create folder')
            print('2- Install or remove program (apt)')
            print('3- Format partitions or disks')
            print('4- Heimdall')
            print('5- Run Windows programs via Wine')
            print('6- Edit or create text files (nano)')
            print('7- Enter in a folder (cd)')
            print('8- Remove files (rm)')
            print('')
            print('To leave use Ctrl + C')
            print('')
            try:
               q = int(input('Enter your answer: '))
            except ValueError:
               print("Invalid input, please enter a number.")
               continue         
# Now the things!
 # Number 1 - Create folder
            if q == 1:
               ES = int(input('Enable sudo?(1- No, 2 - Yes) '))
               fn = input("Enter your folder's name: ")
               if ES == 1:
                  subprocess.run(["mkdir", fn])
               elif ES == 2:
                  subprocess.run(["sudo", "mkdir", fn])
 # Number 2 - Install or remove program (apt)
            if q == 2:
               bq1 = int(input('Do you want to install(1) or remove(2) a program?: '))
               if bq1 == 1:
                  pn = input('Enter program name: ')
                  subprocess.run(["sudo", "apt", "install", pn])
               elif bq1 == 2:
                    pn = input('Enter program name')
                    subprocess.run(["sudo", "apt", "remove", pn])
 # Number 3 - Format partitions or disks     
            if q == 3:
               print('Warning, if is a removable media, plug it now, if is not plugged')
               input('Hit enter here when you are all done(of plugging the media if its not plugged) ')
               subprocess.run(["lsblk"])
               cq1 = input('Enter partition or disk (example /dev/sdx): ')
               cq2 = int(input('Do you want fat32(1) ext4(2) or ntfs(3)?: '))
               if cq2 == 1:
                  confirm = input(f"Are you sure you want to format {cq1}? (y/n): ")
                  if confirm.lower() == "yes":
                     subprocess.run(["sudo", "mkfs.vfat", cq1])
               if cq2 == 2:
                  confirm = input(f"Are you sure you want to format {cq1}? (y/n): ")
                  if confirm.lower() == "yes":
                     subprocess.run(["sudo", "mkfs.ext4", cq1])
               if cq2 == 3:
                  confirm = input(f"Are you sure you want to format {cq1}? (y/n): ")
                  if confirm.lower() == "yes":
                     subprocess.run(["sudo", "mkfs.ntfs", cq1])
 # Number 4 - Heimdall
            if q == 4:
               dq1 = int(input('A custom OS can cause critical problems in phone and installed applications. If you want to install a custom OS, type 1, if not, type 2, and enter it.: '))
               if dq1 == 1:
                  dq2 = input("Choose a partition to flash, (example: --BOOT) (Attention, you need to put the -- , and the partition name in caps or not. Try first with caps, if it don't work use without, and if it doesn't work again, the partition does not exists): ")
                  dq3 = input("Input file source (if is on the folder you are, just put its name, but if not, put its entire path!: ")
                  confirm = input(f"⚠️ Are you sure you want to flash {dq2} with {dq3}? (y/n): ")
                  if confirm.lower() == "y":
                     subprocess.run(["heimdall", "flash", dq2, dq3])
                  else:
                      print("Flash aborted.")
               elif dq1 == 2:
                    print('Abort')
 # Number 5 - Run Windows programs via Wine          
            if q == 5:
                eq1 = input("Input file source (if is on the folder you are, just put its name, but if not, put its entire path!: ")
                ES = int(input('Enable sudo?(1- No, 2 - Yes) '))
                if ES == 1:
                   subprocess.run(["wine", eq1])
                elif ES == 2:
                     subprocess.run(["sudo", "wine", eq1])
 # Number 6 - Edit or create text files (nano)
            if q == 6:
               fq1 = input("Input file source (if is on the folder you are, just put its name, but if not, put its entire path!(if you wanna create a text file, just type the name you want to it): ")
               ES = int(input('Enable sudo?(1- No, 2 - Yes) '))
               if ES == 1:
                  subprocess.run(["nano", fq1])
               elif ES == 2:
                    subprocess.run(["sudo", "nano", fq1])
 # Number 7 - Enter in a folder (cd)
            if q == 7:
                gq1 = input("Input folder's source (if is on the folder you are, just put its name, but if not, put its entire path!: ")
                os.chdir(gq1)

 # Number 8 - Remove files (rm)
            if q == 8:
                hq1 = input("Input file's source (if is on the folder you are, just put its name, but if not, put its entire path!: ")
                ES = int(input('Enable sudo?(1- No, 2 - Yes) '))
                EF = int(input('Enable forced?(1- No, 2 - Yes) '))
                if ES == 1:
                   if EF == 1:
                      subprocess.run(["rm", hq1])
                if ES == 1:
                   if EF == 2:
                      subprocess.run(["rm", "-rf", hq1])
                if ES == 2:
                   if EF == 1:
                      confirm = input(f"⚠️ Are you sure you want to delete {hq1} with sudo? (y/n): ")
                      if confirm.lower() == "yes":
                         subprocess.run(["sudo", "rm", hq1])
                if ES == 2:
                   if EF == 2:
                      confirm = input(f"⚠️ Are you sure you want to delete {hq1} with sudo? (y/n): ")
                      if confirm.lower() == "yes":
                         subprocess.run(["sudo", "rm", "-rf", hq1])
         # Now the exit part
            abcd = int(input('Do you want to exit, or run another command? (1.Exit/2.Run another command): '))
            if abcd == 1:
               break
            if abcd == 2:
                subprocess.run(["clear"])
         
# Ctrl + C part
         except KeyboardInterrupt:
                print('')
                print('Do you really want to exit?')
                print('')
                print('1- No')
                print('2- Yes')
                YN = int(input('Your answer: '))
                if YN == 1:
          	       print('Restarting…')
          	       time.sleep(0.5)
          	       subprocess.run(["clear"])
                if YN == 2:
                   print()
                   print('Goodbye!')
                   time.sleep(0.3)
                   subprocess.run(["clear"])
                   break
