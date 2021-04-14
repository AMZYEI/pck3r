#!/usr/bin/python3

""" 

Short description of this Python module.
Longer description of this module.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

"""
__authors__ = ['M.Amin Azimi .K(amzy-0)', 'https://github.com/amzy-0/pck3r/graphs/contributors']


from libs import stuff
from os import  getcwd, getenv, chdir
from os import system as syscall
###############################################################################
# preinstall requirements                                                     
syscall('mkdir -p ~/.pck3r/icon ; cp -rf ./icon/pck3r-logo.png ~/.pck3r/icon')
syscall('''sudo apt install \\
     python3-tk python3-pil python3-pil.imagetk g++ libnotify-bin -y > /dev/null 2>&1 ''')                                                                                     
###############################################################################
import tkinter as tk
from tkinter.ttk import *
import time
from PIL import ImageTk,Image

# creating tkinter window
root = tk.Tk()


make_link = 'sudo ln -s %s/.pck3r/core_pck3r.py /bin/pck3r' % getenv('HOME')

# Progress bar widget
progress = Progressbar(root, length = 100, mode = 'determinate')

# Function responsible for the updation
# of the progress bar value
def bar():

    # 20% PROGRESS
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    syscall('sudo unlink /bin/pck3r > /dev/null 2>&1')

    # 40% PROGRESS
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
   
    syscall('rm -rf ~/.pck3r && sudo rm -rf /root/.pck3r')
    syscall('mkdir ~/.pck3r')
    syscall('cp -rf . ~/.pck3r')
    syscall('sudo cp -rf . /root/.pck3r')

    # 50% PROGRESS
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
    syscall(make_link)

    # 60% PROGRESS
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
    
    if (syscall('ls -l /bin/pck3r > /dev/null 2>&1')) == 0:
        pass
    else:
        syscall('notify-send --icon="/$(pwd)/icon/pck3r-logo.png" "尸⼕长㇌尺 : No link"')
    
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)

    # 100% PROGRESS
    progress['value'] = 100
    syscall('''notify-send --icon="/$(pwd)/icon/pck3r-logo.png"\\
        "尸⼕长㇌尺 :Link created &\n installed successfuly"''')
    
    root.quit()


# packing to main window (panel)
icon = Image.open('%s/.pck3r/icon/pck3r-logo.png' % getenv('HOME'))
root.title('Pck3r Installer')
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False, photo)
root.geometry('400x80')
root.configure(background='black')
root.resizable(False, False)
progress.pack(fill='x', pady = 10)
installBtn = tk.Button(root, text='install pck3r (system wide) ', command = bar)
installBtn.configure(fg='lightblue', bg='darkred',)

installBtn.pack(fill='x', pady = 10)

# infinite loop
tk.mainloop()
