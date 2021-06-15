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

def wine_installer():
    from os import system as syscall 
    from os import getenv, chdir
    from . import stuff

    syscall("sudo apt update && sudo apt full-upgrade")
    home = getenv("HOME")
    chdir(home)
    

    if (syscall("""
    sudo dpkg --add-architecture i386; 
    wget -nc https://dl.winehq.org/wine-builds/winehq.key;
    sudo apt-key add winehq.key;
    sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main' ;
    sudo apt install --install-recommends winehq-stable;
    """))!=0:

        print(f"{stuff.sysERR()}{stuff.NRM}")

    else:
        syscall("clear")
        print(stuff.sysOk())
        print(f"{stuff.GRN}wine version :")
        syscall(f"wine --version && echo {stuff.NRM}")


if __name__ == "__main__":

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


