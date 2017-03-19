import fresh_tomatoes
import media

bourne_ultimatum = media.Movie("The Bourne Ultimatum",
                               "Jason Bourne (Matt Damon) continues his international quest to uncover his true identity. From Russia to Europe to northern Africa to the United States, he must stay one step ahead of those who would capture or kill him before he has a chance to discover the truth.",
                               "http://ia.media-imdb.com/images/M/MV5BMTgzNjMwOTM3N15BMl5BanBnXkFtZTcwMzA5MDY0MQ@@._V1_SX640_SY720_.jpg",
                               "https://www.youtube.com/watch?v=N6J2oiKJr-A")

tokyo_drift = media.Movie("Tokyo Drift",
                          "Sean Boswell (Lucas Black) always feels like an outsider, but he defines himself through his victories as a street racer. His hobby makes him unpopular with the authorities, so he goes to live with his father in Japan. Once there and even more alienated, he learns about an exciting, but dangerous, new style of the sport. The stakes are high when Sean takes on the local champion and falls for the man's girlfriend.",
                          "https://upload.wikimedia.org/wikipedia/en/4/4f/Poster_-_Fast_and_Furious_Tokyo_Drift.jpg",
                          "https://www.youtube.com/watch?v=p8HQ2JLlc4E")

the_departed = media.Movie("The Departed",
                           "South Boston cop Billy Costigan (Leonardo DiCaprio) goes under cover to infiltrate the organization of gangland chief Frank Costello (Jack Nicholson). As Billy gains the mobster's trust, a career criminal named Colin Sullivan (Matt Damon) infiltrates the police department and reports on its activities to his syndicate bosses. When both organizations learn they have a mole in their midst, Billy and Colin must figure out each other's identities to save their own lives.",
                           "http://ia.media-imdb.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=SGWvwjZ0eDc")

point_break = media.Movie("Point Break",
                          "After a string of bizarre bank robberies in Southern California, with the crooks donning masks of various former presidents, a federal agent, Johnny Utah (Keanu Reeves), infiltrates the suspected gang. But this is no ordinary group of robbers. They're surfers -- led by the charismatic Bodhi (Patrick Swayze) -- who are addicted to the rush of thievery. But when Utah falls in love with a female surfer, Tyler (Lori Petty), who is close to the gang, it complicates his sense of duty.",
                          "https://upload.wikimedia.org/wikipedia/en/7/7e/Pointbreaktheatrical.jpg",
                          "https://www.youtube.com/watch?v=UuVDrpl1tIY")


star_wars = media.Movie("Star Wars",
                        "The Imperial Forces -- under orders from cruel Darth Vader (David Prowse) -- hold Princess Leia (Carrie Fisher) hostage, in their efforts to quell the rebellion against the Galactic Empire. Luke Skywalker (Mark Hamill) and Han Solo (Harrison Ford), captain of the Millennium Falcon, work together with the companionable droid duo R2-D2 (Kenny Baker) and C-3PO (Anthony Daniels) to rescue the beautiful princess, help the Rebel Alliance, and restore freedom and justice to the Galaxy.",
                        "http://www.originalprop.com/blog/wp-content/uploads/2008/12/star-wars-one-sheet-style-a.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

the_worlds_end = media.Movie("The World's End",
                             "Gary King (Simon Pegg) is an immature 40-year-old who's dying to take another stab at an epic pub-crawl that he last attempted 20 years earlier. He drags his reluctant buddies back to their hometown and sets out for a night of heavy drinking. As they make their way toward their ultimate destination -- the fabled World's End pub -- Gary and his friends attempt to reconcile the past and present. However, the real struggle is for the future when their journey turns into a battle for mankind.",
                             "http://ia.media-imdb.com/images/M/MV5BNzA1MTk1MzY0OV5BMl5BanBnXkFtZTgwNjkzNTUwMDE@._V1_SX640_SY720_.jpg",
                             "https://www.youtube.com/watch?v=n__1Y-N5tQk")

the_great_gatsby = media.Movie("The Great Gatsby",
                               "Midwest native Nick Carraway (Tobey Maguire) arrives in 1922 New York in search of the American dream. Nick, a would-be writer, moves in next-door to millionaire Jay Gatsby (Leonardo DiCaprio) and across the bay from his cousin Daisy (Carey Mulligan) and her philandering husband, Tom (Joel Edgerton). Thus, Nick becomes drawn into the captivating world of the wealthy and -- as he bears witness to their illusions and deceits -- pens a tale of impossible love, dreams, and tragedy.",
                               "https://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",
                               "https://www.youtube.com/watch?v=rARN6agiW7o")

daredevil = media.Movie("Daredevil",
                        "Attorney Matt Murdock (Ben Affleck) is blind, but his other four senses function with superhuman sharpness. By day, Murdock represents the downtrodden. At night, he is Daredevil, a masked vigilante, a relentless avenger of justice. When Wilson Fisk (Michael Clarke Duncan) hires Bullseye (Colin Farrell) to kill Daredevil, Murdock must rely on his own senses and search out the conspirators against justice -- which may include his own girlfriend, Elektra (Jennifer Garner).",
                        "http://horrornews.net/wp-content/uploads/2012/05/Daredevil-DVD-2003.jpg",
                        "https://www.youtube.com/watch?v=LmP3YFk_YHA")

good_will_hunting = media.Movie("Good Will Hunting",
                                "Will Hunting (Matt Damon) has a genius-level IQ but chooses to work as a janitor at MIT. When he solves a difficult graduate-level math problem, his talents are discovered by Professor Gerald Lambeau (Stellan Skarsgard), who decides to help the misguided youth reach his potential. When Will is arrested for attacking a police officer, Professor Lambeau makes a deal to get leniency for him if he will get treatment from therapist Sean Maguire (Robin Williams).",
                                "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=z02M3NRtkAA")



# List of movies to run in fresh_tomatoes
movies = [bourne_ultimatum, tokyo_drift, the_departed, point_break, star_wars, the_worlds_end, the_great_gatsby, daredevil, good_will_hunting]

# Creates the web page to view movie posters and trailers
fresh_tomatoes.open_movies_page(movies)
