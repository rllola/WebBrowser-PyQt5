from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer, QLibraryInfo

app = QApplication([])

print "PrefixPath : " + QLibraryInfo.location(QLibraryInfo.PrefixPath)
print "DocumentationPath : " + QLibraryInfo.location(QLibraryInfo.DocumentationPath)
print "HeadersPath : " + QLibraryInfo.location(QLibraryInfo.HeadersPath)
print "LibrariesPath : " + QLibraryInfo.location(QLibraryInfo.LibrariesPath)
print "LibraryExecutablesPath : " + QLibraryInfo.location(QLibraryInfo.LibraryExecutablesPath)
print "BinariesPath : " + QLibraryInfo.location(QLibraryInfo.BinariesPath)
print "PluginsPath : " + QLibraryInfo.location(QLibraryInfo.PluginsPath)
print "ImportsPath : " + QLibraryInfo.location(QLibraryInfo.ImportsPath)
print "Qml2ImportsPath : " + QLibraryInfo.location(QLibraryInfo.Qml2ImportsPath)
print "ArchDataPath : " + QLibraryInfo.location(QLibraryInfo.ArchDataPath)
print "DataPath : " + QLibraryInfo.location(QLibraryInfo.DataPath)
print "TranslationsPath : " + QLibraryInfo.location(QLibraryInfo.TranslationsPath)
print "ExamplesPath : " + QLibraryInfo.location(QLibraryInfo.ExamplesPath)
print "TestsPath : " + QLibraryInfo.location(QLibraryInfo.TestsPath)
print "SettingsPath : " + QLibraryInfo.location(QLibraryInfo.SettingsPath)

view = QWebEngineView()
# Use a raw string to avoid accidental special characters in Windows filenames:
# ``c:\temp`` is `c<tab>emp`!
view.load(QUrl.fromLocalFile(r'{}'))
view.show()

view.page().loadFinished.connect(
    # Display the web page for one second after it loads.
    lambda ok: QTimer.singleShot(1000, app.quit))
app.exec_()
