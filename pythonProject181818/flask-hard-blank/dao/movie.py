from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get_or_404(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director(self, did):
        return self.session.query(Movie).get_or_404(did)

    def get_by_genre(self, gid):
        return self.session.query(Movie).get_or_404(gid)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        self.session.query(Movie).filter(Movie.id == mid).delete()
        self.session.commit()

    def update(self, movie):
        self.session.query(Movie).filter(Movie.id == movie.id).delete()
        self.session.commit()
        self.session.add(movie)
        self.session.commit()
        return movie
