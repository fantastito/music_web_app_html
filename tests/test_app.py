from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums_(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    header_tag = page.locator("h1")
 
    expect(header_tag).to_have_text("Albums")
    expect(div_tags).to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1988",
        "Title: Waterloo\nReleased: 1974",
        "Title: Super Trouper\nReleased: 1980",
        "Title: Bossanova\nReleased: 1990",
        "Title: Lover\nReleased: 2019",
        "Title: Folklore\nReleased: 2020",
        "Title: I Put a Spell on You\nReleased: 1965",
        "Title: Baltimore\nReleased: 1978",
        "Title: Here Comes the Sun\nReleased: 1971",
        "Title: Fodder on My Wings\nReleased: 1982",
        "Title: Ring Ring\nReleased: 1973",
    ])

def test_get_albums_id_1(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text("Doolittle")
    expect(p_tags).to_have_text([
        "Release year: 1989",
        "Artist: Pixies",
    ])

def test_albums_have_link(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")
    p_tags = page.locator("p")
    expect(p_tags).to_have_text([
        "Release year: 1988",
        "Artist: Pixies",
    ])

"""
Challenge
1. Add a route GET /artists/<id> which returns an HTML page showing details for a single artist.
    - Decide what artist HTML page will look like: artist name in title, genre in paragraph
    - Write test (similar to test for album)
    - Write app route
    - Write ArtistRepo method (if needed)
    - Write HTML template
2. Add a route GET /artists which returns an HTML page with the list of artists. This page should contain a link for each artist listed, linking to /artists/<id> where <id> needs to be the corresponding artist id.
"""

def test_get_artist_id_1(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text("Pixies")
    expect(p_tags).to_have_text("Genre: Rock")

#Let's just make this repo mine and do some adds/commits
#The repo is still cloned from the starter