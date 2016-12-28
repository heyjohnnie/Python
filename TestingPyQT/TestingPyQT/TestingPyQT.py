import sys
#The basic GUI widgets are located in the QtGui module.
from PyQt4 import QtGui

def main():
    #Every PyQt4 application must create an application object.
    #The application object is located in the QtGui module.
    #The sys.argv parameter is a list of arguments from the command line.
    app = QtGui.QApplication(sys.argv)

    #The QtGui.QWidget widget is the base class of all user interface objects in PyQt4.
    #We provide the default constructor for QtGui.QWidget.
    #The default constructor has no parent.
    #A widget with no parent is called a window.
    root = QtGui.QWidget()

    #The resize() method resizes the widget. It is 250px wide and 150px high.
    root.resize(250, 150)

    #The move() method moves the widget to a position on the screen at x=300 and y=300 coordinates.
    root.move(300, 300)

    #Here we set the title for our window. The title is shown in the titlebar.
    root.setWindowTitle("Simple")

    #The show() method displays the widget on the screen.
    #A widget is first created in memory and later shown on the screen.
    root.show()

    #The mainloop ends if we call the exit() method or the main widget is destroyed.
    #The sys.exit() method ensures a clean exit.
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()