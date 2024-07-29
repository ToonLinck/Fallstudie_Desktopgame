import sys
import argparse
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
import winreg 
import imageio as iio
from screeninfo import get_monitors
import pythoncom
import win32com

#Gibt den Pfad des Desktop-Wallpapers zurueck
def get_wallpaper():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop")
        value, _ = winreg.QueryValueEx(key, "Wallpaper")
        winreg.CloseKey(key)
        return value
    except Exception as e:
        return str(e)  

#the called files is searched for in the systems deleted files directory and if possible restored
def recreate_Deleted_File(file_name):
    pythoncom.CoInitialize()                                            # starts the Com-library
    try: 
        shell = win32com.client.Dispatch("Shell.Application")           # starts a Shell object to recieve Shell functions
        bin = shell.NameSpace(10)                               # gets the bin (10 is the bins id)
        for item in bin.Items():
            if item.Name == file_name:
                for verb in item.Verbs():                               # goes threw all functions the item has
                    if verb.Name.replace('&', '') == "Wiederherstellen":                # checks for the 'Wiederherstellen' function
                        verb.DoIt()                                                     # calls the function
                        print(f"The file '{file_name}' got restored.")
                        return
                print(f"The file '{file_name}' couldnt be restored.")
                return
        print(f"The file '{file_name}' couldnt be found.")
    finally:
        pythoncom.CoUninitialize()

#find if file_name is the name of an existend file inside the deleted files directory
def find_File_in_Bin(file_name):
    pass

def end_game(has_won, deleted_file_name):
    if has_won:
        #create log
        #close Game
        pass
    else:
        recreate_Deleted_File(deleted_file_name)
        #close game
        pass

class BreakoutBall():               #The object of the "Ball"

    velocity = {0,1}
    position = {50,50}
    shape_pixmap = QPixmap

    def draw():
        #draw ball at current position
        pass

    def move():
        #the ball moves according to its velocity
        pass

    def hit_obstacle():
        #when the ball "bounces" off an obstacle the velocity changes. Is the bottom wall hit, the function will return True
        pass

    def check_if_hit_wall():
        bottom_wall_hit = False
        #if the ball hits either the left, right or top wall it bounces back
        #if the bottom wall is hit, return True
        return bottom_wall_hit

    def gen_shape_pixmap():
        return QPixmap()
    
    def __init__(self):
        self.shape_pixmap = self.gen_shape_pixmap()


class BreakoutPaddle():             #The Object of the "Paddle"

    positionX = 50
    shape_pixmap = QPixmap

    def draw():
        #draw paddle at current position
        pass

    def move():
        #the paddle moves according to the users input
        pass

    def gen_shape_pixmap():
        return QPixmap()

    def __init__(self):
        self.shape_pixmap = self.gen_shape_pixmap



class BreakoutIcon():

    image = QPixmap
    position = {0,0}

    def GetHit():
        #The icon is hit and disappears
        pass

    def Draw():
        #Draw the Icon onto the canvas at its position
        pass

    def __init__(self, image, position):
        self.image = image
        self.position = position


#The main windows components are created and added to a widget
class MyWidget(QWidget):

    breakout_ball = BreakoutBall()
    breakout_paddle = BreakoutPaddle()
    breakout_icons = []

    def gen_main_widget(self, monitor_dimensions): #creates the main widget and background image
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        BGImageLabel = QLabel()
        BGImageLabel.height = monitor_dimensions.height
        BGImageLabel.width = monitor_dimensions.width 

        pixmap = QPixmap(get_wallpaper())
        pixmap.height = monitor_dimensions.height
        pixmap.width= monitor_dimensions.width

        BGImageLabel.setPixmap(pixmap) 

        self.setCentralWidget = BGImageLabel

    def gen_breakout_icons():
        #returns list of breakoutIcons modeled after the desktop icons located on monitor 1
        return []

    def __init__(self,monitor_dimensions):
        super().__init__()
        self.gan_main_widget(monitor_dimensions)

        self.breakout_icons = self.gen_breakout_icons()
        for icon in self.breakout_icons:
            icon.Draw()


if __name__ == "__main__":  #the main mehtod

    parser = argparse.ArgumentParser(description="Breakout Deletion Game")
    parser.add_argument('fileName', type=str, help='Name der gelöschten Datei')
    args = parser.parse_args()

    main_monitor = get_monitors()[0]        #the main monitor

    if(find_File_in_Bin(args.fileName)):      #Application is instantiated and started             
        import sys
        app = QApplication(sys.argv)            

        widget = MyWidget(main_monitor)

        widget.resize( main_monitor.width,main_monitor.height)
        widget.show()                                               #The created widget is started as a windows application

        while True:
            widget.breakout_ball.move()
            widget.breakout_ball.draw()

            #collision mit icons wird geprüft
            for icon in widget.breakout_icons:
                if widget.breakout_ball.position == icon.position:
                    #delete icon from breakout_icons
                    widget.breakout_ball.hit_obstacle()
                    
            #check if no icons are left
            if widget.breakout_icons.count == 0:
                end_game(True, args.fileName)

            widget.breakout_paddle.draw()

            bottom_wall_check = widget.breakout_ball.check_if_hit_wall()
            if bottom_wall_check:
                end_game(False,args.fileName)



            


