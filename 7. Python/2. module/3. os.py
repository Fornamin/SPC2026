import os

print(os.getcwd())
os.chdir('C:/Src/SPC2026')
cwd = os.getcwd()
print(os.listdir(cwd))