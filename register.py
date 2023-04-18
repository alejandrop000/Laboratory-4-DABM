#from main import LoginWindow
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QPixmap, QFont
import sys, csv

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Register")
        self.setMinimumWidth(500)
        self.setMinimumHeight(340)
        self.setMaximumHeight(340)
        self.setMaximumWidth(500)
        self.setGeometry(500,250,500,330)

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
        self.label_title.setGeometry(195,70,180,20)
    
        #Texto Usuario
        # self.label_username = QLabel("Username",self)
        # self.label_username.setFont(QFont("Arial",9))
        # self.label_username.setGeometry(225,80,60,20)
        #Box para escribir usuario
        self.edit_username = QLineEdit(self)
        self.edit_username.setClearButtonEnabled(True)
        self.edit_username.setPlaceholderText("Username")
        self.edit_username.setFont(QFont("Arial",10))
        self.edit_username.setGeometry(175,100,155,40)

        #Texto Contraseña
        # self.label_password = QLabel("Password",self)
        # self.label_password.setFont(QFont("Arial",9))
        # self.label_password.setGeometry(225,145,60,20)
        #Box para escribir contraseña
        self.edit_password = QLineEdit(self)
        self.edit_password.setClearButtonEnabled(True)
        self.edit_password.setPlaceholderText("Password")
        self.edit_password.setFont(QFont("Arial",10))
        self.edit_password.setGeometry(175,155,155,40)
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        
        #Texto Contraseña Confirmación
        # self.label_confirm = QLabel("Confirm Password",self)
        # self.label_confirm.setFont(QFont("Arial",9))
        # self.label_confirm.setGeometry(200,210,110,20)
        #Box para escribir confirmación
        self.edit_confirm = QLineEdit(self)
        self.edit_confirm.setGeometry(175,210,155,40)
        self.edit_confirm.setPlaceholderText("Confirm Password")
        self.edit_confirm.setFont(QFont("Arial",10))        
        self.edit_confirm.setClearButtonEnabled(True)
        self.edit_confirm.setEchoMode(QLineEdit.EchoMode.Password)
        
        #Botón para terminar
        self.btn_save = QPushButton("Finish",self)
        self.btn_save.setStyleSheet("background-color: lightblue")
        self.btn_save.setFont(QFont("Arial",9))
        self.btn_save.setGeometry(175,285,77,35)
        self.btn_save.clicked.connect(self.save)

        #Botón para retornar
        self.btn_return = QPushButton("Return",self)
        self.btn_return.setFont(QFont("Arial",9))
        self.btn_return.setGeometry(255,285,77,35)
        self.btn_return.clicked.connect(self.finish)

        self.fields_msg = QLabel(self)
        self.fields_msg.setGeometry(175,260,200,20)

        self.passw_msg = QLabel(self)
        self.passw_msg.setGeometry(175,260,236,20)

        self.exist_msg = QLabel(self)
        self.exist_msg.setGeometry(175,260,190,20)   

    def finish(self):
        self.close()

    def save(self):
        username = self.edit_username.text()
        password = self.edit_password.text()
        password2 = self.edit_confirm.text()
        values = []
        users = []

        m = 1
        if username == "" or password == "" or password2 == "":
            self.passw_msg.setText("")
            self.passw_msg.setStyleSheet("")
            self.exist_msg.setText("")
            self.exist_msg.setStyleSheet("")           
            self.fields_msg.setText("Some fields are still empty. Try again.")
            self.fields_msg.setStyleSheet("background-color: orange")
            m = 0

        with open("Files/usuarios.csv", newline="") as csvfile:
            reader = csv.reader(csvfile,delimiter=",")
            data = [row for row in reader]
            for i in range (len(data)):
                users.append(data[i][0])    

        x = 1
        for i in range(len(users)):
            if username == users[i]:
                x = 0

        if password == password2 and x != 0 and m == 1:
            values.append(username)
            values.append(password)
            values.append("Usuario")

            myFile = open("Files/usuarios.csv","a",newline="")
            writer = csv.writer(myFile)
            writer.writerow(values)
            myFile.close()

            self.passw_msg.setText("")
            self.passw_msg.setStyleSheet("")
            self.exist_msg.setText("")
            self.exist_msg.setStyleSheet("")
            self.fields_msg.setText("")
            self.fields_msg.setStyleSheet("")                        
            QMessageBox.information(self, "Done",
            "User has been created succesfully",
            QMessageBox.StandardButton.Close)
            self.close()

        elif password != password2 and x != 0 and m == 1:
            self.exist_msg.setText("")
            self.exist_msg.setStyleSheet("")
            self.passw_msg.setText("Passwords don´t match each other. Try again.")
            self.passw_msg.setStyleSheet("background-color: orange")
        
        elif m == 1:
            self.passw_msg.setText("")
            self.passw_msg.setStyleSheet("")
            self.exist_msg.setText("")
            self.exist_msg.setStyleSheet("")            
            self.exist_msg.setText("Username already exists. Try again.")
            self.exist_msg.setStyleSheet("background-color: orange")


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    register_window = RegisterWindow()
    register_window.show()
    sys.exit(app.exec())