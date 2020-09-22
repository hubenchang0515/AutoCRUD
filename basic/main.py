#! /usr/bin/env python3
import os
from flask import Flask, redirect
from common import init
import handlers
import sys
from flask_cors import CORS

MAIN_FILE = os.path.basename(__file__)
MAIN_DIR  = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    sql_url = "sqlite:///" + os.path.join(MAIN_DIR, "database.sqlite")
    app = init(sql_url)

    if len(sys.argv) == 1:
        app.run(host="0.0.0.0", port=80, debug=False)
    elif len(sys.argv) == 2 and sys.argv[1] == "debug":
        CORS(app, supports_credentials=True)  # 设置跨域
        app.run(host="0.0.0.0", port=80, debug=True)
    else:
        print("EasyTodo backend server\n")
        print("Usage : %s       - start server" % MAIN_FILE)
        print("        %s debug - start server with debug mode" % MAIN_FILE)

