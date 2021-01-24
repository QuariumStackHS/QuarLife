#relative to build

#relative to OS Linux,OSX,Win64 are supported


Win64="Win64"
Linux="Linux"
OSX="OSX"
#Engine Dependancy
Libquarp="libquarp.a"
SDLVersion="2-2.0.14"
SDLPath="Deps/SDL"
SDLFullPath=SDLPath+SDLVersion
#Engine 


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

