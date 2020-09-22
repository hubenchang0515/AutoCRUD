class Validator(object):
    def __init__(self, name:str, type:=None, default=None, required=False):
        self.m_name = name
        self.m_type = type
        self.m_default = default
        self.m_required = required

    def validate(value):
        pass
