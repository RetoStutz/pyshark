class Model:

    def __init__(self, initData=""):
        self.telegramCounter = 0
        self._data = initData
        self.callbacks = []

    def getData(self):
        return self._data

    def dataFunction(self, newData):
        oldData = self._data
        self._data = newData
        self.notifyObservers(oldData, newData)

    def notifyObservers(self, oldData, newData):
        for callback in self.callbacks:
            callback(oldData, newData)

    def registerCallback(self, callback):
        self.callbacks.append(callback)
