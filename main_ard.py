from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton,QDial
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont
import serial, struct, sys

class SerialPort:
    def __init__(self,port,baudrate):
        self.serial_port = serial.Serial()
        self.port = port
        self.baudrate = baudrate

    def open(self):
        if not self.serial_port.is_open:
            self.serial_port.port = self.port
            self.serial_port.baudrate = self.baudrate
            self.serial_port.open()

    def is_open(self):
        return self.serial_port.is_open
    
    def close(self):
        if self.is_open():
            self.serial_port.close()
    def read_data(self):
        return self.serial_port.readline().decode().strip()

    def write_data(self,data):
        self.serial_port.write(struct.pack(">B",data))

class MainArduino(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Arduino System")
        self.setMinimumWidth(500)
        self.setMinimumHeight(270)
        self.setMaximumHeight(270)
        self.setMaximumWidth(500)
        self.setGeometry(500,250,500,270)
        #Banner
        self.label_image = QLabel(self)
        self.label_image.setGeometry(0,0,500,48)
        pixmap = QPixmap("Files/banner.png")
        self.label_image.setPixmap(pixmap)

        self.backg = QLabel(self)
        self.backg.setGeometry(0,52,500,330)
        pixmap_back = QPixmap("Files/fondo.jpg")
        self.backg.setPixmap(pixmap_back)

        #Valor máximo del sensor
        self.max_label = QLabel("Maximum value",self)
        self.max_label.setGeometry(40,70,85,20)
        self.maximum = QLineEdit(self)
        self.maximum.setFont(QFont("Arial",10))
        self.maximum.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.maximum.setGeometry(40,90,85,30)

        #Valor mínimo del sensor
        self.min_label = QLabel("Minimum value",self)
        self.min_label.setGeometry(40,130,85,20)
        self.minimum = QLineEdit(self)
        self.minimum.setFont(QFont("Arial",10))
        self.minimum.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.minimum.setGeometry(40,150,85,30)  

        #Mostrar lecutra de sensor
        self.title_data = QLabel("Sent data",self)
        self.title_data.setGeometry(180,70,80,20)
        self.dataval = QLineEdit(self)
        self.dataval.setReadOnly(True)
        self.dataval.setFont(QFont("Arial",10))
        self.dataval.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.dataval.setGeometry(160,90,90,30) 

        #Boton de lectura
        self.btn_read = QPushButton("Start",self)
        self.btn_read.setGeometry(40,190,85,30)
        self.btn_read.clicked.connect(self.read_data)      

        #Botón de LOGOUT
        self.btn_logout = QPushButton("Log Out",self)
        self.btn_logout.setGeometry(415,10,60,30)
        self.btn_logout.clicked.connect(self.logout)

        #Dial PWM
        self.dial = QDial(self)
        self.dial.setMaximum(100)
        self.dial.setGeometry(320,90,70,70)
        self.dial.valueChanged.connect(self.dial_change)
        self.label_data = QLineEdit(self)
        self.label_data.setReadOnly(True)
        self.label_data.setText("PWM: 0")
        self.label_data.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_data.setGeometry(320,180,70,30)

        #Boton de stop
        self.btn_stop = QPushButton("Stop",self)
        self.btn_stop.setGeometry(320,220,70,30)
        self.btn_stop.clicked.connect(self.stop) 

    def dial_change(self):
        port.open()
        if port.is_open():
            get_value = self.dial.value()
            self.label_data.setText("PWM: " + str(get_value))
            self.label_data.setAlignment(Qt.AlignmentFlag.AlignCenter)

            valor = int(255*int(get_value)/100)
            port.write_data(valor)

    def read_data(self):
        min = int(self.minimum.text())
        max = int(self.maximum.text())
        port.open()
        if port.is_open():
            data = int(port.read_data())
            if data < min:
                data = min
            if data > max:
                data = max
            else:
                data = data
            data = int((max - data) * 255 / (max - min))    
            self.dataval.setText(str(data))
            self.dataval.setAlignment(Qt.AlignmentFlag.AlignCenter)
            port.write_data(data)
        port.close()

    def stop(self):
        self.label_data.setText("PWM: 0")
        self.dial.setValue(0)
        port.close()

    def logout(self):
        self.close()

port = SerialPort("COM3",9600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainArduino()
    main_window.show()
    sys.exit(app.exec())