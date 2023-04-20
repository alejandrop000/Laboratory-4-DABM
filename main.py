from main_ard import MainArduino
from register import RegisterWindow
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap, QFont
import sys, csv

#La clase hereda de QWidget
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("DABM Lab 3")
        
        self.setMinimumWidth(500)
        self.setMinimumHeight(320)
        self.setMaximumHeight(500)
        self.setMaximumWidth(320)
        self.setGeometry(500,250,500,300)

        self.label_image = QLabel(self)
        self.label_image.setGeometry(0,0,500,48)
        pixmap = QPixmap("Files/banner.png")
        self.label_image.setPixmap(pixmap)

        self.backg = QLabel(self)
        self.backg.setGeometry(0,52,500,330)
        pixmap_back = QPixmap("Files/fondo.jpg")
        self.backg.setPixmap(pixmap_back)

        self.label_title = QLabel("DABM System",self)
        self.label_title.setFont(QFont("Arial",12))
        self.label_title.setStyleSheet("font-weight: bold")
        self.label_title.setGeometry(195,65,180,20)

        #Box para escribir usuario
        self.edit_username = QLineEdit(self)
        self.edit_username.setGeometry(175,100,155,40)
        self.edit_username.setPlaceholderText("Username")
        self.edit_username.setFont(QFont("Arial",10))
        self.edit_username.setClearButtonEnabled(True)
        
        #Box para escribir contraseña
        self.edit_password = QLineEdit(self)
        self.edit_password.setGeometry(175,160,155,40)
        self.edit_password.setPlaceholderText("Password")
        self.edit_password.setFont(QFont("Arial",10))
        self.edit_password.setClearButtonEnabled(True)
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        #Mostrar contraseña
        self.show_password = QCheckBox("Show password",self)
        self.show_password.setGeometry(175,210,100,20)
        self.show_password.toggled.connect(self.show_pass)

        self.message = QLabel(self)
        self.message.setGeometry(175,232,228,20)
        
        #Botón para ingresar
        self.btn_ingresar = QPushButton("Log In",self)
        self.btn_ingresar.setStyleSheet("background-color: lightblue")
        self.btn_ingresar.setFont(QFont("Arial",9))
        self.btn_ingresar.setGeometry(175,260,77,35)
        self.btn_ingresar.clicked.connect(self.auth)

        #Botón para registrar
        self.btn_registrar = QPushButton("Sign Up",self)
        self.btn_registrar.setFont(QFont("Arial",9))
        self.btn_registrar.setGeometry(255,260,77,35)
        self.btn_registrar.clicked.connect(self.register)
        
    def show_pass(self,clicked):
        if clicked:
            self.edit_password.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.edit_password.setEchoMode(
                QLineEdit.EchoMode.Password
            )        

    def register(self):
        #self.close()
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.edit_username.setText("")
        self.edit_password.setText("")
        self.message.setText("")
        self.message.setStyleSheet("")
            
    def auth(self):
        username = self.edit_username.text()
        password = self.edit_password.text()
        user = []
        passw = []
        with open("Files/usuarios.csv", newline="") as csvfile:
            reader = csv.reader(csvfile,delimiter=",")
            data = [row for row in reader]
            for i in range (len(data)):
                user.append(data[i][0])
                passw.append(data[i][1])
        x = 0
        for i in range (len(user)):
            if user[i] == username:
                x = 1
                if passw[i] == password:
                    self.main_window = MainArduino()
                    self.main_window.show()
                    self.edit_username.setText("")
                    self.edit_password.setText("")
                    self.message.setText("")
                    self.message.setStyleSheet("")
                else:
                    self.message.setText("Incorrect password or username. Try again.")
                    self.message.setStyleSheet("background-color: orange")
                    self.edit_username.setText("")
                    self.edit_password.setText("")
        if x == 0:
            self.message.setText("Incorrect password or username. Try again.")
            self.message.setStyleSheet("background-color: orange")
            self.edit_username.setText("")
            self.edit_password.setText("")        

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
