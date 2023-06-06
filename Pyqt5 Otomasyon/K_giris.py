from PyQt5.QtWidgets import *
from K_giris_python import Ui_Form
from anasayfa import AnaSayfa

class KgirisSayfasi(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.Kgiris = Ui_Form()
        self.Kgiris.setupUi(self)
        self.anapencereAc = AnaSayfa()
        self.Kgiris.pushButtongiris.clicked.connect(self.GirisYap)
    def GirisYap(self):
        kad = self.Kgiris.lnad.text()
        ksifre = self.Kgiris.lnsifre.text()
        if kad == "" and ksifre == "":
            self.close()
            self.anapencereAc.show()
        else : 
            QMessageBox.warning(self,"Bilgi "," Kullanıcı Adı veya Şifrenizi Yanlış Girdiniz.",QMessageBox.Ok)