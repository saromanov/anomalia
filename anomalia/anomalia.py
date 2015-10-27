import os
import logging
import numpy as np

logging.basicConfig(level = logging.DEBUG)

class Item:
    def __init__(self, event, pattern, entity):
        self.event = event
        self.pattern = pattern
        self.entity = entity

class Anomalia:
    def __init__(self, datatype, labels=None, data = None, filepath=None):
        self.data = data
        self.datatype = datatype
        self.events = []
        self.isrunning = False
        if self.datatype == 'file':
            self.data = self._read()


    def _read(self, path):
        if os.path.exists(path) is False:
            logging.error('File {0} is not found'.format(path))
            raise Exception("File not found")

        basename = os.basename(path)
        if basename.find('.csv') != -1:
            logging.info("Try to load .csv file is loaded")
            return np.loadtxt(open(path,"rb"),delimiter=",",skiprows=1)
        else:
            #load every line
            f = open(path, 'r')
            result = []
            logging.info("Try to load data from file")
            lines = f.readlines()
            f.close()
            for line in lines:
                result.append([float(item) for item in line.split()])
            return np.array(result)

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
