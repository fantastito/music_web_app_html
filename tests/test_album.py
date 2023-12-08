from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Title", 2001, 3)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2001
    assert album.artist_id == 3

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 2001, 3)
    assert str(album) == "Album(1, Test Title, 2001, 3)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albumss_are_equal():
    album2 = Album(1, "Test Title", 2001, 3)
    album1 = Album(1, "Test Title", 2001, 3)
    assert album1 == album2