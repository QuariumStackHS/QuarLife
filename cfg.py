#relative to build

#relative to OS Linux,OSX,Win64 are supported


Win64="Win64"
Linux="Linux"
OSX="OSX"

OS=OSX
Debug=True
if OS==OSX:
    Pathtoexe=f"Env/prod/{OS}/main.app/Contents/MacOS/Game"
elif OS==Win64:
    Pathtoexe=f"Env/prod/{OS}/Game.exe"
elif OS==Linux:
    Pathtoexe=f"Env/prod/{OS}/Game"
else:
    Pathtoexe="None"
    print(f"{OS} is not supported")
runcommand=f"./{Pathtoexe}"

