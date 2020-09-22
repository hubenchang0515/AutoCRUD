from flask import Flask, request, jsonify

app = Flask("__main__", static_folder='frontend', static_url_path="")

def getJson():
    if request.is_json :
        return request.json
    else :
        jsonStr = str(request.get_data(), encoding='utf-8')
        return json.loads(jsonStr)