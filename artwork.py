#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from event import Location

class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        assert isinstance(title, str) and title.strip(), "Title must be a non-empty string"
        assert isinstance(artist, str) and artist.strip(), "Artist must be a non-empty string"
        assert isinstance(date_of_creation, str) and date_of_creation.strip(), "Date of creation must be a non-empty string"
        assert isinstance(historical_significance, str) and historical_significance.strip(), "Historical significance must be a non-empty string"
        assert isinstance(exhibition_location, Location), "Invalid exhibition location"
        
        self.title = title.strip()
        self.artist = artist.strip()
        self.date_of_creation = date_of_creation.strip()
        self.historical_significance = historical_significance.strip()
        self.exhibition_location = exhibition_location

        
class ArtworkManagement:
    def __init__(self):
        self.artworks = []

    def add_artwork(self, artwork):
        assert isinstance(artwork, Artwork), "Invalid artwork"
        self.artworks.append(artwork)

    def remove_artwork(self, title):
        assert isinstance(title, str) and title.strip(), "Title must be a non-empty string"
        for artwork in self.artworks:
            if artwork.title == title:
                self.artworks.remove(artwork)
                return True
        return False

    def display_artworks(self):
        return [f"Title: {artwork.title}, Artist: {artwork.artist}, Date of Creation: {artwork.date_of_creation}, Historical Significance: {artwork.historical_significance}, Exhibition Location: {artwork.exhibition_location.name}" for artwork in self.artworks]

