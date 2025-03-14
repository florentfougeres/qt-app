# Standard
import sys

from PyQt6.QtGui import QIcon

# Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from qt_material import apply_stylesheet

# App
from MyQtApp.__init__ import DIR_PLUGIN_ROOT
from MyQtApp.ui.dialog import MyDialog
from MyQtApp.ui.pitch import Pitch


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print(str(DIR_PLUGIN_ROOT))
        loadUi("MyQtApp/ui/mainwindow.ui", self)
        self.actionMyDialog.triggered.connect(self.open_dialog)
        self.setWindowTitle("My Qt App")
        self.setWindowIcon(QIcon(str(DIR_PLUGIN_ROOT / "ressources/images/icon.svg")))
        self.pitch = Pitch()
        self.main_layout.addWidget(self.pitch)
        self.update()

    def open_dialog(self):
        dialog = MyDialog(self)
        dialog.exec()


def main():
    app = QApplication(sys.argv)
    ##apply_stylesheet(app, theme="dark_teal.xml")
    apply_stylesheet(app, theme="light_teal.xml")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
