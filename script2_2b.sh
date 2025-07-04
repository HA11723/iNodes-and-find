#!/usr/bin/bash
#Student Name: Hadi Nasir
#Student Number: 100367064
#Date: Fri May 16 20:44:36 PDT 2025
#Date md5: fb9c5faf81a9cab8b661c41d01fc2729 -
#Machine-
#Host name: ip-172-31-91-141.ec2.internal
#Current Directory: /home/ec2-user/environment/assignment2
#C9 Project: CPSC 1280 HomeWork Machine
#instance-id: i-027eba3cbcba94b47
#b78afcd427434ff035db4f4022feebcf -
#117bd7aa1378351d2c57b805e8a6196c  -
#Script: script2_2b.sh
################################################################################
#Google/Internet References used:
#                               
################################################################################
# list every file writable by others, show symbolic mode, then remove o+w

# print list (path + symbolic permissions)
find q2_p2 -type f -perm -002 -printf '%p %M\n' | sort

# then remove the write bit for others
find q2_p2 -type f -perm -002 -exec chmod o-w {} \;
