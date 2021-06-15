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

# system error (red logo print)

from os import system as syscall

def install_dotnet():

    from . import stuff

    if (syscall('wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo dpkg -i packages-microsoft-prod.deb')) !=0 :
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)




    elif (syscall('sudo apt update')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt  install -y apt-transport-https')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt  update')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall(' sudo apt  install -y dotnet-sdk-3.1')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt  install -y aspnetcore-runtime-3.1')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt  install -y dotnet-runtime-3.1')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt install -y mono-complete')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 )  '% stuff.RED)



    elif (syscall('sudo apt  update')) != 0:
        stuff.sysERR()
        print('%sCan\'t install .NET (only for *UBUNTU 20.04 )  '% stuff.RED)


    else:
        stuff.sysOk()
        print('%s.NET(microsoft dotnet and MCS compiler (LINUX platform) ) installed  '% stuff.GRN )

def uninstall_dotnet():

    from . import stuff

    if (syscall('sudo apt update')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt purge  -y apt-transport-https')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt  update')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall(' sudo apt purge  -y dotnet-sdk-3.1')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt purge  -y aspnetcore-runtime-3.1')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt purge  -y dotnet-runtime-3.1')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 ) \n '% stuff.RED)



    elif (syscall('sudo apt purge  -y mono-complete')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 )  '% stuff.RED)



    elif (syscall('sudo apt  update && sudo apt full-upgrade ; sudo apt autoremove -y')) != 0:
        stuff.sysERR()
        print('%sCan\'t remove .NET (only for *UBUNTU 20.04 )  '% stuff.RED)


    else:
        stuff.sysOk()
        print('%s.NET(microsoft dotnet and MCS compiler (LINUX platform) ) reomved  '% stuff.GRN )




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
    """)