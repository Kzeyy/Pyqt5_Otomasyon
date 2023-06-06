from PyQt5.QtWidgets import *
from anasayfa_python import Ui_MainWindow
from siparisekle import siparisSayfasi
from stokEkrani import stokSayfasi
from veritabani import Veritabani

class AnaSayfa(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anapencere = Ui_MainWindow()
        self.anapencere.setupUi(self)
        self.veritabani = Veritabani()
        self.siparisSayfasiAc = siparisSayfasi()
        self.siparisSayfasiAc.kayitlisiparislistele()

        self.anapencere.pBEklemeSayfas.clicked.connect(self.SiparisSayfa)
        self.stoksayfasiac = stokSayfasi()
        self.anapencere.pBStokSayfas.clicked.connect(self.StokSayfa)
        self.anapencere.pBsiparisSIL.clicked.connect(self.anaekrankayitsil)
    def SiparisSayfa(self):
        self.siparisSayfasiAc.show()
        self.siparisSayfasiAc.kayitlisiparislistele()
        self.anapencere.tableWidget.setColumnWidth(0,40)
        self.anapencere.tableWidget.setColumnWidth(3,180)
        self.anapencere.tableWidget.setColumnWidth(4,75)
        self.anapencere.tableWidget.setColumnWidth(5,75)
        self.anapencere.tableWidget.setColumnWidth(6,75)
        self.anapencere.tableWidget.setColumnWidth(7,180)
        self.anapencere.tableWidget.setColumnWidth(8,75)
        veriler = self.veritabani.siparisEkraniList()
        self.siparisSayfasiAc.kayitlisiparislistele()
        satirsayisi = 0
        if veriler!=False :
            self.anapencere.tableWidget.clear()
            self.anapencere.tableWidget.setRowCount(len(veriler))
            for veri in veriler :
                self.anapencere.tableWidget.setItem(int(satirsayisi),0,QTableWidgetItem(str(veri[0])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),1,QTableWidgetItem(str(veri[1])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),2,QTableWidgetItem(str(veri[2])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),3,QTableWidgetItem(str(veri[3])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),4,QTableWidgetItem(str(veri[4])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),5,QTableWidgetItem(str(veri[5])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),6,QTableWidgetItem(str(veri[6])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),7,QTableWidgetItem(str(veri[7])))
                self.anapencere.tableWidget.setItem(int(satirsayisi),8,QTableWidgetItem(str(veri[8])))

                satirsayisi +=1
        kolonlar = ["ID","Name FirstName","Phone","Address","Product Code","Product Color","Product Size","Product Description","Total Product"]
        self.anapencere.tableWidget.setHorizontalHeaderLabels(kolonlar)
        self.siparisSayfasiAc.kayitlisiparislistele()
    def anaekrankayitsil(self):
        try:
            self.veritabani.veritabaniac()
            secili_satir = self.anapencere.tableWidget.currentRow()
            if secili_satir != -1: 
                siparisID = self.anapencere.tableWidget.item(secili_satir, 0).text()
                self.veritabani.kayitSil(siparisID)
                self.anapencere.statusbar.showMessage("Sipariş Silme İşlemi Başarılı.", 4000)
                self.stoksayfasiac.KayitlariListele()
            else :
                    self.anapencere.statusbar.showMessage("Lütfen bir sipariş seçiniz.", 4000)
        except Exception as error:
            self.anapencere.statusbar.showMessage("Sipariş Silme İşlemi Başarısız. Hata: " + str(error), 6000)
        finally:
            self.veritabani.veritabanikapat()
#-------------------------------------------------
    def StokSayfa(self):
        self.stoksayfasiac.show()
    