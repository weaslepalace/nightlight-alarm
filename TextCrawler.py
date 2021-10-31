
class TextCrawler:

    _variable_map = {}

    def _tokenize(self, contents):
        """
        Warning: there is currently on escape for '$'
        """
        tokens = contents.split("$")
        if len(tokens) % 2 == 0:
            raise Exception("Unterminated variable deliminator '$'")
        text = tokens[::2]
        variables = tokens[1::2]
        return text, variables   

    def __init__(self, path):
        with open(path) as f:
            raw_contents = f.read()
        self._text, self._variables = self._tokenize(raw_contents)

    def define(self, key, value):
        if key not in self._variables:
            raise Exception(f"Variable \"{key}\" not found in document")
        self._variable_map[key] = value

    def make(self):
        doc = [
            text + self._variable_map[key]
            for text, key in zip(self._text, self._variables)
        ]
        doc.append(self._text[-1])
        return "".join(doc)
