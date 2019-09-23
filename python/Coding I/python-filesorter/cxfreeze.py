import cx_Freeze as cx

executables = [cx.Executable("setup.py"), cx.Executable("sorter.py")]

cx.setup(
    name="File Sorter",
    version = "1.0",
    options={"build_exe": {"packages":["re", "shutil", "sys", "os","Tkinter", "time"], "include_files": ["/"]}},
    executables = executables
)