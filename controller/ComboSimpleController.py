from PyQt5 import QtWidgets, uic

class ComboSimpleController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmcombosimple.ui")
        self.ventana.show()
        app.exec()
        