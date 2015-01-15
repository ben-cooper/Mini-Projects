from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('C:\\Users\\ben\\Desktop\\UTSC\\CSCA08\\Side Projects\\typegame.py', base='Win32GUI', targetName = 'typegame.exe') #icon='3D-Grass-Minecraft.ico')
]

setup(name="A Typing Game By Ben Cooper",
      version = '1.1 Beta',
      description = 'A fun typing game!',
      options = dict(build_exe = buildOptions),
      executables = executables)
