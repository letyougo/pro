import os


def getPythonPath():
    if os.getenv("PYTHON") != None:
        return os.getenv("PYTHON")
    sys_path = os.getenv("path")
    li = sys_path.split(';')
    li.sort()
    for i in range(len(li)):
        if li[i].find('Python') != -1 or li[i].find('python') != -1:
            python_path.append(li[i])
    for i in range(len(python_path)):
        try:
            os.chdir(python_path[i])
            python_exe = os.listdir(python_path[i])
            for j in range(len(python_exe)):
                if python_exe[j].find('python.exe') == 0:
                    return python_path[i] + os.sep + python_exe[j]
        except:
            pass


print(getPythonPath()  )
