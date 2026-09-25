from sqlalchemy.orm import Session
from .database import engine, Base, Movie, SessionLocal

movie_data = [
    {
        "title": "The Dark Knight",
        "genre": "Action, Crime, Drama",
        "director": "Christopher Nolan",
        "actors": "Christian Bale, Heath Ledger, Aaron Eckhart",
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
    },
    {
        "title": "Inception",
        "genre": "Action, Adventure, Sci-Fi",
        "director": "Christopher Nolan",
        "actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page",
        "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "poster_url": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQGNV5Pu6.jpg"
    },
    {
        "title": "Interstellar",
        "genre": "Adventure, Drama, Sci-Fi",
        "director": "Christopher Nolan",
        "actors": "Matthew McConaughey, Anne Hathaway, Jessica Chastain",
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    },
    {
        "title": "The Matrix",
        "genre": "Action, Sci-Fi",
        "director": "Lana Wachowski, Lilly Wachowski",
        "actors": "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "poster_url": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GvwJwBGeoMt8.jpg"
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action, Adventure, Drama",
        "director": "Anthony Russo, Joe Russo",
        "actors": "Robert Downey Jr., Chris Evans, Mark Ruffalo",
        "description": "After the devastating events of Infinity War, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
        "poster_url": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"
    },
    {
        "title": "Pulp Fiction",
        "genre": "Crime, Drama",
        "director": "Quentin Tarantino",
        "actors": "John Travolta, Uma Thurman, Samuel L. Jackson",
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "poster_url": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8SPFAJtx.jpg"
    },
    {
        "title": "The Godfather",
        "genre": "Crime, Drama",
        "director": "Francis Ford Coppola",
        "actors": "Marlon Brando, Al Pacino, James Caan",
        "description": "An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.",
        "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg"
    },
    {
        "title": "Fight Club",
        "genre": "Drama",
        "director": "David Fincher",
        "actors": "Brad Pitt, Edward Norton, Meat Loaf",
        "description": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
        "poster_url": "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg"
    },
    {
        "title": "Forrest Gump",
        "genre": "Drama, Romance",
        "director": "Robert Zemeckis",
        "actors": "Tom Hanks, Robin Wright, Gary Sinise",
        "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
        "poster_url": "https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg"
    },
    {
        "title": "Goodfellas",
        "genre": "Biography, Crime, Drama",
        "director": "Martin Scorsese",
        "actors": "Robert De Niro, Ray Liotta, Joe Pesci",
        "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito.",
        "poster_url": "https://image.tmdb.org/t/p/w500/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg"
    },
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "director": "Frank Darabont",
        "actors": "Tim Robbins, Morgan Freeman, Bob Gunton",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "poster_url": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "genre": "Action, Adventure, Drama",
        "director": "Peter Jackson",
        "actors": "Elijah Wood, Viggo Mortensen, Ian McKellen",
        "description": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
        "poster_url": "https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg"
    },
    {
        "title": "Star Wars: Episode V - The Empire Strikes Back",
        "genre": "Action, Adventure, Fantasy",
        "director": "Irvin Kershner",
        "actors": "Mark Hamill, Harrison Ford, Carrie Fisher",
        "description": "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda.",
        "poster_url": "https://image.tmdb.org/t/p/w500/7BuH8itoSrLExs2GIrFNKxxhGQ1.jpg"
    },
    {
        "title": "Gladiator",
        "genre": "Action, Adventure, Drama",
        "director": "Ridley Scott",
        "actors": "Russell Crowe, Joaquin Phoenix, Connie Nielsen",
        "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "poster_url": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"
    },
    {
        "title": "Jurassic Park",
        "genre": "Action, Adventure, Sci-Fi",
        "director": "Steven Spielberg",
        "actors": "Sam Neill, Laura Dern, Jeff Goldblum",
        "description": "A pragmatic paleontologist visiting an almost complete theme park is tasked with protecting a couple of kids after a power failure causes the park's cloned dinosaurs to run loose.",
        "poster_url": "https://image.tmdb.org/t/p/w500/oU7Oq2kFAAlGqbU4GvlPBK3WMNy.jpg"
    }
]

def seed_db():
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()

    if db.query(Movie).count() == 0:
        print("Seeding database with movies...")
        for data in movie_data:
            movie = Movie(**data)
            db.add(movie)
        db.commit()
        print("Done seeding!")
    else:
        print("Database already seeded.")
    db.close()

if __name__ == "__main__":
    seed_db()
