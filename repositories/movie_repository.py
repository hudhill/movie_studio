from db.run_sql import run_sql
from models.movie import Movie

def save(movie):
    sql = "INSERT INTO movies (title, rating) VALUES (%s, %s) RETURNING *"
    values = [movie.title, movie.rating]
    results = run_sql(sql, values)
    id = results[0]['id']
    movie.id = id
    return movie

def select_all():
    movies = []
    sql = "SELECT * FROM movies"
    results = run_sql(sql)
    for row in results:
        movie = Movie(row['title'], row['rating'], row['id'])
        movies.append(movie)
    return movies

def select(id):
    movie = None
    sql = "SELECT * FROM movies WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        movie = Movie(result['title'], result['rating'], result['id'])
    return movie

def delete_all():
    sql = "DELETE FROM movies"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM movies WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(movie):
    sql = "UPDATE movies SET (title, rating) = (%s, %s) WHERE id = %s"
    values = [movie.title, movie.rating, movie.id]
    run_sql(sql, values)