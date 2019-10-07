import os

def __createDir__(nameList):
    for dirname in nameList:
        cmd = os.getcwd()
        #cmd = "mkdir "+dirname
        #os.system(cmd)
        #cmd = "cd "+dirname
        os.chdir(dirname)
        os.remove("touch Task.md")
        os.remove("touch submit.py")
        with open("Task.md", 'a'):
            try:                     # Whatever if file was already existing
                os.utime("Task.md", None)
            except:
                pass
        with open("submit.py", 'a'):
            try:                     # Whatever if file was already existing
                os.utime("submit.py", None)
            except:
                pass
        os.chdir(cmd)

if __name__ == '__main__':
    print(os.getcwd())
    nameList = list((range(3,31)))
    for i in range(len(nameList)):
        nameList[i] = "Day-"+str(nameList[i])
    __createDir__(nameList)
