from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QBrush, QColor, QFont, QPen, QPolygonF
from PyQt6.QtWidgets import (
    QGraphicsPolygonItem,
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
    QWidget,
)
from PyQt6.uic import loadUi


class PlayerItem(QGraphicsPolygonItem):
    """Représente un joueur sur le terrain avec un hexagone et un texte centré."""

    def __init__(self, x, y, color="#FFB6C1", size=10, text=None):
        super().__init__()

        # Définir les points pour l'hexagone
        points = [
            QPointF(0, -size),  # Haut
            QPointF(size, -size / 2),  # Haut-Droit
            QPointF(size, size / 2),  # Bas-Droit
            QPointF(0, size),  # Bas
            QPointF(-size, size / 2),  # Bas-Gauche
            QPointF(-size, -size / 2),  # Haut-Gauche
        ]

        # Appliquer les points à l'hexagone
        polygon = QPolygonF(points)
        self.setPolygon(polygon)
        self.setBrush(
            QBrush(QColor(color))
        )  # Appliquer la couleur via le code hexadécimal
        self.setPen(QPen(Qt.PenStyle.NoPen))  # Pas de bordure
        self.setFlag(
            QGraphicsPolygonItem.GraphicsItemFlag.ItemIsMovable
        )  # Déplacement autorisé
        self.setPos(x, y)

        # Ajouter du texte centré sur l'hexagone
        if text is not None:
            self.text_item = QGraphicsTextItem(text, self)  # Créer l'élément de texte
            self.text_item.setFont(QFont("Arial", 12))  # Police du texte
            self.text_item.setDefaultTextColor(
                QColor(0, 0, 0)
            )  # Couleur du texte (noir)

            # Centrer le texte
            text_rect = (
                self.text_item.boundingRect()
            )  # Rectangle de délimitation du texte
            text_x = -text_rect.width() / 2  # Décalage horizontal pour centrer
            text_y = -text_rect.height() / 2  # Décalage vertical pour centrer
            self.text_item.setPos(
                x + text_x, y + text_y
            )  # Positionner le texte centré sur l'hexagone


class Pitch(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("MyQtApp/ui/pitch.ui", self)  # Charge l'UI

        # Vérifie si l'objet graphicsView existe
        if not hasattr(self, "graphicsView"):
            raise AttributeError(
                "L'élément QGraphicsView 'graphicsView' n'a pas été trouvé dans pitch.ui"
            )

        # Initialisation de la scène graphique
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)  # Associe la scène à la view
        self.scene.setSceneRect(0, 0, 800, 500)

        # Charger une image de terrain de foot (ajuste le chemin si besoin)
        from PyQt6.QtGui import QPixmap
        from PyQt6.QtWidgets import QGraphicsPixmapItem

        field = QGraphicsPixmapItem(QPixmap("MyQtApp/assets/pitch.png"))
        self.scene.addItem(field)

        # Positions des joueurs
        positions = [
            (400, 450),
            (200, 350),
            (600, 350),
            (100, 250),
            (400, 250),
            (700, 250),
            (200, 150),
            (600, 150),
            (300, 80),
            (500, 80),
            (400, 30),
        ]

        # Couleur et taille du gardien
        goalkeeper_color = "#306957"
        goalkeeper_size = 20

        # Couleur et taille des autres joueurs
        player_color = "#82c1ad"
        player_size = 20

        for i, pos in enumerate(positions):

            if i == 0:
                player = PlayerItem(
                    pos[0],
                    pos[1],
                    color=goalkeeper_color,
                    size=goalkeeper_size,
                    text="GB",
                )
            else:
                player = PlayerItem(
                    pos[0], pos[1], color=player_color, size=player_size
                )

            self.scene.addItem(player)
