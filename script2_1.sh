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
#Script: script2_1.sh
################################################################################
#Google/Internet References used:
#                               
################################################################################
        # 1  she-bang

# create root directory
#!/usr/bin/bash
# -----------------------------------------------
#  CPSC 1280  –  Assignment 2  (Hadi Nasir)
# -----------------------------------------------


mkdir -p A2
chmod 700 A2

mkdir -p "A2/KlingonImperiaFleet" \
         "A2/Romulan Imperial Star Navy" \
         "A2/StarFleet"
         
chmod 700 "A2/KlingonImperiaFleet" "A2/Romulan Imperial Star Navy" "A2/StarFleet"

#  KlingonImperiaFleet
mkdir -p "A2/KlingonImperiaFleet/Bird Of Prey" \
         "A2/KlingonImperiaFleet/D5 Cruiser" \
         "A2/KlingonImperiaFleet/K't'inga" \
         "A2/KlingonImperiaFleet/Raptor"

chmod 700 "A2/KlingonImperiaFleet/Bird Of Prey" \
          "A2/KlingonImperiaFleet/K't'inga" \
          "A2/KlingonImperiaFleet/Raptor"

chmod 500 "A2/KlingonImperiaFleet/D5 Cruiser"

# Bird Of Prey files
touch "A2/KlingonImperiaFleet/Bird Of Prey/chipoza" \
      "A2/KlingonImperiaFleet/Bird Of Prey/gazlight" \
      "A2/KlingonImperiaFleet/Bird Of Prey/navi" \
      "A2/KlingonImperiaFleet/Bird Of Prey/puppet"

chmod 700 "A2/KlingonImperiaFleet/Bird Of Prey/chipoza" \
          "A2/KlingonImperiaFleet/Bird Of Prey/gazlight" \
          "A2/KlingonImperiaFleet/Bird Of Prey/navi"

chmod 600 "A2/KlingonImperiaFleet/Bird Of Prey/puppet"

# D5 Cruiser  beta files 

chmod u+w "A2/KlingonImperiaFleet/D5 Cruiser"

touch "A2/KlingonImperiaFleet/D5 Cruiser/beta1"

touch "A2/KlingonImperiaFleet/D5 Cruiser/beta2"

ln  "A2/KlingonImperiaFleet/D5 Cruiser/beta2" \
    "A2/KlingonImperiaFleet/D5 Cruiser/beta3" || true

chmod 600 "A2/KlingonImperiaFleet/D5 Cruiser/beta1" \
          "A2/KlingonImperiaFleet/D5 Cruiser/beta2" \
          "A2/KlingonImperiaFleet/D5 Cruiser/beta3"
chmod 500 "A2/KlingonImperiaFleet/D5 Cruiser"

# K't'inga files
touch "A2/KlingonImperiaFleet/K't'inga/nova.txt" \
      "A2/KlingonImperiaFleet/K't'inga/seno.txt"

chmod 400 "A2/KlingonImperiaFleet/K't'inga/nova.txt" \
          "A2/KlingonImperiaFleet/K't'inga/seno.txt"

# Raptor files
touch "A2/KlingonImperiaFleet/Raptor/check.txt" \
      "A2/KlingonImperiaFleet/Raptor/flight.txt" \
      "A2/KlingonImperiaFleet/Raptor/swim.txt"

chmod 400 "A2/KlingonImperiaFleet/Raptor/"*.txt

#  Romulan Imperial Star Navy
mkdir -p "A2/Romulan Imperial Star Navy/Bird Of Prey" \
         "A2/Romulan Imperial Star Navy/Bird Of Prey\$(Early)" \
         "A2/Romulan Imperial Star Navy/D'deridex" \
         "A2/Romulan Imperial Star Navy/D7" \
         "A2/Romulan Imperial Star Navy/D8" \
         "A2/Romulan Imperial Star Navy/Gasko" \
         "A2/Romulan Imperial Star Navy/Ship Type 1" \
         "A2/Romulan Imperial Star Navy/Valadore"

chmod 700 "A2/Romulan Imperial Star Navy/Bird Of Prey" \
          "A2/Romulan Imperial Star Navy/Bird Of Prey\$(Early)" \
          "A2/Romulan Imperial Star Navy/Gasko" \
          "A2/Romulan Imperial Star Navy/Ship Type 1" \
          "A2/Romulan Imperial Star Navy/Valadore"

chmod 500 "A2/Romulan Imperial Star Navy/D'deridex" \
          "A2/Romulan Imperial Star Navy/D7"

chmod 400 "A2/Romulan Imperial Star Navy/D8"

# Bird-of-Prey files
touch "A2/Romulan Imperial Star Navy/Bird Of Prey/nn"

touch "A2/Romulan Imperial Star Navy/Bird Of Prey\$(Early)/oh"

chmod 600 "A2/Romulan Imperial Star Navy/Bird Of Prey/nn" \
          "A2/Romulan Imperial Star Navy/Bird Of Prey\$(Early)/oh"

# D'deridex file

chmod u+w "A2/Romulan Imperial Star Navy/D'deridex"

touch "A2/Romulan Imperial Star Navy/D'deridex/\$op runn.txt"

chmod 400 "A2/Romulan Imperial Star Navy/D'deridex/\$op runn.txt"

