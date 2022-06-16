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

    elif purpose == "OD":
        temp_file_name = "OD #.txt"
        ver = 1
        for file in os.listdir():
            if file.startswith("OD"):
                ver += 1
        return temp_file_name.replace("#", str(ver))

    with open(temp_file_name, 'w') as f:
        f.close()


def saveData(data, FILE_NAME):
    with open(FILE_NAME, 'a') as f:
        f.write(str(data) + "\n")
        f.close()


def ODdisplay(oled, value):
    oled.fill(0)
    oled.text("OD value: ", 0, 8)
    oled.text(str(value), 10, 17)
    oled.show()


def TempDisplay(oled, temp):
    oled.fill(0)
    oled.text("Temperature: ", 0, 8)
    oled.text(str(temp), 10, 17)
    oled.show()


def cleanTXTFiles():
    for files in os.listdir():
        if files.endswith(".txt"):
            os.remove(files)


files = ['boot.py', 'read_temp.py', 'pump.py', 'main_2.py',
         'cooler.py', 'linearize.py', 'ssd1306.py', 'utils.py']
for file in os.listdir():
    if not file.endswith('.py'):
        os.remove(file)
