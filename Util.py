
import os
import time
import shutil
import subprocess

# create object dir
from cfg import *


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles
# print(getListOfFiles("."))


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
    try:
        print("\ncleaning Workspace")
        shutil.rmtree("src/Dpart/.dub")
        shutil.copyfile(f"src/Dpart/{Libquarp}",
                        f"Env/prod/{OS}/object/{Libquarp}")
        os.remove(f"src/Dpart/{Libquarp}")

        shutil.rmtree("src/Server/.dub")
        shutil.copyfile(f"src/Server/{ServerCore}",
                        f"Env/prod/{OS}/{ServerCore}")
        os.remove(f"src/Server/{ServerCore}")
    except:
        pass


def compile(Part: str):
    if Part == "Mods":
        print(f"{bcolors.HEADER}compiling Mods... {bcolors.BOLD}")
        SC2 = os.getcwd()
        os.chdir("src/Engine/main/mods/source")
        mods = []
        for i in os.listdir("."):
            if os.path.isdir(i):
                mods.append(i)
        for l in mods:
            SC = os.getcwd()
            # print(f"{SC}/{l}")
            os.chdir(f"{SC}/{l}")
            # print(l)
            k = getListOfFiles(".")
            #print(k)
            os.chdir(SC)
            for i in k:
                #print("compiling: ", i)
                if i.endswith(".cpp"):
                    print("CD: ", os.getcwd())
                    print(f"{bcolors.HEADER}compiling: {bcolors.BOLD}", i[2:len(i)],)
                    os.system(
                        f"g++ -c {SC+('/'+l+'/')+i[2:len(i)]} -pthread -I{SC2}/src/Engine/main/Includes -I{SC2}/Deps/libpqxx/include/pqxx -o {(SC2+'/'+outputpath+'/'+l+'_'+(i.split('/')[-1]).replace('.','_'))}.o")
                    if os.path.exists(f"{(SC2+'/'+outputpath+'/'+l+'_'+(i.split('/')[-1]).replace('.','_'))}.o"):
                        print(
                            f"{bcolors.OKGREEN}---compiled '{l+' -> '+(i[2:len(i)])}' succesfuly!---{bcolors.ENDC}\n")
                    else:
                        input(
                            f"{bcolors.FAIL} Compilation failed in '{i}''... (press enter to quit){bcolors.ENDC}")
        os.chdir(SC2)

    if Part == "server":
        print(f"{bcolors.HEADER}compiling Server-Core...\n{bcolors.BOLD}")
        SC = os.getcwd()
        os.chdir("src/Server")
        os.system(
            f"g++ -Isrc/Engine/main/Includes -Isrc/Dpart/Headers -pthread src/Server/source/main.cpp -c -o Env/prod/{OS}/objects/ServerSide.o")
        os.chdir(SC)
        print(bcolors.ENDC, end="")
        if os.path.exists(f"src/Server/{ServerCore}"):
            print(
                f"{bcolors.OKGREEN}---compiled Server-Core succesfuly!---{bcolors.ENDC}\n")
        else:
            input(
                f"{bcolors.FAIL} Compilation failed... (press enter to quit){bcolors.ENDC}")
            exit()
    elif Part == "Engine":
        print(f"{bcolors.HEADER}compiling Engine...\n{bcolors.BOLD}")
        os.system(
            f"g++ -Isrc/Engine/main/Includes -std=c++17 -Isrc/Dpart/Headers -Isrc/Dpart/source -I{SDLFullPath}/include -pthread src/Engine/main/main.cpp -c -o Env/prod/{OS}/objects/Engine/Engine.o")
        if os.path.exists(f"Env/prod/{OS}/objects/Engine/Engine.o"):
            print(f"{bcolors.OKGREEN}---compiled Engine succesfuly!---{bcolors.ENDC}")
        else:
            input(
                f"{bcolors.FAIL} Compilation failed... (press enter to quit){bcolors.ENDC}")
            exit()
    else:
        print("Valids args for compile are Engine, QuarP, server, Mods; Not: ", Part)


def link(arg):
    print(f"{bcolors.HEADER}Linking All together...\n{bcolors.ENDC}")

    os.system(
        f"g++ Env/prod/{OS}/objects/Engine/* Env/prod/{OS}/objects/mods/*.o -pthread -o {Pathtoexe}")

    if os.path.exists(Pathtoexe):
        print(f"{bcolors.OKGREEN}--- Linking succesfuly!---{bcolors.ENDC}")
    else:
        input(
            f"{bcolors.FAIL} linking failed... (press enter to quit){bcolors.ENDC}")
    clean("")


def start_WebApp(arg):
    output = subprocess.Popen(
        ["sudo", "python3", "src/WEB/app.py"], stdout=subprocess.PIPE).communicate()
    print(output[0].decode())
    #os.system("python3 src/WEB/app.py")


class component:
    def __init__(self, path, compilecommand):
        self.path = path
        self.command = compilecommand


def build(t=""):
    compile("Mods")
    #compile("Dserver")
    compile("Engine")
    #compile("Mods")
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


def run(t=""):
    os.system(runcommand)


def BuildDeps(N):
    if OS == OSX:
        os.system(f"""cd {SDLFullPath};./configure;make;sudo make install""")
    elif OS == Win64:
        os.ch
        os.system(f"make {SDLFullPath}")


def test(t=""):
    build()
    run()
def PostGresBuild(arg):
    SC2=os.getcwd()
    os.chdir(SC2+"/Deps/libpqxx")
    os.system("./configure --with-postgres-include")
    os.system("make ")
    os.system("sudo make install")

    pass

tasks = {
    # taskname    taskfunc  Task Description
    "build-dep": F(BuildDeps, "Build Dependancys"),
    "compile": F(compile, "Compile Dpart, Dserver or Engine"),
    "init": F(init, "initialise dirs (only work on Unix for now)"),
    "link": F(link, "Link All Obj together"),
    "build": F(build, "Compile ALL+Link+Clean"),
    "run": F(run, "run game (configure in cfg.py)"),
    "clean": F(clean, "Remove temporary file"),
    "test": F(test, "Build+Run"),
    "Start_Web": F(start_WebApp, "run app.py in the terminal"),
    "deploy": F(deploy, "Deploy App With version (not implemented YET)"),
    "build-PostGresql":F(PostGresBuild,"Build post gres")
}


def ExecTask(taskname="help"):
    if taskname == "compile":
        try:
            tasks.get(taskname).run(sys.argv[2])
        except:
            print("Compile take a switch!")
    else:
        try:
            tasks.get(taskname).run()
        except:
            pass


if __name__ == "__main__":
    import sys
    try:
        ExecTask(sys.argv[1])
    except Exception as e:
        print(f"{bcolors.FAIL}List of available Tasks: {bcolors.ENDC}({bcolors.OKBLUE}{str(len(tasks))}{bcolors.ENDC}):")
        maxs = 0
        for i in tasks:
            if maxs < len(i):
                maxs = len(i)
        for i in tasks:
            print(f"    {bcolors.OKCYAN}{i}{bcolors.ENDC}", (maxs-len(i))
                  * " ", f"{bcolors.OKGREEN}{tasks.get(i).desc}{bcolors.ENDC}")

        print()
        print(f"usage: python3 [APP] [Task]\n")
        if Debug:
            print("-----------Debug-----------")
            print("Last path = "+os.getcwd())
            print(f"{bcolors.FAIL}REACT: {e}{bcolors.ENDC}")
