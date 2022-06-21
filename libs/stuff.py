#!/usr/bin/python3

""" 

Copyright [2020-2021] [M.Amin Azimi .K (amzy-0)]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
__authors__ = ['M.Amin Azimi .K(amzy-0)', 'https://github.com/amzy-0/pck3r/graphs/contributors']


#color zone
NRM = "\x1B[0m"
RED = "\x1B[31m"
GRN = "\x1B[32m"
YEL = "\x1B[33m"
BLU = "\x1B[34m"
MAG = "\x1B[35m"
CYN = "\x1B[36m"
WHT = "\x1B[37m"
#end of color zone

# Modules error !

def stop():
    print("""
This is a module not an executeable program
Alternative command :
$ python3 core_pck3r.py
OR
$ python3 installer.py
OR
$ chmod 755 core_pck3r.py ; ./core_pck3r.py
And for installing :
$ chmod 755 installer.py ; ./installer.py
    """ )

if __name__ == "__main__":
    stop()
else:
    # system error (red logo print)
    def sysERR(MSG=''):
        print("\n%s尸⼕长㇌尺 : ERROR !\n%s\n%s"% (RED, MSG, NRM))

    #system call done (green logo print)
    def sysOk(MSG=''):
        print("\n%s尸⼕长㇌尺 :\n %s\n%s" % (GRN, MSG, NRM))
