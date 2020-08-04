from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import sys
import random
import time
import getpass
import threading

pic_codes = {
    1 : ":/newPrefix/stone.png",
    2 : ":/newPrefix/paper.png",
    3 : ":/newPrefix/cutter.png",
    4 : ":/newPrefix/option1.png",
    5 : ":/newPrefix/option2.png",
}
user_option, comp_option = None, None


def my_function():
    pass

def Victory_Decider(o1, o2):
    if o1 == o2:
        return 2
    elif o1 == 1:
        if o2 == 2:
            return 1
        elif o2 == 3:
            return 0
    elif o1 == 2:
        if o2 == 1:
            return 0
        elif o2 == 3:
            return 1
    elif o1 == 3:
        if o2 == 1:
            return 1
        elif o2 == 2:
            return 0


def Victory_Message(code):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle(" ")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/stone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if not code:
        msg.setText("Congrats {} !\n You Won The Game".format(getpass.getuser()))
    elif code == 1:
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Computer Won The Game")
    elif code == 2:
        msg.setText("Game Tied")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


class Ui_Game_Area(object):
    def setupUi(self, Game_Area):
        Game_Area.setObjectName("Game_Area")
        Game_Area.resize(600, 600)
        Game_Area.setMinimumSize(QtCore.QSize(600, 600))
        Game_Area.setMaximumSize(QtCore.QSize(600, 600))
        Game_Area.setBaseSize(QtCore.QSize(600, 600))
        Game_Area.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/stone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Game_Area.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Game_Area)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 540, 51, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Exit_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(540, 540, 51, 51))
        self.Exit_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Exit_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_Button.setIcon(icon1)
        self.Exit_Button.setObjectName("Exit_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 0, 151, 141))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/user.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 0, 151, 141))
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/robot.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 251, 241))
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/frame.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 160, 251, 241))
        self.label_5.setPixmap(QtGui.QPixmap(":/newPrefix/frame.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 460, 51, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/stone.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 460, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/paper.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 460, 51, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/cutter.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 410, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(21)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Rock_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Rock_Button.setGeometry(QtCore.QRect(40, 460, 51, 51))
        self.Rock_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Rock_Button.setText("")
        self.Rock_Button.setIcon(icon1)
        self.Rock_Button.setObjectName("Rock_Button")
        self.Paper_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Paper_Button.setGeometry(QtCore.QRect(120, 460, 51, 51))
        self.Paper_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Paper_Button.setText("")
        self.Paper_Button.setIcon(icon1)
        self.Paper_Button.setObjectName("Paper_Button")
        self.Cut_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Cut_Button.setGeometry(QtCore.QRect(210, 460, 51, 51))
        self.Cut_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Cut_Button.setText("")
        self.Cut_Button.setIcon(icon1)
        self.Cut_Button.setObjectName("Cut_Button")
        self.User_Choice = QtWidgets.QLabel(self.centralwidget)
        self.User_Choice.setGeometry(QtCore.QRect(30, 170, 231, 221))
        self.User_Choice.setText("")
        self.User_Choice.setPixmap(QtGui.QPixmap(":/newPrefix/option1.png"))
        self.User_Choice.setScaledContents(True)
        self.User_Choice.setObjectName("User_Choice")
        self.Comp_Choice = QtWidgets.QLabel(self.centralwidget)
        self.Comp_Choice.setGeometry(QtCore.QRect(340, 170, 231, 221))
        self.Comp_Choice.setText("")
        self.Comp_Choice.setPixmap(QtGui.QPixmap(":/newPrefix/option2.png"))
        self.Comp_Choice.setScaledContents(True)
        self.Comp_Choice.setObjectName("Comp_Choice")
        Game_Area.setCentralWidget(self.centralwidget)

        self.retranslateUi(Game_Area)
        QtCore.QMetaObject.connectSlotsByName(Game_Area)

        self.Exit_Button.clicked.connect(self.Take_To_Home_Page)
        self.Rock_Button.clicked.connect(self.Option_Rock)
        self.Paper_Button.clicked.connect(self.Option_Paper)
        self.Cut_Button.clicked.connect(self.Option_Cutter)

    def Option_Rock(self):
        global pic_codes, user_option, comp_option
        user_option, comp_option = 1, random.choice([1, 2, 3])
        self.User_Choice.setPixmap(QtGui.QPixmap(pic_codes[1]))
        threading.Timer(1.5, my_function).start()
        self.Comp_Choice.setPixmap(QtGui.QPixmap(pic_codes[comp_option]))
        threading.Timer(0.5, my_function).start()
        Victory_Message(Victory_Decider(user_option,comp_option))
        self.User_Choice.setPixmap(QtGui.QPixmap(pic_codes[4]))
        self.Comp_Choice.setPixmap(QtGui.QPixmap(pic_codes[5]))

    def Option_Paper(self):
        global pic_codes, user_option, comp_option
        user_option, comp_option = 2, random.choice([1, 2, 3])
        self.User_Choice.setPixmap(QtGui.QPixmap(pic_codes[2]))
        threading.Timer(1.5, my_function).start()
        self.Comp_Choice.setPixmap(QtGui.QPixmap(pic_codes[comp_option]))
        threading.Timer(0.5, my_function).start()
        Victory_Message(Victory_Decider(user_option,comp_option))
        self.User_Choice.setPixmap(QtGui.QPixmap(pic_codes[4]))
        self.Comp_Choice.setPixmap(QtGui.QPixmap(pic_codes[5]))

    def Option_Cutter(self):
        global pic_codes, user_option, comp_option
        user_option, comp_option = 3, random.choice([1, 2, 3])
        self.User_Choice.setPixmap(QtGui.QPixmap(pic_codes[3]))
        threading.Timer(1.5, my_function).start()
        self.Comp_Choice.setPixmap(QtGui.QPixmap(pic_codes[comp_option]))
        threading.Timer(0.5, my_function).start()
        Victory_Message(Victory_Decider(user_option,comp_option))
        self.User_Choice.setPixmap(QtGui.QPixmap(pic_codes[4]))
        self.Comp_Choice.setPixmap(QtGui.QPixmap(pic_codes[5]))

    def Take_To_Home_Page(self):
        Splash_Screen.show()
        Game_Area.hide()

    def retranslateUi(self, Game_Area):
        _translate = QtCore.QCoreApplication.translate
        Game_Area.setWindowTitle(_translate("Game_Area", "Game Area"))
        self.Exit_Button.setToolTip(_translate("Game_Area", "<html><head/><body><p><span style=\" font-weight:600;\">Exit To Home Page</span></p></body></html>"))
        self.label_9.setText(_translate("Game_Area", "<html><head/><body><p><span style=\" color:#ffffff;\">Choose Your Weapon</span></p></body></html>"))
        self.Rock_Button.setToolTip(_translate("Game_Area", "<html><head/><body><p><span style=\" font-weight:600;\">Stone / Rock</span></p></body></html>"))
        self.Paper_Button.setToolTip(_translate("Game_Area", "<html><head/><body><p><span style=\" font-weight:600;\">Paper</span></p></body></html>"))
        self.Cut_Button.setToolTip(_translate("Game_Area", "<html><head/><body><p><span style=\" font-weight:600;\">Scissors</span></p></body></html>"))


class Ui_Splash_Screen(object):
    def setupUi(self, Splash_Screen):
        Splash_Screen.setObjectName("Splash_Screen")
        Splash_Screen.resize(600, 600)
        Splash_Screen.setMinimumSize(QtCore.QSize(600, 600))
        Splash_Screen.setMaximumSize(QtCore.QSize(600, 600))
        Splash_Screen.setBaseSize(QtCore.QSize(600, 600))
        Splash_Screen.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/stone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Splash_Screen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Splash_Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/splash.png"))
        self.background.setObjectName("background")
        self.Exit_Icon = QtWidgets.QLabel(self.centralwidget)
        self.Exit_Icon.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.Exit_Icon.setPixmap(QtGui.QPixmap(":/newPrefix/exit_icon.png"))
        self.Exit_Icon.setScaledContents(True)
        self.Exit_Icon.setObjectName("Exit_Icon")
        self.Exit_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(540, 10, 51, 51))
        self.Exit_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_Button.setIcon(icon1)
        self.Exit_Button.setObjectName("Exit_Button")
        self.Play_Button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Play_Button.setGeometry(QtCore.QRect(200, 440, 191, 61))
        self.Play_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Play_Button.setIcon(icon1)
        self.Play_Button.setObjectName("Play_Button")
        Splash_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash_Screen)
        QtCore.QMetaObject.connectSlotsByName(Splash_Screen)

        self.Exit_Button.clicked.connect(self.Quit_Application)
        self.Play_Button.clicked.connect(self.Take_To_Game_Room)

    def Take_To_Game_Room(self):
        global ui1
        ui1.setupUi(Game_Area)
        Game_Area.show()
        Splash_Screen.hide()

    def Quit_Application(self):
        app.quit()

    def retranslateUi(self, Splash_Screen):
        _translate = QtCore.QCoreApplication.translate
        Splash_Screen.setWindowTitle(_translate("Splash_Screen", "Stone Paper Scissor"))
        self.Exit_Button.setToolTip(_translate("Splash_Screen", "<html><head/><body><p><span style=\" font-weight:600;\">Exit Game</span></p></body></html>"))
        self.Play_Button.setToolTip(_translate("Splash_Screen", "<html><head/><body><p><span style=\" font-weight:600;\">Play The Game</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    Game_Area = QtWidgets.QMainWindow()
    ui1 = Ui_Game_Area()

    Splash_Screen = QtWidgets.QMainWindow()
    ui = Ui_Splash_Screen()
    ui.setupUi(Splash_Screen)
    
    Splash_Screen.show()
    sys.exit(app.exec_())

#