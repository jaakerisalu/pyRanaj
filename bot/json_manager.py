import json


class JsonManager:
    """
        Hopefully this will be useful for custom writes
    """
    def __init__(self):
        # Load the JSON into memory (It's around a few MB and grows slowly)
        with open('fixtures/ranaj.json', 'r') as json_file:
            self.json_content = json.loads(json_file)

    def access(self, query):
        return self.json_content[query]

