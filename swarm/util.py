import json

# TODO: make this automatically set a config
def get_config():
    with open("config.json", "r") as conf:
        contents = conf.read()
        contentsJson = json.loads(contents)
        return contentsJson