from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer

app = QApplication([])
view = QWebEngineView()
# Use a raw string to avoid accidental special characters in Windows filenames:
# ``c:\temp`` is `c<tab>emp`!
view.load(QUrl.fromLocalFile(r'{}'))
view.show()
view.page().loadFinished.connect(
    # Display the web page for one second after it loads.
    lambda ok: QTimer.singleShot(1000, app.quit))
app.exec_()
