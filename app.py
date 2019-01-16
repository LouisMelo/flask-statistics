from flask import Flask, render_template
from data import Articles, SZ50s, BoxOffice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles())

@app.route('/sz50')
def sz50():
    return render_template('sz50.html', sz50 = SZ50s())

@app.route('/boxoffice')
def boxoffice():
    return render_template('boxoffice.html', boxoffice = BoxOffice())

if __name__ == '__main__':
    app.run(debug=True)
