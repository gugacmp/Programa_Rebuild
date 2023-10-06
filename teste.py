#Caminho : C:\Users\campos\Documents\GitHub\Hub-Gerenciamento\Hub-Gerenciamento>
#No prompt, digite python teste.py build
from cx_Freeze import setup, Executable

base = None    

executables = [Executable("sgarebuild.py", base=base)]

packages = ["random", "matplotlib", "numpy", "tqdm", "datetime","time", "colorama", "pyplot"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Sga Rebuild",
    options = options,
    version = "1.1.4",
    description = 'Sga Rebuild',
    executables = executables
)