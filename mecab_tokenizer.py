import MeCab
from rasa_nlu.components import Component
from rasa_nlu.tokenizers import Tokenizer, Token

class MecabTokenizer(Tokenizer, Component):
    name = "mecab_tokenizer.MecabTokenizer"
    provides = ["tokens", "mecab_features"]

    def __init__(self, component_config=None):
        print('hogehoge')
        super(MecabTokenizer, self).__init__(component_config)
        self.mecab = MeCab.Tagger ("-Ochasen")
        self.mecab.parse("")

    def train(self, training_data, config, **kwargs):
        for example in training_data.training_examples:
            tokens, mecab_features = self.tokenize(example.text)
            example.set("tokens", tokens)
            example.set("mecab_features", mecab_features)

    def process(self, message, **kwargs):
        tokens, mecab_features = self.tokenize(message.text)
        message.set("tokens", tokens)
        message.set("mecab_features", mecab_features)

    def tokenize(self, text):
        words = []
        mecab_features = []
        node = self.mecab.parseToNode(text).next
        while node:
            words.append(node.surface)
            mecab_features.append(node.feature.split(','))
            node = node.next
        running_offset = 0
        tokens = []
        for word in words:
            word_offset = text.index(word, running_offset)
            running_offset = word_offset + len(word)
            tokens.append(Token(word, word_offset))
        return tokens, mecab_features