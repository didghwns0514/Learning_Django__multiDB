from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from StoreScript.Scripts.Sqlite.SqliteOP import SQlite
from StoreScript.Scripts.Flask.app import clsFlask


class Ui_Dialog(object):

	STRING_LEN = 10

	def setupUi(self, Form):
		"""
		setting up Ui_dialog UI
		"""
		Form.setObjectName("Form")
		Form.resize(453, 352)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(Form)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.lineEditEmail = QtWidgets.QLineEdit(Form)
		self.lineEditEmail.setObjectName("lineEditEmail")
		self.horizontalLayout.addWidget(self.lineEditEmail)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_2.addWidget(self.label_2)
		self.lineEditPassword = QtWidgets.QLineEdit(Form)
		self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEditPassword.setObjectName("lineEditPassword")
		self.horizontalLayout_2.addWidget(self.lineEditPassword)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setObjectName("pushButton")
		self.pushButton_createID = QtWidgets.QPushButton(Form)
		self.pushButton_createID.setObjectName("pushButton_createId")

		#clicked signal of the button connected to login method
		self.pushButton.clicked.connect(self.login)
		self.pushButton_createID.clicked.connect(self.create_id)

		self.verticalLayout.addWidget(self.pushButton)
		self.labelResult = QtWidgets.QLabel(Form)
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.labelResult.setFont(font)
		self.labelResult.setText("")
		self.labelResult.setObjectName("labelResult")
		self.verticalLayout.addWidget(self.labelResult)
		self.verticalLayout_2.addLayout(self.verticalLayout)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def create_id(self):
		"""
		method for creatind id, under sqlite3 database
		"""
		pass


	def login(self):
		"""
		method for login, we have connected this with the clicked signal of button
		"""
		try:
			email = self.lineEditEmail.text()
			password = self.lineEditPassword.text()

			# @ run flask
			clsFlask._runProcess()

			if clsFlask.LOGGED:


			else:
				self.labelResult.setText("You are not logged - check Flask")


			if result == None:
				self.labelResult.setText("Incorrect Email & Password")

			else:
				self.labelResult.setText("You are logged in")
				mydialog = QDialog()
				mydialog.setModal(True)
				mydialog.exec()


		except mc.Error as e:
			self.labelResult.setText("Error")


	def retranslateUi(self, Form):
		"""
		setting texts for Qt objects in the class
		"""
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label.setText(_translate("Form", "Email:".ljust(Ui_Dialog.STRING_LEN)))
		self.label_2.setText(_translate("Form", "Password:".ljust(Ui_Dialog.STRING_LEN)))
		self.pushButton.setText(_translate("Form", "Login"))
		self.pushButton_createID.setText(_translate("Form", "Create ID"))