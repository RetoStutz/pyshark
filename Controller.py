class Controller:

    def __init__(self, model):
        self.model = model

    def newData(self, newData):

        for layer in newData.layers:
            if "DATA" == str(layer):

                currentString = layer.Data
                charBuffer = []
                while currentString:
                    charBuffer.append(currentString[:2])
                    currentString = currentString[2:]

                for ind in range(len(charBuffer)):
                    charBuffer[ind] = chr(int("0x" + charBuffer[ind], 16))

                self.model.dataFunction("".join(charBuffer))
