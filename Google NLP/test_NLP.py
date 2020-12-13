import pytest
import os
from google.cloud import language_v1
import sys

class redirect:
    content = []

    def write(self,str):
        self.content.append( str)
    def flush(self):
        self.content = ""
global r

def analyze_sentiment(text_content):

    print('Analysis start')

    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """
    credential_path = "C:/GoogleNLP_Key/My First Project-78e3be7f4341.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request={'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    print(u"Language of the text: {}".format(response.language))

def test_start():
    assert r.content[0] == 'Analysis start'

def test_SenScore():
    assert r.content[1].count('score') == 1

def test_Magnitude():
    assert r.content[2].count('magnitude') == 1



r = redirect()
sys.stdout = r

# print directory redirected. The prompts and results are all stored in print.txt file
analyze_sentiment('Test examples of the NLP test')

f = open('print.txt', 'w')
for i in range(len(r.content)):
    f.write(r.content[i])
f.close()

istr = ""
for istr in r.content:
    if istr == '\n':
        r.content.remove(istr)

test_start()
test_SenScore()
test_Magnitude()
