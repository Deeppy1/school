movies = []
for i in range(4):
    movies.append(input("Please enter a film: ").lower())
movies.remove((input("Please enter the name of the movie you want to remove: ")))
print(movies)