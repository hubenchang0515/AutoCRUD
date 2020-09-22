from sqlalchemy.types import (
    Integer,
    SmallInteger,
    BigInteger,
    Float,
    Numeric,
    String,
    Text,
    Unicode,
    UnicodeText,
    Boolean,
    Date,
    Time,
    LargeBinary
)
from sqlalchemy.types import TypeDecorator
import hashlib

class Md5(TypeDecorator):
    impl = String(32)

    def process_bind_param(self, value, dialect):
        m = hashlib.md5()
        m.update(value)
        return m.hexdigest()

    def process_result_value(self, value, dialect):
        return value