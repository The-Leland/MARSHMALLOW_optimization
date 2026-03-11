

def populate_object(obj, data):
    for field, value in data.items():
        if hasattr(obj, field):
            setattr(obj, field, value)
    return obj