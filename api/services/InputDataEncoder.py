import json

class InputDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, InputData):
            return obj.to_dict()
        return super().default(obj)