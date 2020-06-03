from flask import Flask, request
from flask_cors import CORS, cross_origin
from newspaper import Article

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, support_credentials=True)

@app.route('/', methods = ['GET', 'POST'])
@cross_origin(support_credentials=True)

def geturl():
    url = request.get_json(silent=True)

    #article = Article(url)
    #article.download()
    #article.parse()
    #return str(article.title)
    return str(url)


if __name__ == '__main__':
    app.run(debug=True)

