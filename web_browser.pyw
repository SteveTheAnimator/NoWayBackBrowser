import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView


class NoWayBackBrowser(QWebEngineView):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event):
        # Disable right-click context menu
        pass

    def mousePressEvent(self, event):
        # Disable back and forward navigation buttons
        if event.buttons() == Qt.BackButton or event.buttons() == Qt.ForwardButton:
            event.ignore()
        else:
            super().mousePressEvent(event)


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("No Way Back Browser")
        self.browser = NoWayBackBrowser()
        self.setCentralWidget(self.browser)

    def load_page(self, url):
        self.browser.load(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.load_page("https://www.google.com")  # Default page to load
    browser.show()
    sys.exit(app.exec_())
