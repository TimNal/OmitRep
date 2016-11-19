'''
Created on 31.10.2016

@author: Timo
'''

import json

class Source:
    '''
    classdocs
    '''
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)

    def __init__(self):
        '''
        Constructor
        '''
        self._class = 'Source'
        self.author = ''
        self.pubinfo = ''
        self.gramps_id = 'S900001'
        self.title = 'Angelniemi Kuolleet 1749-1777'
        self.change = ''
        self.private = 'False'
        self.handle = 'd711372afc24f1c3cb6942a61a6'
        self.srcattr_list = []
        self.note_list = []
        self.reporef_list = []