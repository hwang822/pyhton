# https://www.youtube.com/watch?v=0ftT1y_ckd0
# Python Scripting and AWS automation with Python

import os
import time
import re
import urllib

from subprocess import *
os.system('cls')
print ("please wait checking the pre-requisites.....")
time.sleep(2)

def welcome():
    print("*********************************")
    print("This Script will find the existing git version if any \nand also update /install latest git")
    print("*********************************")
    time.sleep(4)
    
def thank_you():
    print("\n\nThank you for using this script\nHave a great day\n")
    return none
   
def run_cmd_status(cmd)   
    sp = Popen(cmd.shell=true.stdout=PIPE.stderr=PIPE)
    rt=sp.wait()
    out.err=sp.communicate()
    return out

def is_root():
    if is_root()==true:
        print("you are the root user. so you can run this script")
    else:
        print("Please run this script as a root user")
        Thank_you()
        sys.exit(1)
        
except Exception as e:
    print e
    print{"Please rectify the erro and try it"}
    sys.exit(2)
try:
    #print("Checking wget command")
    #get_status=run_cmd_status('wget --version')
    if wget_status=='':
        #print("out is name")
        print("Please wait installing wget command")
        run_cmd_status("yum install wget -y")
        run_cmd_status("yum install wget -y")
    else:
        print("satisefied with wget command")
except Exception as e:
except Exception as e:
    print(e)
    print("please rectify the error and try it")
    Thank_you()
    sys.exit(3)
try:
    #print("Checking pip command")
    
def get_current_git_version():
sp=Popen('git--version', shell=true, sudout=PIPE, stder=PIPE)    
    rt=sp.wait()
    out, err=sp.communicate()
    if rt==0:
        if platform.system()=="windows":
            return out.strip().strip(".windows.1").split()[-1]
        else:
            returnout.split()[-1]
    else:
        if "not found" in err:
            return None
        print err*5+2
        sys.exit(2)
    
def all_git_versions():
    link="https://mirrors.edge.kerrnel.org/pub/software/scm/ig/"
    page=urllib.urlopen(link)
    html_doc=page.read()
    page.close()
    soup=Beautifulsoup(html_doc, 'html.parser')
    my_tar_ob=re.compile("git-\d\.\d+\.\d+\.tar\.gz")
    my_var_ob=re.complie("\d\, \d+\, \d+\, \d")
    href_link=[]
# .....................................

def main():
    git_ver=get_current_git_version()
    if git_var==None:
        print("Git is not installed\n")
        Print(Do you want to insall git on this host?")
        yes_or_no=user_request()
        new _install_git()
        print("Now your git is isnalled with version of {}".format(get_current_git_version()
        Thank_you()
    else 
        print ("Currently installed git vesion is: {}".format(git_ver)
        Print("Do you want to update git on this host?")
        yes_or_no=user_request()
        update_git(git_ver)
        print("Now your latest git is :",get_current_git_version())
        
  )

if __name__=="__main__":
    time.sleep(2)  
    print("Pre_requsisties are statiesfied")
    time.sleep(4)
    os.system('cls')
    welcome()
    main()
  
    