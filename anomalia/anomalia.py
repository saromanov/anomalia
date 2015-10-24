
class Item:
    def __init__(self, event, pattern, entity):
        self.event = event
        self.pattern = pattern
        self.entity = entity

class Anomalia:
    def __init__(self, data, datatype, labels=None):
        self.data = data
        self.datatype = datatype

    def preprocessing(self):
        ''' preprocessing data before apply it to algorithms
        '''
        pass
