
import os
import time
import shutil
# create object dir
from cfg import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def init():
    os.system(
        f"mkdir Env;mkdir Env/objects;mkdir Env/prod;mkdir Env/prod/OSX;mkdir Env/prod/Win64;mkdir Env/prod/Linux;mkdir Env/prod/{OS}/object;")


def clean():
    print("\ncleaning Workspace")
    shutil.rmtree("src/Dpart/.dub")
    shutil.copyfile("src/Dpart/libquarp.a", f"Env/prod/{OS}/object/libquarp.a")
    os.remove("src/Dpart/libquarp.a")


def compile():
    print(f"{bcolors.HEADER}compiling Dpart...\n{bcolors.ENDC}")
    os.system("cd src/Dpart;dub")
    if os.path.exists(f"src/Dpart/libquarp.a"):
        print(f"{bcolors.OKGREEN}---compiled Dpart succesfuly!---{bcolors.ENDC}\n")
    else:
        input(
            f"{bcolors.FAIL} Compilation failed... (press enter to quit){bcolors.ENDC}")
    print(f"{bcolors.HEADER}compiling Engine...\n{bcolors.ENDC}")
    os.system(
        f"g++ -Isrc/Engine/main/Includes -Isrc/Dpart/Headers  -pthread src/Engine/main/main.cpp -c -o Env/prod/{OS}/object/Engine.o")
    if os.path.exists(f"Env/prod/{OS}/object/Engine.o"):
        print(f"{bcolors.OKGREEN}---compiled Engine succesfuly!---{bcolors.ENDC}")
    else:
        input(
            f"{bcolors.FAIL} Compilation failed... (press enter to quit){bcolors.ENDC}")


def link():
    print(f"{bcolors.HEADER}Linking All together...\n{bcolors.ENDC}")

    os.system(f"g++ Env/prod/{OS}/object/*  -o {Pathtoexe}")
    
    if os.path.exists(Pathtoexe):
        print(f"{bcolors.OKGREEN}---compiled Linking succesfuly!---{bcolors.ENDC}")
    else:
        input(
            f"{bcolors.FAIL} linking failed... (press enter to quit){bcolors.ENDC}")
    clean()


def build():
    compile()
    link()


class F:
    def __init__(self, addr, desc) -> None:
        self.addr = addr
        self.desc = desc

    def run(self):
        self.addr()


def deploy():
    pass


def run():
    os.system(runcommand)


def test():
    build()
    run()


tasks = {
    # taskname    taskfunc  Task Description
    "compile": F(compile, "Compile Dpart and Engine"),
    "init": F(init, "initialise dirs (only work on Unix for now)"),
    "link": F(link, "Link All Obj togehter"),
    "build": F(build, "Compile+Link+Clean"),
    "run": F(run, "run game (configure in cfg.py)"),
    "clean": F(clean, "Remove temporary file"),
    "test": F(test, "Build+Run")
    # "deploy":F(deploy,"Deploy App With version")
}


def ExecTask(taskname="help"):
    tasks.get(taskname).run()


if __name__ == "__main__":
    import sys
    try:
        ExecTask(sys.argv[1])
    except Exception as e:
        print(f"{bcolors.FAIL}List of available Tasks: {bcolors.ENDC}({bcolors.OKBLUE}{str(len(tasks))}{bcolors.ENDC}):")
        for i in tasks:
            print(f"    {bcolors.OKCYAN}{i}{bcolors.ENDC}", (9-len(i))*" ", f"{bcolors.OKGREEN}{tasks.get(i).desc}{bcolors.ENDC}")

        print()
        print(f"usage: python3 [APP] [Task]")
        if Debug:

            print(f"{bcolors.FAIL}REACT: {e}{bcolors.ENDC}")
