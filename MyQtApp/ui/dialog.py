from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Charger l'UI directement depuis le fichier .ui
        loadUi("MyQtApp/ui/dialog.ui", self)
        self.setWindowTitle("My Duialog")

        # Connecter les événements du bouton
        self.my_button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.my_button.setText("Vous avez cliqué !")
