from speech_recognition import Recognizer, Microphone
import nltk  # type: ignore
from nltk.data import find  # type: ignore
from nltk.corpus import stopwords  # type: ignore
from nltk.stem import WordNetLemmatizer # type: ignore


class RecognizeTheText:
    def __init__(self):
        self.recognizer = Recognizer()
        self.microphone = Microphone()
        self.download_nltk_resources()
        self.lemmatizer = WordNetLemmatizer()


    # download nltk resources
    def download_nltk_resources(self):
        resources = ['punkt', 'stopwords', 'wordnet']
        for resource in resources:
            try:
                find(f'tokenizers/{resource}') if resource == 'punkt' else find(f'corpora/{resource}')
            except LookupError:
                nltk.download(resource)


    # recognize the text
    def recognize_text(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language='pt-BR')
                return text
            except Exception as e:
                print(e)
                return None


    # process the input text
    def process_input(self, text):
        cleaned_text = ""
        new_list = stopwords.words('english')
        new_list.extend(["shop", "shopping", "list", "want"])

        for word in text.lower().split():
            if word not in new_list:
                cleaned_text += self.lemmatizer.lemmatize(word) + " "
        return cleaned_text
    

if __name__ == "__main__":
    recognizer = RecognizeTheText()
    text = "buy apples from the shopping list"
    processed_text = recognizer.process_input(text)
    print(processed_text)
