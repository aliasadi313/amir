import  sys
import  os

import  utility

from    sqlalchemy.orm              import  sessionmaker, join
from    sqlalchemy.orm.util         import  outerjoin
from    sqlalchemy.sql              import  and_, or_
from    sqlalchemy.sql.functions    import  *

from    helpers                     import  get_builder
from    amirconfig                  import  config
from    datetime                    import  date
from    database                    import  *


class dbConfig:

    data = {
        'co-name':'Enter Company name',
        'co-logo':'',
        'custSubject'   : '4',
        'bank'          : '1',
        'cash'          :'14',
        'buy'           :'17', 
        'sell'          :'18', 
        'sell-discount' :'25',
        'tax'           :'33', 
        #"sell-adds": '7',
        #"fund": '9', 
        #"acc-receivable": '10', 
        #"commission": '11',
    }

    def get_default(self, key):
        return self.data[key]

    def get_value(self, key):
        key = unicode(key)
        query = config.db.session.query(Config)
        query = query.filter(Config.cfgKey == key)
        return query.first().cfgValue

    def set_value(self, key, val, commit=True):
        val = unicode(val)
        query = config.db.session.query(Config)
        query = query.filter(Config.cfgId == key)
        query = query.update({u'cfgValue':val})
        if commit: # commit all of the at once for more speed
            config.db.session.commit()
        
    def get_int(self ,key):
        return int(self.get_value(key))

    def get_int_list(self, key):
        val = []
        try:
            for item in self.get_value(key).split(','):
                val.appned(int(item))
        except ValueError:
            return False
        return val

