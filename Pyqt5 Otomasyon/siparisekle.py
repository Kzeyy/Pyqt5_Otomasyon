from PyQt5.QtWidgets import *
from siparisekle_python import Ui_MainWindow
from veritabani import Veritabani

class siparisSayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.Ssayfasi = Ui_MainWindow()
        self.Ssayfasi.setupUi(self)
        self.veritabani = Veritabani()
        self.kayitlisiparislistele()
        
        
        self.Ssayfasi.pBEkle.clicked.connect(self.siparisEkle)
        self.Ssayfasi.pBsiparisSIL.clicked.connect(self.siparis_sil)
    def siparisEkle(self):
        try:
            self.veritabani.veritabaniac()
            m_Adsoyad = self.Ssayfasi.lnadsoyad.text()
            m_tlf = int(self.Ssayfasi.lntlf.text())
            m_adres = self.Ssayfasi.textEditAdress.toPlainText()
            u_code = self.Ssayfasi.cmSipariskod.currentText()
            u_renk = self.Ssayfasi.cmSiparisRenk.currentText()
            u_olcu = self.Ssayfasi.cmSiparisolcu.currentText()
            s_aciklama = self.Ssayfasi.textEditS_aciklama.toPlainText()
            s_fiyat = int(self.Ssayfasi.lnSiparisSayi.text())
            siparisKayit =self.veritabani.siparis_kayit(m_Adsoyad,m_tlf,m_adres,u_code,u_renk,u_olcu,s_aciklama,s_fiyat)
            self.kayitlisiparislistele()
            if (siparisKayit):
                pass
            self.Ssayfasi.statusbar.showMessage(" Sipariş Kayıt İşlemi Başarılı. ",4000)
        except Exception as error : 
            self.Ssayfasi.statusbar.showMessage("Sipariş Kayıt İşlemi Başarız. Hata " + str(error),600000)
        finally:
            self.veritabani.veritabanikapat()
    
    def kayitlisiparislistele (self):
        self.Ssayfasi.siparistablosu.setColumnWidth(0,40)
        self.Ssayfasi.siparistablosu.setColumnWidth(3,180)
        self.Ssayfasi.siparistablosu.setColumnWidth(4,75)
        self.Ssayfasi.siparistablosu.setColumnWidth(5,75)
        self.Ssayfasi.siparistablosu.setColumnWidth(6,75)
        self.Ssayfasi.siparistablosu.setColumnWidth(7,180)
        self.Ssayfasi.siparistablosu.setColumnWidth(8,75)
        veriler = self.veritabani.siparisEkraniList()
        satirsayisi = 0
        if veriler!=False :
            self.Ssayfasi.siparistablosu.clear()
            self.Ssayfasi.siparistablosu.setRowCount(len(veriler))
            for veri in veriler :
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),0,QTableWidgetItem(str(veri[0])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),1,QTableWidgetItem(str(veri[1])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),2,QTableWidgetItem(str(veri[2])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),3,QTableWidgetItem(str(veri[3])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),4,QTableWidgetItem(str(veri[4])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),5,QTableWidgetItem(str(veri[5])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),6,QTableWidgetItem(str(veri[6])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),7,QTableWidgetItem(str(veri[7])))
                self.Ssayfasi.siparistablosu.setItem(int(satirsayisi),8,QTableWidgetItem(str(veri[8])))

                satirsayisi +=1
        kolonlar = ["ID","Name FirstName","Phone","Address","Product Code","Product Color","Product Size","Product Description","Total Product"]
        self.Ssayfasi.siparistablosu.setHorizontalHeaderLabels(kolonlar)
    def siparis_sil(self):
        try:
            self.veritabani.veritabaniac()
            seciliSatir = self.Ssayfasi.siparistablosu.currentRow()
            if seciliSatir != -1:
                siparisID = self.Ssayfasi.siparistablosu.item(seciliSatir, 0).text()
                self.veritabani.siparis_sil(siparisID)
                self.Ssayfasi.statusbar.showMessage("Sipariş Silme İşlemi Başarılı.", 4000)
                self.kayitlisiparislistele()
            else:
                self.Ssayfasi.statusbar.showMessage("Lütfen bir sipariş seçiniz.", 4000)
        except Exception as error:
            self.Ssayfasi.statusbar.showMessage("Sipariş Silme İşlemi Başarısız. Hata: " + str(error), 6000)
        finally:
            self.veritabani.veritabanikapat()

        