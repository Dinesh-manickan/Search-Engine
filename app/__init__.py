from flask import Flask
# import nltk
# nltk.download()
app=Flask(__name__)

from app.api import apis
