import sys
from UI import Ui_MainWindow
from PyQt5 import QtCore, QtMultimedia, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for btn in self.buttons.buttons():
            btn.clicked.connect(self.play_sound)

    def play_sound(self):
        note = self.sender().text()
        media = QtCore.QUrl.fromLocalFile(f'sounds/{note}.wav')
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 49:
            self.doo.click()
        if event.key() == 50:
            self.re.click()
        if event.key() == 51:
            self.mi.click()
        if event.key() == 52:
            self.fa.click()
        if event.key() == 53:
            self.sol.click()
        if event.key() == 54:
            self.lya.click()
        if event.key() == 55:
            self.si.click()


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec_())
