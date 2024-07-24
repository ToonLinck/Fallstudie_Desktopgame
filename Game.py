import sys
import argparse
from PySide6 import QtCore, QtWidgets, QtGui
import winreg 
import imageio as iio
from screeninfo import get_monitors

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        

def get_wallpaper():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop")
        value, _ = winreg.QueryValueEx(key, "Wallpaper")
        winreg.CloseKey(key)
        return value
    except Exception as e:
        return str(e)        

    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Breakout Deletion Game")
    #parser.add_argument('fileName', type=str, help='Name der gelöschten Datei')
    args = parser.parse_args()

    wallpaperPath = get_wallpaper()
    wallpaperImage = iio.imread(wallpaperPath)

    main_monitor = get_monitors()[0]


    if(True):
        app = QtWidgets.QApplication([])

        widget = MyWidget()
        widget.resize( main_monitor.width,main_monitor.height)
        widget.show()

    sys.exit(app.exec())


