from PyQt5.QtWidgets import *
from stokEkrani_python import Ui_MainWindow
from veritabani import Veritabani

class stokSayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.StkSayfa = Ui_MainWindow()
        self.StkSayfa.setupUi(self)
        self.veritabani = Veritabani()
        self.KayitlariListele()
        self.StkSayfa.pBEkle.clicked.connect(self.kaydet)
        self.StkSayfa.pBSil.clicked.connect(self.kayitSil)
        
 #----------------------------------------------------------------------------------------------------       
    def kaydet(self):
        u_code = self.StkSayfa.cmStokkod.currentText()
        u_renk = self.StkSayfa.cmStokRenk.currentText()
        u_olcu = self.StkSayfa.cmStokolcu.currentText()
        u_aciklama = self.StkSayfa.textEditS_aciklama.toPlainText()
        s_sayi = int(self.StkSayfa.lnstokSayi.text())
        stok_kayıt =self.veritabani.stok_kayit(u_code,u_renk,u_olcu,u_aciklama,s_sayi,)
        self.KayitlariListele() 
        if(stok_kayıt):
            print("Kayit Başarılı")
        else:
            print("Kayit Ekleme Başarısız.")
            
    #----------------------------------------------------------------------------------------------------
    def kayitSil(self):
            try:
                self.veritabani.veritabaniac()
                secili_satir = self.StkSayfa.tableWidget.currentRow()
                if secili_satir != -1: 
                    siparisID = self.StkSayfa.tableWidget.item(secili_satir, 0).text()
                    self.veritabani.kayitSil(siparisID)
                    self.StkSayfa.statusbar.showMessage("Sipariş Silme İşlemi Başarılı.", 4000)
                    self.KayitlariListele() 
                else :
                    self.StkSayfa.statusbar.showMessage("Lütfen bir sipariş seçiniz.", 4000)
            except Exception as error:
                self.StkSayfa.statusbar.showMessage("Sipariş Silme İşlemi Başarısız. Hata: " + str(error), 6000)
            finally:
                self.veritabani.veritabanikapat()
#----------------------------------------------------------------------------------------------------
    def KayitlariListele(self):
        try:
            self.StkSayfa.tableWidget.clear()
            # self.StkSayfa.tableWidget.setColumnWidth(0,60) kolon boşluğu ayarlama.
            self.StkSayfa.tableWidget.setColumnWidth(3,200)
            kolonlar = ["Product Code","Product Color","Product Size","Product Description","Total Product"]
            self.StkSayfa.tableWidget.setHorizontalHeaderLabels(kolonlar)
            veriler = self.veritabani.KayitListele()
            
            satirsayisi = 0
            if veriler!=False:
                
                self.StkSayfa.tableWidget.setRowCount(len(veriler))
                for veri in veriler:
                    self.StkSayfa.tableWidget.setItem(int(satirsayisi),0,QTableWidgetItem(str(veri[0])))
                    self.StkSayfa.tableWidget.setItem(int(satirsayisi),1,QTableWidgetItem(str(veri[1])))
                    self.StkSayfa.tableWidget.setItem(int(satirsayisi),2,QTableWidgetItem(str(veri[2])))
                    self.StkSayfa.tableWidget.setItem(int(satirsayisi),3,QTableWidgetItem(str(veri[3])))
                    self.StkSayfa.tableWidget.setItem(int(satirsayisi),4,QTableWidgetItem(str(veri[4])))
                    
                    satirsayisi +=1

        except Exception as error : 
            print("Hata ==>> " + str(error))
    #----------------------------------------------------------------------------------------------------
