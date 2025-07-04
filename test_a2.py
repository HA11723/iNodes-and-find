import unittest
import uuid
import os
import shutil
import subprocess
import stat
from pathlib import Path

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shell = "/usr/bin/bash"
        if not os.path.isfile(cls.shell):
            print("/usr/bin/bash not found, trying /bin/zsh for macs")
            cls.shell = "/bin/zsh"
    
        cls.test_files = [{"filename":"script2_1.sh", "mode":"744"},                           
                          {"filename":"part2_prep.sh", "mode":"744"},
                          {"filename":"script2_2a.sh", "mode":"744"},
                          {"filename":"script2_2b.sh", "mode":"744"},
                          {"filename":"script2_2c.sh", "mode":"744"}]
                          
        
        #Create working directory to execute script in 
        #a clean environment
        uidString = str(uuid.uuid4()) 
        
        workingdir = str(Path.home())+"/.cpsc1280"
        if os.path.isfile(workingdir):
            print("Working directory is a file, type 'rm ~/.cpsc1280' and try again")
            exit()
        if not os.path.isdir(workingdir):
            os.mkdir(workingdir)
        
        cls.test_directory = workingdir+"/Assignment2_"+uidString;
        
        os.mkdir(cls.test_directory)        
        print("Test ran in : " + cls.test_directory)
        for file in cls.test_files:
            if os.path.isfile(file["filename"]) :
                shutil.copy(file["filename"],cls.test_directory)
                new_filename = cls.test_directory + "/" + file["filename"];
                os.system("chmod "+ file["mode"]+" "+ new_filename)
            else:
                print("Setup failed, file " + file["filename"] + "Does not exist")
                assert("Setup failed, file " + file["filename"] + "Does not exist")
        os.chdir(cls.test_directory)        

    @classmethod
    def tearDown(cls):
        #uncomment in production
        #shutil.rmtree(cls.test_directory)
        pass
        
    def test_script2_1(self):
        print("Output for Part 1")
        scriptIdx = 0
        items = [ ["A2","drwx------"],
    ["A2/StarFleet","drwx------"],
    ["A2/StarFleet/Enterprise","drwx------"],
    ["A2/StarFleet/Enterprise/Constitution","drwx------"],
    ["A2/StarFleet/Enterprise/Constitution/USS1701","-rw-------"],
    ["A2/StarFleet/Enterprise/Soveriegn","drwx------"],
    ["A2/StarFleet/Enterprise/Soveriegn/USS1701E","-rw-------"],
    ["A2/StarFleet/Voyager","drwx------"],
    ["A2/StarFleet/Voyager/2057","drwx------"],
    ["A2/StarFleet/Voyager/2267","drwx------"],
    ["A2/StarFleet/Voyager/2267/delta.txt","-r--------"],
    ["A2/StarFleet/Discovery","dr-x------"],
    ["A2/StarFleet/Discovery/mushroom","drwx------"],
    ["A2/StarFleet/Discovery/mushroom/trips","-rwx------"],
    ["A2/StarFleet/Discovery/mushroom/violation","-rwx------"],
    ["A2/StarFleet/Discovery/mushroom/problems","-r--------"],
    ["A2/StarFleet/Discovery/Conventional","drwx------"],
    ["A2/StarFleet/Discovery/Conventional/problems","-rw-------"],
    ["A2/StarFleet/Discovery/Conventional/violation","-rwx------"],
    ["A2/StarFleet/Discovery/Conventional/trips","-r--------"],
    ["A2/StarFleet/Discovery/problems","-rw-------"],
    ["A2/StarFleet/Discovery/violation","-rwx------"],
    ["A2/StarFleet/Discovery/trips","-r--------"],
    ["A2/StarFleet/Stargazer","drwx------"],
    ["A2/StarFleet/Excelsior","drwx------"],
    ["A2/StarFleet/Hurd","drwx------"],
    ["A2/StarFleet/Defiant","dr-x------"],
    ["A2/StarFleet/Defiant/victories","-rwx------"],
    ["A2/StarFleet/Defiant/defeats","-rw-------"],
    ["A2/StarFleet/Defiant/upgrades","-rw-------"],
    ["A2/KlingonImperiaFleet","drwx------"],
    ["A2/KlingonImperiaFleet/D5 Cruiser","dr-x------"],
    ["A2/KlingonImperiaFleet/D5 Cruiser/beta1","-rw-------"],
    ["A2/KlingonImperiaFleet/D5 Cruiser/beta2","-rw-------"],
    ["A2/KlingonImperiaFleet/D5 Cruiser/beta3","-rw-------"],
    ["A2/KlingonImperiaFleet/Raptor","drwx------"],
    ["A2/KlingonImperiaFleet/Raptor/flight.txt","-r--------"],
    ["A2/KlingonImperiaFleet/Raptor/swim.txt","-r--------"],
    ["A2/KlingonImperiaFleet/Raptor/check.txt","-r--------"],
    ["A2/KlingonImperiaFleet/K't'inga","drwx------"],
    ["A2/KlingonImperiaFleet/K't'inga/seno.txt","-r--------"],
    ["A2/KlingonImperiaFleet/K't'inga/nova.txt","-r--------"],
    ["A2/KlingonImperiaFleet/Bird Of Prey","drwx------"],
    ["A2/KlingonImperiaFleet/Bird Of Prey/puppet","-rw-------"],
    ["A2/KlingonImperiaFleet/Bird Of Prey/gazlight","-rwx------"],
    ["A2/KlingonImperiaFleet/Bird Of Prey/navi","-rwx------"],
    ["A2/KlingonImperiaFleet/Bird Of Prey/chipoza","-rwx------"],
    ["A2/Romulan Imperial Star Navy","drwx------"],
    ["A2/Romulan Imperial Star Navy/Gasko","drwx------"],
    ["A2/Romulan Imperial Star Navy/Gasko/unknown","-rw-------"],
    ["A2/Romulan Imperial Star Navy/Valadore","drwx------"],
    ["A2/Romulan Imperial Star Navy/Valadore/reverv","-rw-------"],
    ["A2/Romulan Imperial Star Navy/Ship Type 1","drwx------"],
    ["A2/Romulan Imperial Star Navy/Ship Type 1/niky","-rwx------"],
    ["A2/Romulan Imperial Star Navy/D'deridex","dr-x------"],
    ["A2/Romulan Imperial Star Navy/D'deridex/$op runn.txt","-r--------"],
    ["A2/Romulan Imperial Star Navy/D7","dr-x------"],
    ["A2/Romulan Imperial Star Navy/D7/Rune","-rw-------"],
    ["A2/Romulan Imperial Star Navy/D7/Runo","-rw-------"],
    ["A2/Romulan Imperial Star Navy/D7/Run","-r--------"],
    ["A2/Romulan Imperial Star Navy/D8","dr--------"],
    ["A2/Romulan Imperial Star Navy/Bird Of Prey","drwx------"],
    ["A2/Romulan Imperial Star Navy/Bird Of Prey/nn","-rw-------"],
    ["A2/Romulan Imperial Star Navy/Bird Of Prey$(Early)","drwx------"],
    ["A2/Romulan Imperial Star Navy/Bird Of Prey$(Early)/oh","-rw-------"]]
    
        self.assertTrue(os.path.isfile(self.test_files[scriptIdx]["filename"]),"Testing directory is not a directory or does not exist")
        cpi = subprocess.run([self.shell, self.test_files[scriptIdx]["filename"]], capture_output=True, text=True)
        print(cpi.stdout)
        
        #check if files and directories exist with the correct permissions
        for item in items:
            try:
                status = os.stat(item[0])
            except:    
                self.assertTrue(False, f"Script did not create all required directories or files, missing {item[0]}")
            perms = stat.filemode(status.st_mode)
            assert perms == item[1], "Permission for " + item[0] + " not correct. perm =" + item[1] + ":" + perms
        file_pairs = [
            ["A2/StarFleet/Voyager/2267/delta.txt","A2/Romulan Imperial Star Navy/D7/Run"],
            ["A2/StarFleet/Voyager/2267/delta.txt","A2/KlingonImperiaFleet/K't'inga/nova.txt"],
            ["A2/StarFleet/Discovery/mushroom/problems","A2/StarFleet/Discovery/Conventional/trips"],
            ["A2/StarFleet/Discovery/mushroom/problems","A2/KlingonImperiaFleet/Raptor/check.txt"],
            ["A2/StarFleet/Discovery/mushroom/problems","A2/StarFleet/Discovery/trips"],
            ["A2/KlingonImperiaFleet/D5 Cruiser/beta2","A2/KlingonImperiaFleet/D5 Cruiser/beta3"]]
        
        #check if files are linked correctly
        for files in file_pairs:
            inum1 = os.stat(files[0]).st_ino
            inum2 = os.stat(files[1]).st_ino
            assert inum1 == inum2, "hard link for " + files[0] +" and " + files[1] + " do not match"
        
        file_sets = [ ["A2/StarFleet/Voyager/2267/delta.txt","A2/Romulan Imperial Star Navy/D7/Run","A2/KlingonImperiaFleet/K't'inga/nova.txt"],
                      ["A2/StarFleet/Discovery/mushroom/problems","A2/StarFleet/Discovery/Conventional/trips",
                       "A2/KlingonImperiaFleet/Raptor/check.txt","A2/StarFleet/Discovery/trips"],
                    ["A2/KlingonImperiaFleet/D5 Cruiser/beta2","A2/KlingonImperiaFleet/D5 Cruiser/beta3"]]

        #check if files are linked incorrectly
        for fileset1 in file_sets:
            for fileset2 in file_sets:
                file1 = fileset1[0];
                file2 = fileset2[0];
                if file1 != file2:
                    inum1 = os.stat(file1).st_ino
                    inum2 = os.stat(file2).st_ino                    
                    assert inum1 != inum2, "hard link for " + file1 +" and " + file2 + " match but should not match"

                    
        print("Test 1 finished")
    def test_script2_2a(self):
        print("Output for Part 2a")
        scriptIdx = 2
        self.assertTrue(os.path.isfile(self.test_files[1]["filename"]),"Prep script not found")
        self.assertTrue(os.path.isfile(self.test_files[scriptIdx]["filename"]),"script2_2a.sh not found")
        subprocess.run([self.shell, self.test_files[1]["filename"]])
        cpi = subprocess.run([self.shell, self.test_files[scriptIdx]["filename"]], capture_output=True, text=True)
        files = cpi.stdout.strip().split("\n")
        files.sort()
        print(cpi.stdout)
        expected_files = ["q2_p2/location1/ommeuf.txt",
                          "q2_p2/location1/ommeui.txt",
                          "q2_p2/location1/oooome.txt"]
        expected_files.sort()
        assert len(expected_files) == len(files), "File list is not correct"
        for i in range(len(expected_files)):
            assert expected_files[i] == files[i], "Files list is not correct"
        
    def test_script2_2b(self):
        print("Output for Part 2b")
        scriptIdx = 3
        self.assertTrue(os.path.isfile(self.test_files[1]["filename"]),"Prep script not found")
        self.assertTrue(os.path.isfile(self.test_files[scriptIdx]["filename"]),"script2_2b.sh not found")
        subprocess.run([self.shell, self.test_files[1]["filename"]])
        cpi = subprocess.run([self.shell, self.test_files[scriptIdx]["filename"]], capture_output=True, text=True)
        files = cpi.stdout.strip().split("\n")
        files.sort()
        expected_files = ["q2_p2/location1/oooo.mi -rw-r---w-",
                          "q2_p2/location2/orchard/zello/noether.ditto -rw-r---w-"]
        expected_files.sort()
        print(cpi.stdout)
        assert len(expected_files) == len(files), "File list is not correct"
        for i in range(len(expected_files)):
            assert expected_files[i] == files[i], "Files list is not correct"
        for file in expected_files:
            filename = file.split(" ")[0]
            status = os.stat(filename)
            assert status.st_mode & 0o002 == 0, "Write permission found on one of the listed files"
    
    def test_script2_2c(self):
        print("Output for Part 2c")
        scriptIdx = 4
        self.assertTrue(os.path.isfile(self.test_files[1]["filename"]),"Prep script not found")
        self.assertTrue(os.path.isfile(self.test_files[scriptIdx]["filename"]),"script2_2c.sh not found")
        subprocess.run([self.shell, self.test_files[1]["filename"]])
        cpi = subprocess.run([self.shell, self.test_files[scriptIdx]["filename"]], capture_output=True, text=True)
        files = cpi.stdout.strip().split("\n")
        files.sort()
        print(cpi.stdout)
        expected_files = [  "q2_p2/location1/zebra/zero.tmef",
                            "q2_p2/location1/zebra/zero",
                            "q2_p2/location1/zebra/zero.txt",
                            "q2_p2/location1/zany/topaz.txt",
                            "q2_p2/location2/orchard/zello/noether.ditto"]
        expected_files.sort()
        assert len(expected_files) == len(files), "File list is not correct"
        for i in range(len(expected_files)):
            assert expected_files[i] == files[i], "Files list is not correct"
        
if __name__ == '__main__':
    unittest.main()