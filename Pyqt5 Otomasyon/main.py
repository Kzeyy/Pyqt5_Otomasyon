from PyQt5.QtWidgets import QApplication
from K_giris import KgirisSayfasi


uygulama = QApplication([])
pencere = KgirisSayfasi()
pencere.show()
uygulama.exec_()