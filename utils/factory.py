from models.beef_iso import BEEFISO

def get_model(model_name, args):
    name = model_name.lower()
    if name == "beefiso":
        return BEEFISO(args)
    else:
        assert 0
