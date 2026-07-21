from PySide6.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)

window = QWidget()

window.resize(
    500,
    500
)

window.show()

sys.exit(
    app.exec()
)