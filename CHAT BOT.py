import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import json

lemmatizer = WordNetLemmatizer()

# Sample intents for the chatbot
intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hello", "Hey", "Good morning", "Good evening"],
            "responses": ["Hello!", "Hi there!", "Greetings!", "Hey! How can I help you?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye"],
            "responses": ["Goodbye!", "See you later!", "Have a great day!"]
        },
        {
            "tag": "thanks",
            "patterns": ["Thanks", "Thank you", "That's helpful"],
            "responses": ["You're welcome!", "Glad I could help!", "Anytime!"]
        },
        {
            "tag": "noanswer",
            "patterns": [],
            "responses": ["Sorry, I don't understand that."]
        }
    ]
}

def clean_up_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    words = [lemmatizer.lemmatize(w.lower()) for w in words]
    return words

def bag_of_words(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

# Create word and class lists
words = []
classes = []
documents = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w.isalnum()]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Simple prediction and response function
def predict_class(sentence):
    sentence_words = clean_up_sentence(sentence)
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if sentence.lower() in pattern.lower():
                return intent["tag"]
    return "noanswer"

def get_response(intent_tag):
    for intent in intents["intents"]:
        if intent["tag"] == intent_tag:
            return random.choice(intent["responses"])
    return "I'm not sure how to respond to that."

# Main chat loop
def chatbot_response(msg):
    intent = predict_class(msg)
    response = get_response(intent)
    return response

# Interface
if _name_ == "_main_":
    print("Chatbot is running! (Type 'quit' to stop)")
    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        reply = chatbot_response(message)
        print("Bot:", reply)
