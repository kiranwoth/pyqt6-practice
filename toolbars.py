import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar,
    QCheckBox, QMenuBar, QVBoxLayout
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
        

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("bug.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        toolbar.addSeparator()
        toolbar.addWidget(QLabel("NEW GAME:"))
        easy_mode = QAction(QIcon("smiley.png"), "Easy", self)
        normal_mode = QAction(QIcon("smiley-neutral.png"), "Normal", self)
        expert_mode = QAction(QIcon("smiley-evil.png"), "Expert", self)
        toolbar.addAction(easy_mode)
        toolbar.addAction(normal_mode)
        toolbar.addAction(expert_mode)

        self.setStatusBar(QStatusBar(self))


    def onMyToolBarButtonClick(self, s):
        print("click", s)
        self.vb.addWidget(QLabel("Hi"))


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()