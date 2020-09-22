from flask_sqlalchemy import SQLAlchemy 
from flask_sqlalchemy.type import TypeDecorator, String, Text
import hashlib

db = SQLAlchemy()

def toDict(args):
    if isinstance(args, db.Model) :
        ret = args.__dict__
        if "_sa_instance_state" in ret:
            del ret["_sa_instance_state"]
        return ret

    elif isinstance(args, list):
        ret = []
        for arg in args :
            if isinstance(arg, db.Model) :
                dict = arg.__dict__
                if "_sa_instance_state" in dict:
                    del dict["_sa_instance_state"]
                ret.append(dict)
        return ret

    else:
        return args


class Md5(TypeDecorator):
    
    impl = String(32)
    
    def process_bind_param(self, value, dialect):
        m = hashlib.md5()
        m.update(value)
        return m.hexdigest()
 
    def process_result_value(self, value, dialect):
        return value
