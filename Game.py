import sys
import argparse
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        

        

    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Breakout Deletion Game")
    parser.add_argument('fileName', type=str, help='Name der gelöschten Datei')
    args = parser.parse_args()

    if(args.fileName)
        app = QtWidgets.QApplication([])

        widget = MyWidget()
        widget.resize(800,600)
        widget.show()

    sys.exit(app.exec())