from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
import os, json, helper, shutil
from distutils.dir_util import copy_tree

# 常量定义
BUILD_DIR = "build"
TEMPLATE_DIR = "templates"
CONFIGURE_DIR = "configure"
MODULES_DIR = os.path.join(BUILD_DIR, "modules")

# 初始化模板
env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape(enabled_extensions="py")
)
modelTemplate = env.get_template("model.py")
handlerTemplate = env.get_template("handler.py")

# 生成
handlersList = []
fileList = os.listdir(CONFIGURE_DIR)
for filename in fileList:
    with open(os.path.join(CONFIGURE_DIR, filename)) as fp:
        try:
            data = json.load(fp)
            helper.setDefaults(data["columns"])
        except Exception as e:
            writeStderr("SKIP %s" % filename)
            writeStderr(e)
            continue

    # 创建模块的目录
    moduleName = MODULE_NAME=data["table"]
    moduleDir = os.path.join(MODULES_DIR, moduleName)
    os.makedirs(moduleDir, mode=0o644, exist_ok=True)

    # 创建model
    modelFile = os.path.join(moduleDir, "model.py")
    model = modelTemplate.render(MODULE_NAME=moduleName, COLUMNS=data["columns"])
    with open(modelFile, "w+") as fp:
        fp.write(model)

    # 创建handler
    handlerFile = os.path.join(moduleDir, "handler.py")
    handler = handlerTemplate.render(MODULE_NAME=moduleName, COLUMNS=data["columns"])
    with open(handlerFile, "w+") as fp:
        fp.write(handler)

    print("Created module '%s'" % moduleName)
    handlersList.append("modules.%s.handler" % moduleName)

# 创建一个import所有handler的文件
handlersListFile = os.path.join(BUILD_DIR, "handlers.py")
handlersListTemplate = Template("{% for handler in handlersList %}import {{handler}}\n{% endfor %}")
handlers = handlersListTemplate.render(handlersList=handlersList)
with open(handlerFile, "w+") as fp:
        fp.write(handlers)

# 复制基础文件
copy_tree("./basic/common", BUILD_DIR)
shutil.copy("./basic/main.py", BUILD_DIR)