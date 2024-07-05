import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Contoh Aplikasi PyQt')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('Masukkan Nama Anda:', self)
        layout.addWidget(self.label)

        self.textbox = QLineEdit(self)
        layout.addWidget(self.textbox)

        self.combobox = QComboBox(self)
        self.combobox.addItem('Pilihan 1')
        self.combobox.addItem('Pilihan 2')
        self.combobox.addItem('Pilihan 3')
        layout.addWidget(self.combobox)

        self.button = QPushButton('Tampilkan Pesan', self)
        self.button.clicked.connect(self.showMessage)
        layout.addWidget(self.button)

        self.setLayout(layout)
    
    def showMessage(self):
        name = self.textbox.text()
        choice = self.combobox.currentText()
        QMessageBox.information(self, 'Pesan', f'Nama: {name}\nPilihan: {choice}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
