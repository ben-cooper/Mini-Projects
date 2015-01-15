from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('C:\\Users\\ben\\Desktop\\UTSC\\CSCA08\\minebackup.py', base='Win32GUI', targetName = 'minebackup.exe', icon='3D-Grass-Minecraft.ico')
]

setup(name='Minebackup',
      version = '1.0',
      description = 'A cyclic backup program for Minecraft.',
      options = dict(build_exe = buildOptions),
      executables = executables)
