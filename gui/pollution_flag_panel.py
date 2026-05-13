"""
gui/pollution_flag_panel.py
---------------------------
Panel for pollution flagging. Placeholder — to be implemented.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class PollutionFlagPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        label = QLabel("Pollution Flag Panel — coming soon.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

    def load_data(self, data):
        pass
