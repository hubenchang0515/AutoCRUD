from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import TypeDecorator, String, Text
import hashlib

db = SQLAlchemy()

def filterDict(inputDict, keys):
    for key in keys:
        if key in inputDict:
            del inputDict[key]
    return inputDict

def convertDbModel(arg, filterKeys):
    if isinstance(arg, db.Model) :
        tmp = arg.__dict__
        if "_sa_instance_state" in tmp:
            del tmp["_sa_instance_state"]
        return convertDbModel(tmp, filterKeys)
    elif isinstance(arg, dict):
        if "_sa_instance_state" in arg:
            del arg["_sa_instance_state"]
        arg = filterDict(arg, filterKeys)
        for key in arg:
            arg[key] = convertDbModel(arg[key], filterKeys)
        return arg
    elif isinstance(arg, list):
        tmp = []
        for subArg in arg:
            tmp.append(convertDbModel(subArg, filterKeys))
        return tmp
    else:
        return arg

