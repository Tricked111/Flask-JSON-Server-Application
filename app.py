""" Simple Flask API """
from flask import Flask,Response,jsonify,make_response,request
from models import database
from models.Movies import Movies

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JSON_SORT_KEYS'] = False
database.init_app(app)

with app.app_context():
    database.create_all()

@app.route('/')
def index():
    """ Index route """
    return "Hello, World"

@app.route('/movies',methods = ['GET','POST'])
def movies() -> Response:
    """ Movies route for GET, POST"""
    if request.method == 'GET':
        movies = Movies.query.order_by(Movies.release_year).all()
        return make_response(jsonify([row.to_dict() for row in movies]),
                             200)
    else:
        movies_content = request.get_json()
        new_movie = Movies(title = movies_content['title'],
                           description = movies_content['description'],
                           release_year = movies_content['release_year'])
        try:
            database.session.add(new_movie)
            database.session.commit()
            return make_response('You added new movie',200)
        except:
            return make_response('Error',500)



@app.route('/movies/<int:id>',methods = ['GET','PUT'])
def movies_id(id: int) -> Response:
    """ Movies_id route for GET, POST """
    if request.method == 'GET':
        movie = Movies.query.get_or_404(id)
        return make_response(jsonify(movie.to_dict()),200)
    else:
        movies = Movies.query.get_or_404(id)
        movies_content = request.get_json()
        movies.title = movies_content['title']
        movies.description = movies_content['description']
        movies.release_year = movies_content['release_year']
        try:
            database.session.add(movies)
            database.session.commit()
            return make_response('You updated movie',200)
        except:
            return make_response('Error',500)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")