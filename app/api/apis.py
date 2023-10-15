from app import app
from flask import render_template
from flask import request,redirect,url_for, jsonify

from app.model.model import model

obj = model()
@app.route('/')
def index():
    return render_template('home.html',title='Home Page', active_page='Home')

@app.route('/InvertedIndex')
def InvertedIndex():
    invertedIndex=obj.InvertedIndexBuilder()
    return render_template('invertedIndex.html',result=invertedIndex, title='InvertedIndex', active_page='InvertedIndex')

@app.route('/BigramIndex')
def BigramIndex():
    bigramIndex=obj.BigramIndexBuilder()
    return render_template('ngram.html',data=bigramIndex, title='N-gram', active_page='ngram')

@app.route('/PermutermIndex')
def PermutermIndex():
    permutermIndex=obj.PermutermIndexBuilder()
    return render_template('permutermIndex.html',data=permutermIndex, title='Permuterm Index', active_page='PermutermIndex')

@app.route('/SoundexIndex')
def SoundexIndex():
    soundexIndex=obj.SoundexIndexBuilder()
    return render_template('soundex.html',data=soundexIndex , title='Soundex', active_page='SoundexIndex')

@app.route('/EditDistance', methods=['GET'])
def EditDistance():
    misspelledWord=request.args.get('misspelledWord', '')
    if misspelledWord == '':
        error_message = "Please provide a misspelled word."
        return redirect(url_for('error', error_message=error_message))
    editDistance=obj.editDistance(misspelledWord)
    return render_template('editDistanceResult.html', result=editDistance,  title='EditDistance', active_page='EditDistance')

@app.route('/SearchEditDistance')
def DisplayEditDistance():
    return render_template('editDistanceSearch.html', title='EditDistance', active_page='EditDistance')

@app.route('/pullEditDistance', methods=['GET'])
def pullEditDistance(): #for that pop up
    misspelledWord=request.args.get('misspelledWord', '')
    editDistance=obj.editDistance(misspelledWord)
    return editDistance

@app.route('/search',  methods=['GET'])
def search():
    query = request.args.get('query', '')
    results= obj.queryProcessing(query)
    return render_template('search.html',result=results)

@app.route('/searching', methods=['GET'])
def searching():
    search_term = request.args.get('q', '')
    return jsonify(obj.PermutermIndexQuery(search_term))

@app.route('/getDocument/<id>')
def getDocument(id):
    # documents = obj.SendDocuments()
    # result = obj.ReadFile(documents[int(id)-1])
    result = obj.getDocument(id)
    return render_template('displayDoc.html',results=result)

@app.route('/pr')
def pr():
    return render_template('precisionRecall.html')

@app.route('/error')
def error():
    error_message = request.args.get('error_message', 'An error occurred.')
    return render_template('error.html', error_message=error_message)