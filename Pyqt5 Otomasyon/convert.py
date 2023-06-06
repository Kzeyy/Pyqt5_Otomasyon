from PyQt5 import uic
with open("K_giris_python.py","w",encoding= "utf-8") as fout:
    uic.compileUi("k_giris.ui",fout)
with open("anasayfa_python.py","w",encoding= "utf-8") as fout:
    uic.compileUi("anasayfa.ui",fout)
with open("siparisekle_python.py","w",encoding="utf-8") as fout:
    uic.compileUi("siparisekle.ui",fout)
with open("stokEkrani_python.py","w",encoding="utf-8") as fout:
    uic.compileUi("stokEkrani.ui",fout)