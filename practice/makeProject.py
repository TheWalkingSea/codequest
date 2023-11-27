import easygui
import os
import zipfile
import shutil
path = easygui.fileopenbox()
filename = os.path.basename(path).removesuffix(".zip")

os.mkdir(filename)
testCases = os.path.join(filename, "testCases")
os.mkdir(testCases)

with zipfile.ZipFile(path, 'r') as f:
    f.extractall(testCases)

shutil.copy("src/compile.py", filename)
shutil.copy("src/test.py", filename)

