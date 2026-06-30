class TextAnalyzer:

    def __init__(self, text):
        self.text = text


    def word_count(self):
        words = self.text.split()

        return len(words)


text = TextAnalyzer("Python is a powerful programming language")

print("Word Count:", text.word_count())