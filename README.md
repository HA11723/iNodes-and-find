# iNodes-and-find

Part 1: File System
The following is a listing of the A2 directory using the "ls -R -i -l A2" command.  Write a shell script called script2_1.sh that recreates the directory structure described by listing listing below.  Your iNodes numbers will not be the same, however the permissions and links needs to match. The contents of the files does not matter, so they can be empty or have other content.

To keep your work organize, please work in the Cloud 9 environment, in a subdirectory called assignment2.  

A2:
total 0
19889988 drwx------.  6 ec2-user ec2-user  74 Mar 18 17:49 KlingonImperiaFleet
13838060 drwx------. 10 ec2-user ec2-user 139 Mar 18 17:49 Romulan Imperial Star Navy
 5673805 drwx------.  9 ec2-user ec2-user 117 Mar 18 17:49 StarFleet

A2/KlingonImperiaFleet:
total 0
 5675476 drwx------. 2 ec2-user ec2-user 63 Mar 18 17:49 Bird Of Prey
 5675475 dr-x------. 2 ec2-user ec2-user 45 Mar 18 17:49 D5 Cruiser
19889989 drwx------. 2 ec2-user ec2-user 38 Mar 18 17:49 K't'inga
13838059 drwx------. 2 ec2-user ec2-user 57 Mar 18 17:49 Raptor

A2/KlingonImperiaFleet/Bird Of Prey:
total 16
5675492 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 chipoza
5675485 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 gazlight
5675491 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 navi
5675484 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 puppet

A2/KlingonImperiaFleet/D5 Cruiser:
total 12
5675483 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 beta1
5675505 -rw-------. 2 ec2-user ec2-user 12 Mar 18 17:49 beta2
5675505 -rw-------. 2 ec2-user ec2-user 12 Mar 18 17:49 beta3

A2/KlingonImperiaFleet/K't'inga:
total 8
 5675504 -r--------. 3 ec2-user ec2-user 12 Mar 18 17:49 nova.txt
19889997 -r--------. 1 ec2-user ec2-user 12 Mar 18 17:49 seno.txt

A2/KlingonImperiaFleet/Raptor:
total 12
19890001 -r--------. 4 ec2-user ec2-user 12 Mar 18 17:49 check.txt
13838068 -r--------. 1 ec2-user ec2-user 12 Mar 18 17:49 flight.txt
13838069 -r--------. 1 ec2-user ec2-user 12 Mar 18 17:49 swim.txt

A2/Romulan Imperial Star Navy:
total 0
19889993 drwx------. 2 ec2-user ec2-user 16 Mar 18 17:49 Bird Of Prey
 5675479 drwx------. 2 ec2-user ec2-user 16 Mar 18 17:49 Bird Of Prey$(Early)
19889991 dr-x------. 2 ec2-user ec2-user 26 Mar 18 17:49 D'deridex
 5675478 dr-x------. 2 ec2-user ec2-user 41 Mar 18 17:49 D7
13838062 dr--------. 2 ec2-user ec2-user  6 Mar 18 17:49 D8
19889990 drwx------. 2 ec2-user ec2-user 21 Mar 18 17:49 Gasko
13838061 drwx------. 2 ec2-user ec2-user 18 Mar 18 17:49 Ship Type 1
 5675477 drwx------. 2 ec2-user ec2-user 20 Mar 18 17:49 Valadore

A2/Romulan Imperial Star Navy/Bird Of Prey:
total 4
19890000 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 nn

A2/Romulan Imperial Star Navy/Bird Of Prey$(Early):
total 4
5675503 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 oh

A2/Romulan Imperial Star Navy/D'deridex:
total 4
19889999 -r--------. 1 ec2-user ec2-user 12 Mar 18 17:49 $op runn.txt

A2/Romulan Imperial Star Navy/D7:
total 12
5675504 -r--------. 3 ec2-user ec2-user 12 Mar 18 17:49 Run
5675499 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 Rune
5675502 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 Runo

A2/Romulan Imperial Star Navy/D8:
total 0

A2/Romulan Imperial Star Navy/Gasko:
total 4
19889998 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 unknown

A2/Romulan Imperial Star Navy/Ship Type 1:
total 4
13838070 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 niky

