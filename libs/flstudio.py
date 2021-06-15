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



if __name__ == '__main__':
    
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
    from . import wine
    from os import system as syscall
    from os import chdir, getenv

    chdir(getenv('HOME'))

    print(f'{stuff.YEL}')

    syscall('wget "https://archive.org/download/flstudio_202103/flstudio.exe"')

    print(f'{stuff.NRM}')

    syscall('wine flstudio.exe')