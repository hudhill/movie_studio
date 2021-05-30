import pdb
from models.movie import Movie
import repositories.movie_repository as movie_repository

movie_repository.delete_all()

movie_1 = Movie("Sound of Metal", 7.8)
movie_2 = Movie("Nomadland", 7.4)
movie_3 = Movie("Promising Young Woman", 7.5)

print(movie_1.__dict__) # allows you to print class object as dictionary, otherwise would just show location of object

# save movies to the movies table in the movie_studio db:
movie_repository.save(movie_1)
movie_repository.save(movie_2)
movie_repository.save(movie_3)

# select_all rows from movies table: This just demonstrates that the function worked by printing out the results when you run this console.py file
example = movie_repository.select_all()
for movie in example:
    print(movie.__dict__)

# select one row from movies table: Then print it out to demonstrate that it worked
selected_movie = movie_repository.select(1)
print(selected_movie.__dict__)

# delete one row from movies table: This doesn't return results, so print out select_all again to see the change or check Postico
movie_repository.delete(1)

# update a row in the movies table: I have a change_rating function in the movie model; when run it asks the user how they would rate the given film. The update function updates that row in the movies table with the new data. You would need to comment out the delete method above for this to work properly. This doesn't return results, so print out select_all again to see the change or check Postico
movie_1.change_rating()
movie_repository.update(movie_1)

pdb.set_trace()