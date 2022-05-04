#!/usr/bin/python3

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
__authors__ = ['M.Amin Azimi .K(amzy-0)', 
'https://github.com/amzy-0/pck3r/graphs/contributors']

from os import system as syscall
from os import chdir
from sys import argv
from libs import stuff
from libs import dotnet
from libs import wine

argc = len(argv)

def error_sys(): 
    print('''%s%s
After "sys" is empty !

Please try:
$ pck3r sys <update/upgrade/updgr(update and upgrade)>%s'''
    % (stuff.sysERR() , stuff.RED, stuff.NRM))


while True:
        # check network connection, if internet not avalable BREAK the operation
        if (syscall('ping -c2 4.2.2.4 > /dev/null 2>&1')) != 0:

            if argc ==  2 and argv[1] == 'help':
                pass

            else:
                print('%s%sNetwork is unreachable\n%s' 
                % (stuff.sysERR(),stuff.RED, stuff.NRM))
                break
        # if user just type $ pck3r
        if argc <= 1:
                print('%s%sAfter "pck3r" is empty!\n%s\nPlease try:\n$ pck3r help %s\n' 
                    %  (stuff.sysERR(), stuff.RED, stuff.CYN, stuff.NRM))
                
        else:

            # if argument 1 equal to "clear"
            # clear terminal
            # do :
            if argv[1] == 'clear' and argc == 2:
                syscall('clear')
                print('%sThis is funny clear command :D ' 
                % stuff.sysOk())
            
            # pck3r updator
            elif argv[1] == 'update' and argc == 2:
                
                if (syscall('ls /opt/pck3r > /dev/null 2<&1'))==0:
                    chdir('/opt/pck3r')
                    syscall('sudo -p "[sudo]🔑 : " git pull ; sudo git restore .; ./installer.py')
                else:
                    print('''%s%sYou can not update pck3r with the "root" permission
                    %s'''
                    %(stuff.sysERR(), stuff.RED, stuff.NRM))

            # if argument 1 equal to "help"
            # like -> $ pck3r help
            # do :
            elif argv[1] == 'help' and argc == 2:
                from libs import help

            # if argument 1 equal to "install"
            # and argument 2 is not empty
            # do :
            elif argv[1] == 'install' and argc >= 2:

                # if after install is empty
                if argv[1]== 'install' and argc <= 2:
                    print('%s%sAfter "install" is empty !%s ' 
                    % (stuff.sysERR() , stuff.RED, stuff.NRM))
                
                elif argv[2] == 'flstudio' and argc == 3:
                    from libs import flstudio

                # if argument 2 is nodejs
                elif argv[2]=='nodejs' and argc==3:

                    if (syscall(
                        '''echo %s ; 
                            curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -p "[sudo]🔑 : " -E bash -; sudo -p "[sudo]🔑 : " apt install -y nodejs 
                            sudo -p "[sudo]🔑 : " apt update && echo %s;
                            echo %s;
                            sudo -p "[sudo]🔑 : " apt install yarnpkg -y''' 
                        % (stuff.YEL, stuff.CYN, stuff.MAG)))==0:

                        print('%s' % stuff.sysOk())

                        syscall('echo %s"Nodejs LTS Version :" ;  node --version %s' 
                        %(stuff.GRN, stuff.NRM))
                        syscall('echo "Npm Version :" %s; npm --version %s' 
                        %(stuff.GRN, stuff.NRM))

                        # Exception
                    else:
                        print('%s%s\nplease retry...\n$ pck3r install nodejs%s ' 
                        % (stuff.sysERR() , stuff.RED, stuff.NRM))

                elif argv[2] == 'dotnet' and argc==3:
                    dotnet.install_dotnet()

                elif argv[2] == 'ohmyzsh' and argc==3:
                    syscall('sudo -p "[sudo]🔑 : " apt install zsh curl')
                    if (syscall('curl --version')) == 0 :
                        syscall('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"') 
                    else:
                        syscall('echo "curl" is required for using "ohMyZsh" ; sudo -p "[sudo]🔑 : " apt install curl')
                        syscall('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"') 

                
                # wine installer blocks
                # command : $ pck3r install  wine 
                elif argv[2] == 'wine' and argc==3:
                    wine.wine_installer()

                # argument 2 is not empty

                elif argv[2:] != [] and argc >= 2:
                    print('%s%s\nCommand is valid : "$ pck3r install"\nLoading package lists...\n%s' 
                    % (stuff.sysOk(), stuff.GRN, stuff.YEL))

                    packages = argv[2:]
                    packages = list(packages)


                    for package in packages:

                        if syscall(('sudo -p "[sudo]🔑 : " apt install -f && sudo -p "[sudo]🔑 : " dpkg --configure -a ; sudo -p "[sudo]🔑 : " apt install %s  2> /dev/null ' 
                        % package))==0:
                            
                            if package[0] == '-':
                                continue
                            
                            failed = list()
                            failed.append(package)
                            syscall("echo %s; %s --version" % (stuff.GRN, package))
                            print('%s%sPackage(s) or Command(s) : %s Status : found ! ...%s'
                            % (stuff.sysOk(), stuff.GRN, ' '.join(failed), stuff.NRM))

                        elif syscall(('sudo -p "[sudo]🔑 : " apt install %s > /dev/null 2>&1' % package))==25600:
                            failed = list()
                            failed.append(package)
                            print('%s%sPackage(s) or Command(s) : %s Status : Not found ! ...%s'
                            % (stuff.sysERR(), stuff.RED, ' '.join(failed), stuff.NRM))
                            syscall('sleep 1')
                                                        

                        elif (syscall('sudo -p "[sudo]🔑 : " apt install %s 2> /dev/null ' 
                        % ' '.join(argv[2:]))) != 0 :
                                                    
                            # all the packages after "sudo apt install" assigned to the : packages variable
                            
                            for package in packages: #validation

                                # if(syscall('%s --version 2> /dev/null' % package))==0:
                                #     print('%s%s\n"%s" is already the newest version %s'
                                #     % (stuff.sysOk(), stuff.GRN, package, stuff.NRM))
                                
                                if (syscall('sudo -p "[sudo]🔑 : " apt install %s 2> /dev/null' % package))==25600:
                                    failed = list()
                                    failed.append(package)
                                    print('%s%sPackage(s) or Command(s) : "%s" Status : Not found ! ...'
                                    % (stuff.sysERR(), stuff.RED, ' '.join(failed)), end='')
                                    syscall('sleep 1')
                                    break
                         
                                print(stuff.NRM)
                            break

            # if argument 1 equal to "uninstall"
            elif argv[1] == 'uninstall' and argc >= 2:

                # if after "uninstall" is empty
                if argv[1] == 'uninstall' and argc <= 2:

                    print('%s %sAfter "uninstall" is empty !%s ' 
                    % (stuff.sysERR() , stuff.RED, stuff.NRM))
                
                # if user want uninstall dotnet 
                # do :
                elif argv[2]=='dotnet' and argc==3:
                    dotnet.uninstall_dotnet()

                # argument 2 is not empty
                # do :
                elif argv[2:] != [] and argc >= 2:
                    print('%s%s\nCommand is valid!\n%s' % (stuff.sysOk(), stuff.GRN, stuff.YEL))
                    syscall('sudo -p "[sudo]🔑 : " apt purge %s' % ' '.join(argv[2:]))

            # if argument 1 equal to "rm" (sudo apt remove)
            elif argv[1] == 'rm' and argc >= 2:

                # if after install is empty
                if argv[1]== 'rm' and argc<=2:
                    print('%s %sAfter "rm" is empty !%s ' % (stuff.sysERR() , stuff.RED, stuff.NRM))

                #  argument 2 is not empty
                # do :
                if argv[2:] != [] and argc>=2:
                    print('%s%s\nCommand is valid!\n%s' % (stuff.sysOk(), stuff.GRN, stuff.YEL))
                    syscall('sudo -p "[sudo]🔑 : " apt remove %s' % ' '.join(argv[2:]))

                # Exception
                else:
                    print('%sCommand or package(s) not found : %s' % (stuff.sysERR(), ' '.join(argv[2:])))


            # Too many arguments error for $ pck3r term
            # Only use :
            # $ pck3r tilix <somthing> <somthing> <somthing> <somthing>, ...
            elif argv[1] =='tilix' and argc==2:
                ans = input('install and run "tilix" terminal (y/n) ? ')
                if (ans == 'y'):
                    syscall('sudo -p "[sudo]🔑 : " apt install tilix  > /dev/null 2>&1 ;  tilix& > /dev/null 2>&1; clear')
                    
                else:
                    break


            # Too many arguments error for $ pck3r tilix
            # Only use :
            # $ pck3r tilix <somthing> <somthing> <somthing> <somthing>, ...
            elif argv[1] =='tilix' and argc>2:
                    print('%s%sToo many arguments !\nOnly use :\n$ pck3r term %s' % (stuff.sysERR(), stuff.RED, stuff.NRM))


            # if after "sys" command is empty
            elif argv[1] == 'sys' and argc == 2:
                error_sys()


            # if after pck3r equal to "sys"
            elif argv[1] == 'sys' and argc > 2:
                if argv[2]=='update' and argc==3:
                    if (syscall('sudo -p "[sudo]🔑 : " apt update')) == 0:
                        print('%s%s\nAll package(s) status : UPDATED%s' % (stuff.sysOk(), stuff.GRN, stuff.NRM))
                    else:
                        print(stuff.sysERR())
                # if user command, equal to $ pck3r sys upgrade
                #do :
                elif argv[2] == 'upgrade' and argc==3:
                    
                    if (syscall('sudo -p "[sudo]🔑 : " apt full-upgrade')) != 0:
                        print('%s' %stuff.sysERR())

                    else:                       
                        # print with green logo  
                        print('%s%sAll package(s) status : UPGRADED' % (stuff.sysOk(), stuff.GRN))
                        # echo green color and 
                        # and say:
                        syscall('echo %s' % stuff.GRN)
                    
                        # All information about OS 
                        syscall('echo your OS information :')
                        syscall('uname -a ')

                        # the machine architecture 
                        syscall('echo your machine architecture : ')
                        syscall('uname -p')
                        # end of the all information and 
                        #back to the true color of this terminal 
                        syscall('echo %s' % stuff.NRM)
                    
                    
                        

                # if user command, equal to $ pck3r sys updgr
                #do :
                elif argv[2] == 'updgr' and argc==3:
                    
                    if (syscall('sudo -p "[sudo]🔑 : " apt update && sudo -p "[sudo]🔑 : " apt full-upgrade')) != 0:
                        print('%s' %stuff.sysERR())

                    else:    
                        print('%s%sAll package(s) status : UPDATED and UPGRADED' % (stuff.sysOk(), stuff.GRN))
                        syscall('echo %s' % stuff.GRN)
                        syscall('echo your OS information :')
                        syscall('uname -a ')
                        syscall('echo your machine architecture : ')
                        syscall('uname -p')
                        syscall('echo %s' % stuff.NRM)
                                    
                # if command is not a valid one !
                # will send an error to the user.
                # do :
                else:
                    error_sys()

                    
            # if after "pkg" is empty
            elif argv[1]== 'pkg' and argc <= 2:
                print('%s%sAfter "pkg" is empty !%s ' % (stuff.sysERR() , stuff.RED, stuff.NRM))
            
            # if after "pkg" is not empty
            elif argv[1] == 'pkg' and argc >= 2:

                # if after "pkg" isn't empty
                if argv[2:] != [] and argc >= 2:
                    syscall('apt search %s' % ' '.join(argv[2:]))
            

            # if user want to see the pck3r version
            elif argv[1] == 'version' and argc ==2:
                chdir('/opt/pck3r')
                syscall(f'echo {stuff.CYN}version is : `git describe --tags --abbrev=0` {stuff.YEL}{stuff.NRM}')
                print(f'{stuff.NRM}{stuff.CYN}{", ".join(__authors__[:2])}, ...{stuff.NRM}')
          

            # if command not valid 
            # print :
            # and breaking any operation  
            else:
                print('%s%sCommand not found !%s\nPlease try:\n$ pck3r help %s'
                 % (stuff.sysERR(), stuff.RED, stuff.CYN, stuff.NRM))

        # end of (for) loop
        break
