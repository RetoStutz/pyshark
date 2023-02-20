import pyshark

from datetime import datetime

class View:

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

        self.model.registerCallback(self.update)

        self.capture = pyshark.LiveCapture(interface='Adapter for loopback traffic capture',
                                           display_filter='tcp.port==5000')

        self.startReading()

    def startReading(self):
        for packet in self.capture.sniff_continuously():
            self.controller.newData(packet)

    def update(self, oldData, newData):
        self.writeToLog(newData)

    def writeToLog(self, info):
        with open('Logfile-' + str(datetime.now().date()) + '.txt', 'a') as f:
            space = "    "
            date = str(datetime.now())
            logger = date + space + info
            print(logger)
            f.write(logger)
            f.write('\n')
