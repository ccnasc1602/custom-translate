import os, sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog
print(os.path.join(os.getcwd()))
from utils.translations.translate import gettex as _


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('workspace/gui/login.ui', self)

        # Configutations
        self.label_user.setText(_('Usuário'))
        self.label_password.setText(_('Senha:'))
        self.pushButton_login.setText(_('Acessar'))
        self.pushButton_logout.setText(_('Sair'))

        # Conections
        self.pushButton_login.clicked.connect(self.button_login_clicked)
        self.pushButton_logout.clicked.connect(self.button_logout_clicked)

        self.show()

    def button_login_clicked(self):
        print(self.lineEdit_user.text())
        print(self.lineEdit_password.text())

    def button_logout_clicked(self):
        sys.exit()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    L = Login()
    sys.exit(app.exec_())