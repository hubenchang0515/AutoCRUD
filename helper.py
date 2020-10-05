import sys

def writeStderr(*args):
    print(args, file=sys.stderr)

def setDefaults(columns):
    defaultValue = {
        "index" : False,
        "unique" : False,
        "nullable" : True,
        "default" : None,
        "private" : False,
    }

    for column in columns:
        for key in defaultValue:
            if key not in column["props"]:
                column["props"][key] = defaultValue[key]

    return columns