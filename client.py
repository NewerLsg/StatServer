# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *

PORTS = (9998, 9999)
PORT = 9999
SIZEOF_UINT32 = 4

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Ititialize socket
        self.socket = QTcpSocket()

        # Initialize data IO variables
        self.nextBlockSize = 0
        self.request = None

        # Create widgets/layout
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Enter text here, dummy")
        self.lineedit.selectAll()
        self.connectButton = QPushButton("Connect")
        self.connectButton.setEnabled(True)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.connectButton)
        self.setLayout(layout)
        self.lineedit.setFocus()

        # Signals and slots for line edit and connect button
        self.lineedit.returnPressed.connect(self.issueRequest)
        self.connectButton.clicked.connect(self.connectToServer)

        self.setWindowTitle("Client")
        # Signals and slots for networking
        self.socket.readyRead.connect(self.readFromServer)
        self.socket.disconnected.connect(self.serverHasStopped)
        self.connect(self.socket,
                     SIGNAL("error(QAbstractSocket::SocketError)"),
                     self.serverHasError)

    # Update GUI
    def updateUi(self, text):
        self.browser.append(text)

    # Create connection to server
    def connectToServer(self):
        self.connectButton.setEnabled(False)
        self.socket.connectToHost("localhost", PORT)

    def issueRequest(self):

        #门请求权限
        self.socket.write("DS0001\n") #1号门请求权限
        self.socket.write("DS0002\n") #2号门请求权限
        self.socket.write("DS0003\n") #3号门请求权限
        self.socket.write("DS0004\n") #4号门请求权限
        self.socket.write("DS0005\n") #5号门请求权限
        self.socket.write("DS0006\n") #6号门请求权限

        self.socket.write("TS0102001002hongdui\n")
        self.socket.write("TS0103003004005landui\n")
        self.socket.write("TS0103006007008zidui\n")

        #被击中
        self.socket.write("MS01001\n")
        self.socket.write("MS01002\n")
        self.socket.write("MS01002\n")
        self.socket.write("MS01003\n")
        self.socket.write("MS01004\n")
        self.socket.write("MS01005\n")
        self.socket.write("MS01006\n")
        self.socket.write("MS01007\n")
        self.socket.write("MS01008\n")
        self.socket.write("MS01008\n")

        #HD队1号开1号门,应该是允许
        self.socket.write("DS0100101\n")
        self.socket.write("DS0100301\n")
        self.socket.write("DS0100601\n")

         #HD队2号开2号门,应该是允许
        self.socket.write("DS0100202\n")

        #LD队3号开1号门,应该是允许
        self.socket.write("DS0100301\n")
        self.socket.write("DS0100302\n")

        #HD  3
        self.socket.write("DS0100103\n")

        #LD 2
        self.socket.write("DS0100302\n")

        #
        self.socket.write("DS0100601\n")

        self.lineedit.setText("")

    def readFromServer(self):
        while self.socket.canReadLine():
            rawMsg = self.socket.readLine(128)         #QBytesArray
            print("raw:%s,data:%s" % (rawMsg, rawMsg.decode()))
            msg = rawMsg.decode()
            self.updateUi(msg[:-1])
            continue
            
        """"
        while self.socket.bytesAvailable():
            stream = QDataStream(self.socket)
            stream.setVersion(QDataStream.Qt_4_2)
            textFromServer = stream.readQString()
            print("recv:%s" % textFromServer)
            self.updateUi(textFromServer)
            """

    def serverHasStopped(self):
        self.socket.close()
        self.connectButton.setEnabled(True)

    def serverHasError(self):
        self.updateUi("Error: {}".format(
                self.socket.errorString()))
        self.socket.close()
        self.connectButton.setEnabled(True)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
