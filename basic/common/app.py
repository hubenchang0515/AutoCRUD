from flask import Flask, request, jsonify
import json

app = Flask("__main__", static_folder='frontend', static_url_path="")

def getJson(default={}):
    if request.is_json :
        ret = request.json
    else :
        jsonStr = str(request.get_data(), encoding='utf-8')
        ret = json.loads(jsonStr)

    for key in default:
        if key not in ret:
            ret[key] = default[key]
    return ret