from flask import Flask, request, jsonify
from common import app, db, getJson
from .model import {{MODULE_NAME}}


@app.route("/api/{{MODULE_NAME.lower()}}/create", methods=["POST"])
def create_{{MODULE_NAME}}():
    json = getJson()
    {% for COLUMN in COLUMNS -%}
    {{ COLUMN["name"] }} = json["{{COLUMN["name"]}}"]
    {% endfor %}
    obj = MODULE_NAME(
        {%- for COLUMN in COLUMNS %}
        {{ COLUMN["name"] }} = {{COLUMN["name"]}},
        {%- endfor %}
    )
    db.session.add(obj)
    db.session.commit()
    return jsonify({"id": obj.id})

@app.route("/api/{{MODULE_NAME.lower()}}/delete", methods=["POST"])
def delete_{{MODULE_NAME}}():
    json = getJson()
    id = json["id"]
    obj = {{MODULE_NAME}}.query.filter_by(id=id, deleted=False).first()
    if obj is not None:
        db.session.delete(obj)
        db.session.commit()
        return jsonify({"id": obj.id})
    else:
        return None

@app.route("/api/{{MODULE_NAME.lower()}}/update", methods=["POST"])
def update_{{MODULE_NAME}}():
    json = getJson()
    id = json["id"]
    obj = {{MODULE_NAME}}.query.filter_by(id=id, deleted=False).first()
    {% for COLUMN in COLUMNS -%}
    obj.{{ COLUMN["name"] }} = json["{{COLUMN["name"]}}"]
    {% endfor %}
    db.session.commit()
    return jsonify({"id": obj.id})

@app.route("/api/{{MODULE_NAME.lower()}}/get", methods=["POST"])
def get_{{MODULE_NAME}}():
    json = getJson()
    id = json["id"]
    obj = {{MODULE_NAME}}.query.filter_by(id=id, deleted=False).first()
    return jsonify(toDict(obj))

{% for COLUMN in COLUMNS -%}
{%- if COLUMN["props"]["public"] -%}
@app.route("/api/{{MODULE_NAME.lower()}}/find_by_{{ COLUMN["name"] }}", methods=["POST"])
def find_{{MODULE_NAME}}_by_{{ COLUMN["name"] }}():
    json = getJson()
    {{ COLUMN["name"] }} = json["{{ COLUMN["name"] }}"]
    obj = User.query.filter_by(
        {{ COLUMN["name"] }}={{ COLUMN["name"] }}, 
        deleted=False
    ).first()
    return jsonify(toDict(obj))
{%- endif %}
{% endfor %}

{% for COLUMN in COLUMNS -%}
{%- if COLUMN["props"]["public"] -%}
@app.route("/api/{{MODULE_NAME.lower()}}/search_by_{{ COLUMN["name"] }}", methods=["POST"])
def search_{{MODULE_NAME}}_by_{{ COLUMN["name"] }}():
    json = getJson()
    {{ COLUMN["name"] }} = json["{{ COLUMN["name"] }}"]
    objs = User.query.filter(
        {{MODULE_NAME}}.{{ COLUMN["name"] }}.like('%'+ {{ COLUMN["name"] }} +'%'), 
        {{MODULE_NAME}}.deleted==False
    ).all()
    return jsonify(toDict(objs))
{%- endif %}
{% endfor %}