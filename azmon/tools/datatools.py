

def dict_clean(d):
    return { k: v for k, v in d.items() if v is not None }
