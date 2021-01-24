
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


def init(arg):
    pass
# create


def clean(arg):
    print("\ncleaning Workspace")
    shutil.rmtree("src/Dpart/.dub")
    shutil.copyfile(f"src/Dpart/{Libquarp}",
                    f"Env/prod/{OS}/object/{Libquarp}")
    os.remove(f"src/Dpart/{Libquarp}")
    
    shutil.rmtree("src/Server/.dub")
    shutil.copyfile(f"src/Server/{ServerCore}",
                    f"Env/prod/{OS}/{ServerCore}")
    os.remove(f"src/Dpart/{ServerCore}")


def compile(Part: str):
    if Part == "Dpart":
        print(f"{bcolors.HEADER}compiling Dpart...\n{bcolors.BOLD}")
        SC = os.getcwd()
        os.chdir("src/Dpart")
        os.system("dub")
        os.chdir(SC)
        print(bcolors.ENDC,end="")
        if os.path.exists(f"src/Dpart/{Libquarp}"):
            print(
                f"{bcolors.OKGREEN}---compiled Dpart succesfuly!---{bcolors.ENDC}\n")
        else:
            input(
                f"{bcolors.FAIL} Compilation failed... (press enter to quit){bcolors.ENDC}")
            exit()
    if Part == "Dserver":
        print(f"{bcolors.HEADER}compiling Server-Core...\n{bcolors.BOLD}")
        SC = os.getcwd()
        os.chdir("src/Server")
        os.system("dub")
        os.chdir(SC)
        print(bcolors.ENDC,end="")
        if os.path.exists(f"src/Dpart/{ServerCore}"):
            print(
                f"{bcolors.OKGREEN}---compiled Server-Core succesfuly!---{bcolors.ENDC}\n")
        else:
            input(
                f"{bcolors.FAIL} Compilation failed... (press enter to quit){bcolors.ENDC}")
            exit()
    elif Part == "Engine":
        print(f"{bcolors.HEADER}compiling Engine...\n{bcolors.BOLD}")
        os.system(
            f"g++ -Isrc/Engine/main/Includes -Isrc/Dpart/Headers -I{SDLFullPath}/include -pthread src/Engine/main/main.cpp -c -o Env/prod/{OS}/object/Engine.o")
        if os.path.exists(f"Env/prod/{OS}/object/Engine.o"):
            print(f"{bcolors.OKGREEN}---compiled Engine succesfuly!---{bcolors.ENDC}")
        else:
            input(
                f"{bcolors.FAIL} Compilation failed... (press enter to quit){bcolors.ENDC}")
            exit()
    else:
        print("Valids args for compile are Engine, Dpart, Dserver", Part)


def link(arg):
    print(f"{bcolors.HEADER}Linking All together...\n{bcolors.ENDC}")

    os.system(f"g++ Env/prod/{OS}/object/*  -o {Pathtoexe}")

    if os.path.exists(Pathtoexe):
        print(f"{bcolors.OKGREEN}--- Linking succesfuly!---{bcolors.ENDC}")
    else:
        input(
            f"{bcolors.FAIL} linking failed... (press enter to quit){bcolors.ENDC}")
    clean("")


def build(arg):
    compile("Dpart")
    compile("Engine")
    link("all")
    print("I wish you the Best to run...")


class F:
    def __init__(self, addr, desc) -> None:
        self.addr = addr
        self.desc = desc

    def run(self, Kwargs=""):
        self.addr(Kwargs)


def deploy(arg):
    pass


def run(arg):
    os.system(runcommand)


def BuildDeps(N):
    if OS == OSX:
        os.system(f"""cd {SDLFullPath};./configure;make;sudo make install""")
    elif OS == Win64:
        os.ch
        os.system(f"make {SDLFullPath}")


def test():
    build()
    run()


tasks = {
    # taskname    taskfunc  Task Description
    "build-dep": F(BuildDeps, "Build Dependancys"),
    "compile": F(compile, "Compile Dpart or Engine"),
    "init": F(init, "initialise dirs (only work on Unix for now)"),
    "link": F(link, "Link All Obj togehter"),
    "build": F(build, "Compile ALL+Link+Clean"),
    "run": F(run, "run game (configure in cfg.py)"),
    "clean": F(clean, "Remove temporary file"),
    "test": F(test, "Build+Run")
    # "deploy":F(deploy,"Deploy App With version")
}


def ExecTask(taskname="help"):
    if taskname == "compile":
        tasks.get(taskname).run(sys.argv[2])
    tasks.get(taskname).run()


if __name__ == "__main__":
    import sys
    try:
        ExecTask(sys.argv[1])
    except Exception as e:
        print(f"{bcolors.FAIL}List of available Tasks: {bcolors.ENDC}({bcolors.OKBLUE}{str(len(tasks))}{bcolors.ENDC}):")
        for i in tasks:
            print(f"    {bcolors.OKCYAN}{i}{bcolors.ENDC}", (9-len(i))
                  * " ", f"{bcolors.OKGREEN}{tasks.get(i).desc}{bcolors.ENDC}")

        print()
        print(f"usage: python3 [APP] [Task]\n")
        if Debug:
            print("-----------Debug-----------")
            print("Last path = "+os.getcwd())
            print(f"{bcolors.FAIL}REACT: {e}{bcolors.ENDC}")
