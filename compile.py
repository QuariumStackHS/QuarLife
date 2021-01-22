
import os
import time
import shutil
# create object dir
from cfg import *


def init():
    os.system(
        f"mkdir Env;mkdir Env/objects;mkdir Env/prod;mkdir Env/prod/OSX;mkdir Env/prod/Win64;mkdir Env/prod/Linux;mkdir Env/prod/{OS}/object;")


def clean():
    print("cleaning Workspace")
    shutil.rmtree("src/Dpart/.dub")
    shutil.copyfile("src/Dpart/libquarp.a", f"Env/prod/{OS}/object/libquarp.a")
    os.remove("src/Dpart/libquarp.a")


def compile():
    print("compiling Dpart...\n")
    os.system("cd src/Dpart;dub")
    print("compiling Engine...\n")
    os.system(
        f"g++ -Isrc/Engine/main/Includes -Isrc/Dpart/Headers  -pthread src/Engine/main/main.cpp -c -o Env/prod/{OS}/object/Engine.o")


def link():
    print("Linking All together...\n")

    os.system(f"g++ Env/prod/{OS}/object/*  -o {Pathtoexe}")
    clean()


def build():
    compile()
    link()


def run():
    os.system("./"+Pathtoexe)


tasks = {"compile": compile,
         "init": init,
         "link": link,
         "build": build,
         "run": run,
         "clean": clean}


def ExecTask(taskname="showtasks"):
    tasks.get(taskname)()


if __name__ == "__main__":
    import sys
    try:
        ExecTask(sys.argv[1])
    except Exception as e:
        print(f"REACT: {e}")
        print("usage: python3 [APP] Task")
