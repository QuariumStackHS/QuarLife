#relative to build
runcommand="./Env/prod/OSX/main.app/Contents/MacOS/Game"
#relative to OS Linux,OSX,Win64 are supported
OS="OSX"

if OS=="OSX":
    Pathtoexe=f"Env/prod/{OS}/main.app/Contents/MacOS/Game"
elif OS=="Win64":
    Pathtoexe=f"Env/prod/{OS}/Game.exe"
elif OS=="Linux":
    Pathtoexe=f"Env/prod/{OS}/Game"

