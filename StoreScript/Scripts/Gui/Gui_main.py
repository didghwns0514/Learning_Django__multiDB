import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

from mainwindow_ui import Ui_MainWindow
from dialog_ui     import Ui_Dialog

class MyDialog(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

class MyWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		centralWidget = QWidget()
		self.setCentralWidget(centralWidget)
		gridLayout = QGridLayout(centralWidget)
		gridLayout.addWidget(self.ui.label,      0, 0, alignment=Qt.AlignCenter)
		gridLayout.addWidget(self.ui.pushButton, 1, 0)

	def dialogbox(self):
		#self.hide()
		self.myDialog = MyDialog()
		self.myDialog.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MyWindow()
	w.show()
	sys.exit(app.exec_())