def movieAwards(oscarResults):
    awards_count = {}
    for category, movie in oscarResults:
        awards_count[movie] = awards_count.get(movie, 0) + 1
    return awards_count

# Test case
oscarResults = { 
    ("Best Picture", "Green Book"), 
    ("Best Actor", "Bohemian Rhapsody"),
    ("Best Actress", "The Favourite"),
    ("Film Editing", "Bohemian Rhapsody"),
    ("Best Original Score", "Black Panther"),
    ("Costume Design", "Black Panther"),
    ("Sound Editing", "Bohemian Rhapsody"),
    ("Best Director", "Roma")
}

print(movieAwards(oscarResults))
