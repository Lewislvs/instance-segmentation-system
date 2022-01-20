import sys
from jieguo_window import *
from shibie_window import *
from zhujiemian import *

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)

    zhu = zhujiemian()

    zhu.show()

    sys.exit(app.exec_())


