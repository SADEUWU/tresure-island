import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("tresure.island.py", base=base, icon="Icone.ico")
]


setup(
    name="tresure.island",
    version="1.0",
    description="Game.exe",
    executables=executables
)
