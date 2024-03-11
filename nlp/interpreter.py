import spacy
from langdetect import detect

class Interpreter:
    def __init__(self):

        try:
            spacy.load("es_core_news_sm")
        except IOError:
            from spacy.cli import download
            download("es_core_news_sm")

        try:
            spacy.load("en_core_web_sm")
        except IOError:
            from spacy.cli import download
            download("en_core_web_sm")

        # Carga ambos modelos de lenguaje.
        self.nlp_es = spacy.load("es_core_news_sm")
        self.nlp_en = spacy.load("en_core_web_sm")

    def interpret(self, user_input):
        # Intenta detectar el idioma del input del usuario.
        try:
            lang = detect(user_input)
        except:
            lang = 'en'  # Asume inglés por defecto si la detección falla.

        # Selecciona el modelo de lenguaje basado en el idioma detectado.
        nlp = self.nlp_es if lang == 'es' else self.nlp_en

        doc = nlp(user_input.lower())
        area_keywords = {
            'Receiving': ['Receiving', 'recibo', 'recivo', 'receiving'],
            'Automotive': ['Automotive', 'auto', 'auto tower'],
            'Industrial': ['Industrial', 'ind', 'industrial tower', 'ind tower'],
            'Shipping': ['Shipping', 'embarque', 'embarques', 'shipping'],
            'End': ['goodbye', 'bye', 'fare well', 'see you' , 'adios', 'hasta la proxima', 'haste luego', 'fin', 'end'],
        }

        for area, keywords in area_keywords.items():
            if any(word in doc.text for word in keywords):
                return area
        return None