chmod 500 "A2/Romulan Imperial Star Navy/D'deridex"

# D7 files

chmod u+w "A2/Romulan Imperial Star Navy/D7"

ln  "A2/KlingonImperiaFleet/K't'inga/nova.txt" \
    "A2/Romulan Imperial Star Navy/D7/Run" || true

touch "A2/Romulan Imperial Star Navy/D7/Rune" \
      "A2/Romulan Imperial Star Navy/D7/Runo"

chmod 400 "A2/Romulan Imperial Star Navy/D7/Run"

chmod 600 "A2/Romulan Imperial Star Navy/D7/Rune" \
          "A2/Romulan Imperial Star Navy/D7/Runo"

chmod 500 "A2/Romulan Imperial Star Navy/D7"

# Remaining Romulan files

touch "A2/Romulan Imperial Star Navy/Gasko/unknown"

chmod 600 "A2/Romulan Imperial Star Navy/Gasko/unknown"

touch "A2/Romulan Imperial Star Navy/Ship Type 1/niky"

chmod 700 "A2/Romulan Imperial Star Navy/Ship Type 1/niky"

touch "A2/Romulan Imperial Star Navy/Valadore/reverv"

chmod 600 "A2/Romulan Imperial Star Navy/Valadore/reverv"


#  StarFleet

mkdir -p "A2/StarFleet/Defiant" \
         "A2/StarFleet/Discovery" \
         "A2/StarFleet/Enterprise" \
         "A2/StarFleet/Excelsior" \
         "A2/StarFleet/Hurd" \
         "A2/StarFleet/Stargazer" \
         "A2/StarFleet/Voyager"

chmod 500 "A2/StarFleet/Defiant" "A2/StarFleet/Discovery"

chmod 700 "A2/StarFleet/Enterprise" "A2/StarFleet/Excelsior" \
          "A2/StarFleet/Hurd" "A2/StarFleet/Stargazer" \
          "A2/StarFleet/Voyager"

# Defiant files
chmod u+w "A2/StarFleet/Defiant"

touch "A2/StarFleet/Defiant/defeats" \
      "A2/StarFleet/Defiant/upgrades" \
      "A2/StarFleet/Defiant/victories"

chmod 600 "A2/StarFleet/Defiant/defeats" \
          "A2/StarFleet/Defiant/upgrades"

chmod 700 "A2/StarFleet/Defiant/victories"

chmod 500 "A2/StarFleet/Defiant"

# Discovery  
chmod u+w "A2/StarFleet/Discovery"

mkdir -p "A2/StarFleet/Discovery/Conventional" \
         "A2/StarFleet/Discovery/mushroom"

chmod 700 "A2/StarFleet/Discovery/Conventional" \
          "A2/StarFleet/Discovery/mushroom"

check="A2/KlingonImperiaFleet/Raptor/check.txt"

# Discovery root files
touch "A2/StarFleet/Discovery/problems" \
      "A2/StarFleet/Discovery/violation"

ln  "$check" "A2/StarFleet/Discovery/trips" || true

chmod 600 "A2/StarFleet/Discovery/problems"

chmod 400 "A2/StarFleet/Discovery/trips"

chmod 700 "A2/StarFleet/Discovery/violation"

# Conventional
touch "A2/StarFleet/Discovery/Conventional/problems" \
      "A2/StarFleet/Discovery/Conventional/violation"

ln  "$check" "A2/StarFleet/Discovery/Conventional/trips" || true

chmod 600 "A2/StarFleet/Discovery/Conventional/problems"

chmod 400 "A2/StarFleet/Discovery/Conventional/trips"

chmod 700 "A2/StarFleet/Discovery/Conventional/violation"

# mushroom
ln  "$check" "A2/StarFleet/Discovery/mushroom/problems" || true

touch "A2/StarFleet/Discovery/mushroom/trips" \
      "A2/StarFleet/Discovery/mushroom/violation"

chmod 400 "A2/StarFleet/Discovery/mushroom/problems"

chmod 700 "A2/StarFleet/Discovery/mushroom/trips" \
          "A2/StarFleet/Discovery/mushroom/violation"

chmod 500 "A2/StarFleet/Discovery"     

# Enterprise
mkdir -p "A2/StarFleet/Enterprise/Constitution" \
         "A2/StarFleet/Enterprise/Soveriegn"

chmod 700 "A2/StarFleet/Enterprise/Constitution" \
          "A2/StarFleet/Enterprise/Soveriegn"

touch "A2/StarFleet/Enterprise/Constitution/USS1701"

touch "A2/StarFleet/Enterprise/Soveriegn/USS1701E"

chmod 600 "A2/StarFleet/Enterprise/Constitution/USS1701" \
          "A2/StarFleet/Enterprise/Soveriegn/USS1701E"

# Voyager
mkdir -p "A2/StarFleet/Voyager/2057" "A2/StarFleet/Voyager/2267"

chmod 700 "A2/StarFleet/Voyager/2057" "A2/StarFleet/Voyager/2267"

ln "A2/KlingonImperiaFleet/K't'inga/nova.txt" \
   "A2/StarFleet/Voyager/2267/delta.txt" || true

chmod 400 "A2/StarFleet/Voyager/2267/delta.txt"
