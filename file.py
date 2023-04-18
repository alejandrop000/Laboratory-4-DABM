import csv
import os

class Sensor:
    def register(values):
        cwd = os.getcwd()
        ruta = cwd + "/archivos/"
        ruta = ruta + "/values.csv"

        with open(ruta, "w", newline="" ) as file:  #mode w: write
            writer = csv.writer(file, delimiter=",")
            writer.writerow(values)
    
    def lecture():
        cwd = os.getcwd()
        ruta = cwd + "/archivos/"
        ruta = ruta + "/values.csv"
        with open(ruta, "r") as file: #mode r: read
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                return row