A2/Romulan Imperial Star Navy/Valadore:
total 4
5675498 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 reverv

A2/StarFleet:
total 0
13838058 dr-x------. 2 ec2-user ec2-user 54 Mar 18 17:49 Defiant
13838056 dr-x------. 4 ec2-user ec2-user 88 Mar 18 17:49 Discovery
13838047 drwx------. 4 ec2-user ec2-user 43 Mar 18 17:49 Enterprise
19889987 drwx------. 2 ec2-user ec2-user  6 Mar 18 17:49 Excelsior
 5675474 drwx------. 2 ec2-user ec2-user  6 Mar 18 17:49 Hurd
13838057 drwx------. 2 ec2-user ec2-user  6 Mar 18 17:49 Stargazer
13838055 drwx------. 4 ec2-user ec2-user 30 Mar 18 17:49 Voyager

A2/StarFleet/Defiant:
total 12
13838066 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 defeats
13838067 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 upgrades
13838065 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 victories

A2/StarFleet/Discovery:
total 12
 5675472 drwx------. 2 ec2-user ec2-user 52 Mar 18 17:49 Conventional
19889986 drwx------. 2 ec2-user ec2-user 52 Mar 18 17:49 mushroom
13838063 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 problems
19890001 -r--------. 4 ec2-user ec2-user 12 Mar 18 17:49 trips
13838064 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 violation

A2/StarFleet/Discovery/Conventional:
total 12
 5675481 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 problems
19890001 -r--------. 4 ec2-user ec2-user 12 Mar 18 17:49 trips
 5675482 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 violation

A2/StarFleet/Discovery/mushroom:
total 12
19890001 -r--------. 4 ec2-user ec2-user 12 Mar 18 17:49 problems
19889995 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 trips
19889996 -rwx------. 1 ec2-user ec2-user 12 Mar 18 17:49 violation

A2/StarFleet/Enterprise:
total 0
19889984 drwx------. 2 ec2-user ec2-user 21 Mar 18 17:49 Constitution
 5675470 drwx------. 2 ec2-user ec2-user 22 Mar 18 17:49 Soveriegn

A2/StarFleet/Enterprise/Constitution:
total 4
19889994 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 USS1701

A2/StarFleet/Enterprise/Soveriegn:
total 4
5675480 -rw-------. 1 ec2-user ec2-user 12 Mar 18 17:49 USS1701E

A2/StarFleet/Excelsior:
total 0

A2/StarFleet/Hurd:
total 0

A2/StarFleet/Stargazer:
total 0

A2/StarFleet/Voyager:
total 0
19889985 drwx------. 2 ec2-user ec2-user  6 Mar 18 17:49 2057
 5675471 drwx------. 2 ec2-user ec2-user 23 Mar 18 17:49 2267

A2/StarFleet/Voyager/2057:
total 0

A2/StarFleet/Voyager/2267:
total 4
5675504 -r--------. 3 ec2-user ec2-user 12 Mar 18 17:49 delta.txt



Part 2: find command
References:

find command: https://man7.org/linux/man-pages/man1/find.1.html

For this part of the assignment, you can use the provided part2_prep.sh script to create directories that you can test your commands on.

Part a

In a script called script2_2a.sh, please write a find command to find all files and not directories that starts with "o" and ends with "t" q2_p2 directory.  For the provided example you should get the output

q2_p2/location1/ommeuf.txt
q2_p2/location1/ommeui.txt
q2_p2/location1/oooome.txt
Part b

In a script called script2_2b.sh,  please a write a find command to find all files that have write permission for others. Print the list of files and their current permissions to stdout and remove the write permission from the files. (Hint: the ----printf option may be useful)

You output for the above test directory should list the following files:

q2_p2/location1/oooo.mi -rw-r---w-
q2_p2/location2/orchard/zello/noether.ditto -rw-r---w-
part c
In a script called script2_2c.sh, starting with the q2_p2 directory, find all the files inside directories that contain the letter "z". Print the files to stdout

For the above test directory your output may be:

q2_p2/location1/zebra/zero.tmef
q2_p2/location1/zebra/zero
q2_p2/location1/zebra/zero.txt
q2_p2/location1/zany/topaz.txt
q2_p2/location2/orchard/zello/noether.ditto
