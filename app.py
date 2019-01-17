from flask import Flask, render_template
from data import Articles, SZ50s, BoxOffice

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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

class SZ50_Api(Resource):
    def get(self):
        sz50 = []
        for dummy_index, row in SZ50s().iterrows():
            sz50.append({ 'code': row['code'], 'name': row['name'] })
        return sz50

api.add_resource(SZ50_Api, '/api/sz50')

class BoxOffice_Api(Resource):
    def get(self):
        boxoffice = []
        for dummy_index, row in BoxOffice().iterrows():
            boxoffice.append({
                'rank': row['Irank'],
                'movie_name': row['MovieName'],
                'box_per': row['boxPer'],
                'movie_day': row['movieDay'],
                'box_office': row['BoxOffice'],
                'sum_box_office': row['sumBoxOffice'],
                'updated_time': row['time']
            })
        return boxoffice

api.add_resource(BoxOffice_Api, '/api/boxoffice')

if __name__ == '__main__':
    app.run(debug=True)
