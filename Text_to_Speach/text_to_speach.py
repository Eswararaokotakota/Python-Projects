#pip install elevenlabslib
from elevenlabslib import *
from Text_to_speech_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

class speech(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(speech,self).__init__()
        self.setupUi(self)
        try:
            api = ElevenLabsUser("2a4e9c5178c68739db794e528c97cf0c")  # API key copied from Elevenlabs website
            self.voice = api.get_voices_by_name("Bella")[0]
        except:
            self.label.setText(" Ooops..  No Internet!")
            self.label.setStyleSheet("font:20px;color: red;background-color:yellow;")
            self.textEdit.setStyleSheet("padding-left:100px;padding-top:100px;font:20px;background-color:#fcc4c0;border-radius:10px;")
            self.textEdit.setPlaceholderText("Please connect to the internet.!")
            self.textEdit.setReadOnly(True)
            self.speak.setEnabled(False)     
        self.speak.clicked.connect(self.gen_voice)
        
    def gen_voice(self):
        text = self.textEdit.toPlainText()
        if len(text)==0:
            text = "Please Write Something my dearrr..."
        else:
            text = text
        self.voice.generate_and_play_audio(text,playInBackground=True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    text_speech = speech()
    text_speech.show()
    sys.exit(app.exec_())