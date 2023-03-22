from flask import request

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        stmt = Movie.query
        if director_id:
            stmt = stmt.filter(Movie.director_id == director_id)
        if genre_id:
            stmt = stmt.filter(Movie.genre_id == genre_id)
        if year:
            stmt = stmt.filter(Movie.year == year)
        movies = stmt.all()
        return movies
