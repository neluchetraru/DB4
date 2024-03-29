import os


def getNewFileName(purpose):
    temp_file_name = ""
    if purpose == "temperature":
        temp_file_name = "temp #.txt"
        ver = 1
        for file in os.listdir():
            if file.startswith("temp"):
                ver += 1
        return temp_file_name.replace("#", str(ver))

    elif purpose == "absorbance":
        temp_file_name = "absorbance #.txt"
        ver = 1
        for file in os.listdir():
            if file.startswith("absorbance"):
                ver += 1
        return temp_file_name.replace("#", str(ver))

    with open(temp_file_name, 'w') as f:
        f.close()


def saveData(data, FILE_NAME):
    with open(FILE_NAME, 'a') as f:
        f.write(str(data) + "\n")
        f.close()


def cleanTXTFiles():
    for files in os.listdir():
        if files.endswith(".txt"):
            os.remove(files)
