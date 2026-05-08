# 2. Create a list of movies
movies = ["Dune", "Wonder Woman", "Avengers", "The Matrix", "Superman"]

# 3. Use len() function
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)

# 4a. Use sorted() function
print(sorted(movies))
print(movies)

# 4b. Use .sort() method
movies.sort()
print(movies)
     
    # Comparing the two outputs:  - sorted() returns a new sorted list but leaves the original list unchanged 
    #           whereas           - .sort() permanently modifies the original list in place 

# 5. Use the .append() method
movies.append("Inception")

print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)
