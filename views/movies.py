from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service


moviw_ns = Namespace('movies')


@moviw_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        result = MovieSchema(many=True).dumps(movies)
        return result, 200


@moviw_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        result = MovieSchema().dump(movie)
        return result, 200
