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


from libs import stuff
from os import system as syscall
# install dependancies 
syscall('pip install progress')

from progress.bar import Bar

###############################################################################
# preinstall requirements                                                     
if syscall('sudo -p "[sudo]🔑 : " mkdir -p /opt/pck3r/')!=0:
    quit()
###############################################################################

import time

make_link = ' sudo   ln -s  /opt/pck3r/core_pck3r.py /bin/pck3r'

# Progress bar widget

# Function responsible for the updation
# of the progress bar value

with Bar('INSTALLING', fill='\U0001F709', max=100) as bar:

    # 20% PROGRESS 
    syscall(' sudo   unlink /bin/pck3r > /dev/null 2>&1')
    bar.next(20)

    # 40% PROGRESS
    time.sleep(1)
   
    syscall('sudo rm -rf /opt/pck3r')
    syscall('sudo cp -rf . /opt/pck3r')
    bar.next(20)

    # 50% PROGRESS
    time.sleep(1)
    syscall(make_link)
    bar.next(10)

    # 60% PROGRESS
    time.sleep(1)
    if (syscall('sudo ls -l /bin/pck3r > /dev/null 2>&1')) == 0:
        pass
    else:
        syscall('%s%sNO LINK ! (/bin/pck3r)%s' % (stuff.sysERR(), stuff.RED, stuff.NRM))
    

    time.sleep(1)
    bar.next(10)

    # 100% PROGRESS
    bar.next(40)
    print('\n%s\bLink created and installed successfuly' % (stuff.sysOk()))
