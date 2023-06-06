import sqlite3
import os

class Veritabani():
    def __init__(self) -> None:
        yol= os.path.dirname(os.path.abspath(__file__))#dizini bulmak için
        self.db = os.path.join(yol,'isletme.db')#dizin ile veri tabaninin birleştirdi.
    def veritabaniac(self):
        self.con = sqlite3.connect(self.db)
        self.cursor = self.con.cursor()
    def veritabanikapat(self):
        self.con.close()
#----------------------------------------------------------------------------------------------------

    def stok_kayit(self,u_code,u_renk,u_olcu,u_aciklama,s_sayi):
        try:
            print(u_code,u_olcu,u_renk,u_aciklama,s_sayi)
            self.veritabaniac()
            sql = "insert into stoklar('u_code','u_renk','u_olcu','u_aciklama','s_sayi') values(?,?,?,?,?)"
            self.cursor.execute(sql,(u_code,u_renk,u_olcu,u_aciklama,s_sayi))
            self.con.commit()
        
            return True
        except Exception as error:
            print("Hata == " + str(error))
            return False
        finally:
            self.veritabanikapat()
#----------------------------------------------------------------------------------------------------
    def siparis_kayit(self,m_Adsoyad,m_tlf,m_adres,u_code,u_renk,u_olcu,s_aciklama,s_fiyat):
        try:
            self.veritabaniac()
            sorgu = """insert into siparisEkle ('m_AdSoyad','m_tlf','m_adres','u_code','u_renk',
                    'u_olcu','s_aciklama','s_fiyat') values (?,?,?,?,?,?,?,?)"""
            self.con.execute(sorgu,(m_Adsoyad,m_tlf,m_adres,u_code,u_renk,u_olcu,s_aciklama,s_fiyat))
            self.con.commit()
        except Exception as error:
            print("Sipariş Ekleme Hatası =" +str(error),7000)
        finally:
            self.veritabanikapat()
#-------------------------------------------------------------------------------------------------------
    def kayitSil(self, siparisID):
        cursor=self.con.cursor()
        sorgu = ("DELETE FROM stoklar WHERE u_code=? ")
        cursor.execute(sorgu,(siparisID,))
        self.con.commit()
        cursor.close()
#-------------------------------------------------------------------------------------------------------
    def siparis_sil(self, siparisID):
        cursor = self.con.cursor()
        sorgu = "DELETE FROM siparisEkle WHERE s_id = ?"
        cursor.execute(sorgu, (siparisID,))
        self.con.commit()
        cursor.close()

#-------------------------------------------------------------------------------------------------------
    def KayitListele(self):
        try:
            self.veritabaniac()
            sql = "select * from stoklar"
            self.cursor.execute(sql)
            veriler = self.cursor.fetchall()
            return veriler
        except Exception as error:
            print("Hata == " + str(error))
            return False
        finally:
            self.veritabanikapat()
    #----------------------------------------------------------------------------------------------------
    def siparisEkraniList(self):
        try:
            self.veritabaniac()
            sorgu = "select * from siparisEkle"
            self.cursor.execute(sorgu,)
            veriler = self.cursor.fetchall()
            return veriler
        except:
            False
        finally:
            self.veritabanikapat()
    

    #----------------------------------------------------------------------------------------------------         
    