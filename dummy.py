from datetime import datetime

import pyshark

currentLine = 1

capture = pyshark.LiveCapture(interface='Adapter for loopback traffic capture', display_filter='tcp.port==5000')

for packet in capture.sniff_continuously():

    print(packet.layers)

    for layer in packet.layers:
        if "DATA" == str(layer):

            print(layer.Data)
            currentString = layer.Data
            o = []
            while currentString:
                o.append(currentString[:2])
                currentString = currentString[2:]

            for ind in range(len(o)):
                o[ind] = chr(int("0x" + o[ind], 16))

            with open('Logfile-' + str(datetime.now().date()) + '.txt', 'a') as f:
                space = "    "
                date = str(datetime.now())
                info = "".join(o)
                logger = str(currentLine) + space + date + space + info
                print(logger)
                f.write(logger)
                f.write('\n')
                currentLine = currentLine + 1
