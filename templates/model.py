from flask_sqlalchemy import SQLAlchemy
from common import db
from common.types import *

# Generate by AutoCRUD
class {{MODULE_NAME}}(db.Model) :
    __tablename__ = "{{MODULE_NAME.lower()}}"
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, nullable=False, default=False)
    {%- for COLUMN in COLUMNS %}
    {{ COLUMN["name"] }} = db.Column(
        {{ COLUMN["type"] }},
        index = {{ COLUMN["props"]["index"] }},
        nullable = {{ COLUMN["props"]["nullable"] }},
        unique = {{ COLUMN["props"]["unique"] }},
        default = {{ COLUMN["props"]["default"] }},
    )
    {%- endfor %}

    def __repr__(self) :
        return '<{{MODULE_NAME}} %r>' % self.id