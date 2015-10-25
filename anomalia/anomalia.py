
class Item:
    def __init__(self, event, pattern, entity):
        self.event = event
        self.pattern = pattern
        self.entity = entity

class Anomalia:
    def __init__(self, data, datatype, labels=None):
        self.data = data
        self.datatype = datatype
        self.events = []
        self.isrunning = False

    def preprocessing(self):
        ''' preprocessing data before apply it to algorithms
        '''
        pass

    def addEvent(self, data):
        if isinstance(data, list):
            if len(data) == 0:
                return
            self.events.append(data)

    def stop(self):
        ''' Stopping real time anomaly detection
        '''
        self.isrunning = False

    def start(self):
        ''' Start anomaly detection in real time
        '''
        self.isrunning = True
        while self.isrunning:
            pass
