import sys
import subprocess

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

install_and_import("PyQt5")
install_and_import("PyQt5.QtWidgets")
install_and_import("PyQt5.QtCore")
install_and_import("PyQt5.QtWebEngineWidgets")

from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class PyQt5Wrapper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Wrapper")
        self.resize(900, 600)

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.url_bar)

        self.browser.setUrl(QUrl("http://www.google.com"))
        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url_text = self.url_bar.text()
        if not url_text.startswith(("http://", "https://")):
            url_text = "http://" + url_text
        self.browser.setUrl(QUrl(url_text))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyQt5Wrapper()
    window.show()
    sys.exit(app.exec_())