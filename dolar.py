import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dolar')
def dolar():
    # Busque os dados do dólar usando a API
    # Analise os dados usando BeautifulSoup
    # Renderize a página HTML com os dados do dólar

if __name__ == '__main__':
    app.run()
