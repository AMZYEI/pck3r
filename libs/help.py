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

from os import system as syscall


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

else:
    from . import stuff

    print("""%s

Pck3r : It is a versatile program. 
You avoid using useless commands, and it is written for Ubuntu.


\"install\" command :

    $ pck3r install \"somthing\" :
    {
        nodejs,
        wine,
        ohmyzsh,
        flstudio,
        or ...
    }

\"clear\" command :

    $ pck3r clear:
    {clear your terminal }

\"sys\" command :

    $ pck3r sys update
    (update your oprating system)

    $ pck3r sys upgrade
    (upgrade your oprating system)

    $ pck3r sys updgr
    (both, update and upgrade (full upgrade))

\"tilix\" command :

    $ pck3r tilix
    (tilix terminal ...)

\"dotnet\" command :

    $ pck3r install dotnet
    (installing .NET (dot net ) C0RE, ASP, MCS compiler , ...)

\"pkg\" command :

    $ pck3r pkg <package name>
    (search for packages ...)

\"update\" command :

    $ pck3r update
    (update to last release from github.com/amzy-0/pck3r)
    
"version" command :

    $ pck3r version
    (this command show pck3r version)


            %s
    """ % (stuff.YEL, stuff.NRM)
    )