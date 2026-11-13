from drafter import *
import random
from dataclasses import dataclass
from bakery import assert_equal

set_website_title("Alternative Archive")
set_site_information(
    author="Camila L. Rios",
    description="Recommends user a song that matches the spcific theme, mood, and genre they imputed",
    sources="Drafter Documentation, Past Projects, Gemini (LLM), I also used google, chatgpt, reddit, and my spotify to help come up with the original song library. Most of these songs arein my playlist, I googled them and based on reddit reviews and what google said I matchedattributes to them",
    planning=["plan.pdf", "design.pdf"],
    links=["https://github.com/camttrios/Alternative-Archive-Project-"]
)
hide_debug_information()
set_website_framed(False)

@dataclass
class Song:
    name: str
    artist:str
    theme:str
    mood: str
    genre: str
    

@dataclass
class State:
    library: list[Song]
    search_theme: str
    search_mood:str
    search_genre:str
    result_message:str
    submission_message:str   

INITIAL_SONGS = [
    Song("Breed","Nirvana","Rebellion","Angsty", "Grunge"),
    Song("Disintegration", "The Cure","Heartbreak", "Dark","Goth"),
    Song("Tidal Wave: Breakfast, Lunch, and Dinner", "Dance Gavin Dance", "Isolation", "Angsty", "Post-Hardcore"),
    Song("Headfirst for Halos","My Chemical Romance", "Death", "Upbeat", "Pop Punk"),
    Song("XO","Fall Out Boy", "Desperation", "Angsty", "Pop Punk"),
    Song("Star No Star", "Jack Off Jill", "Heartbreak", "Dark", "Alternative Rock"),
    Song("Lying Is the Most Fun a Girl Can Have Without Taking Her Clothes Off", "Panic! At The Disco", "Desperation", "Angsty", "Pop Punk"),
    Song("Saturday", "Fall Out Boy", " Self-Discovery", "Upbeat", "Alternative Rock"),
    Song("Evil", "Interpol","Loss","Melancholic","Alternative Rock"),
    Song("In Circles", "Sunny Day Real Estate", "Isolation", "Melancholic", "Emotional Hardcore"),
    Song("For Want Of", "Rites of Spring", "Desperation", "Angsty", "Emotional Hardcore"),
    Song("Tears Through Tyranny","April's Love Affair",  "Hopelessness" , "Slow", "Post-Hardcore"),
    Song("Not The American Average", "Asking Alexandria", "Rebellion", "Angsty", "Post-Hardcore"),
    Song("Stab", "Title Fight", "Heartbreak", "Angsty", "Post-Hardcore"),
    Song("Room 409", "Bullet For My Valentine", "Heartbreak", "Angsty", "Post-Hardcore"),
    Song("For You I'll Pull the Trigger", "Arranged in April", "Desperation", "Melancholic", "Post-Hardcore"),
    Song("Charlotte", "Kittie", "Death", "Dark", "Grunge"),
    Song("Stars", "Hum", "Isolation", "Slow", "Shoegaze"),
    Song("Knowing That You've Already Arrived", "Tides Of Man", "Self-Discovery", "Upbeat", "Post-Hardcore"),
    Song("Accidental Obsession", "Amarionette", "Romance", "Upbeat", "Post-Hardcore"),
    Song("Rose & Web", "Fearing", "Loss", "Dark", "Goth"),
    Song("We Treat the Blindness", "Strange Boutique", "Hopelessness","Dark", "Goth"),
    Song("The Importance of Cocaine", "Dance Gavin Dance", "Desperation", "Melancholic", "Post-Hardcore"),
    Song("Perfect", "Dance Gavin Dance", "Heartbreak", "Slow", "Post-Hardcore"),
    Song("Cancer", "My Chemical Romance","Death","Melancholic","Pop Punk"),
    Song("Grenade Jumper", "Fall Out Boy", "Appreciation", "Upbeat", "Pop Punk"),
    Song("Dissipate", "Buried In Spring", "Loss", "Melancholic", "Post-Hardcore"),
    Song("She Burned Me Down", "Type O Negative", "Heartbreak", "Slow", "Goth"),
    Song("Shame", "Stabbing Westward","Heartbreak","Angsty", "Alternative Rock"),
    Song("Hope", "Ashbury Heights", "Redemption", "Upbeat", "Goth"),
    Song("Hum Hallelujah", "Fall Out Boy", "Redemption", "Upbeat", "Pop Punk"),
    Song("I Changed My Name", "Sugarcult", "Self-Discovery", "Upbeat", "Pop Punk"),
    Song ("Join Me In Death", "HIM", "Romance", "Slow", "Goth" ),
    Song("Sunday", "Sonic Youth", "Self-Discovery", "Melancholic", "Alternative Rock"),
    Song("Sunburn", "Muse", "Desperation", "Angsty", "Alternative Rock"),
    Song("Summertime", "The Sundays", "Romance", "Upbeat", "Alternative Rock"),
    Song("The Razor's Apple", "Fleshwater","Hopelessness", "Angsty", "Shoegaze"),
    Song("Falling Down","Chapterhouse", "Isolation", "Upbeat","Shoegaze"),
    Song("Dagger", "Slowdive", "Heartbreak", "Slow", "Shoegaze"),
    Song("Change", "The Lightning Seeds", "Self-Discovery", "Upbeat", "Alternative Rock"),
    Song("Snakedriver", "The Jesus and Mary Chain", "Desperation", "Dark", "Grunge"),
    Song("I Will Bury You A New Life", "Everclear", "Appreciation", "Upbeat", "Grunge"),
    Song("I Stay Away", "Alice In Chains", "Isolation", "Melancholic", "Grunge"),
    Song("Forever", "Siouxsie and the Banshees", "Heartbreak", "Slow", "Goth"),
    Song("Happy house", "Siouxsie and the Banshees", "Isolation", "Upbeat", "Goth"),
    Song("Clairvoyant", "The Story So Far", "Loss", "Slow", "Alternative Rock"),
    Song("Closer", "Nine Inch Nails", "Desperation", "Dark", "Alternative Rock"),
    Song( "No One Knows", "Queens of the Stone Age", "Rebellion", "Upbeat", "Alternative Rock"),
    Song("Eyes", "Sans Seraph", "Loss", "Slow", "Shoegaze"),
    Song("Like a Ghost", "The High Court", "Heartbreak", "Upbeat", "Pop Punk"),
    Song("Jeanuary 1979","mewithoutYou", "Death", "Dark", "Emotional Hardcore"),
    Song("Climbing Up the Walls", "Radiohead", "Self-Discovery", "Dark", "Alternative Rock"),
    Song("Black No.1 (Little Miss Scare-All)", "Type O Negative", "Rebellion", "Angsty", "Goth"),
    Song("When You Sleep", "My Bloody Valentine", "Appreciation", "Slow", "Shoegaze"),
    Song("King Park", "La Dispute", "Redemption", "Dark", "Emotional Hardcore"),
    Song("Hurt", "Nine Inch Nails", "Redemption", "Slow", "Alternative Rock"),
    Song("Swing Life Away", "Rise Against", "Redemption", "Melancholic", "Pop Punk"),
    Song("Black Hole Sun", "Soundgarden", "Loss", "Dark", "Alternative Rock"),
    Song("Jesus of Suburbia", "Green Day", "Rebellion", "Melancholic", "Pop Punk"),
    Song("Everlong", "Foo Fighters", "Appreciation", "Upbeat", "Grunge"),
    Song("Leave Them All Behind","Ride", "Death", "Dark", "Shoegaze"),
    Song("Rooster","Alice In Chains","Self-Discovery","Dark", "Grunge"),
    Song("Only Shallow", "My Bloody Valentine", "Loss", "Upbeat", "Shoegaze"),
    Song("Sweetness", "Jimmy Eat World", "Desperation", "Upbeat", "Emotional Hardcore"),
    Song("Alison", "Slowdive", "Desperation", "Slow", "Shoegaze"),
    Song("Dance, Dance", "Fall Out Boy", "Desperation", "Upbeat", "Pop Punk"),
    Song("Nutshell","Alice In Chains","Desperation", "Melancholic","Grunge"),
    Song("Float On","Modest Mouse","Loss","Upbeat","Alternative Rock"),
    Song("The Middle","Jimmy Eat World","Self-Discovery", "Upbeat", "Emotional Hardcore"),
    Song("Second & Sebring","Of Mice & Men","Redemption", "Dark", "Post-Hardcore"),
    Song("Helena","My Chemical Romance", "Death", "Angsty", "Post-Hardcore"),
    Song("A Forest","The Cure","Loss", "Angsty","Goth"),
    Song("Such Great Heights","The Postal Service","Isolation", "Upbeat", "Emotional Hardcore"),
    Song("American Idiot","Green Day","Rebellion", "Dark", "Pop Punk"),
    Song("Yellow","Coldplay", "Appreciation", "Melancholic", "Alternative Rock"),
    Song("Bela Lugosi's Dead","Bauhaus","Hopelessness", "Upbeat", "Goth"),
    Song("When the Sun Hits", "Slowdive", "Hopelessness", "Slow", "Shoegaze"),
    Song("Never Meant","American Football","Hopelessness", "Slow", "Emotional Hardcore"),
    Song("Adam's Song", "Blink-182", "Hopelessness", "Melancholic", "Pop Punk"),
    Song("About a Girl","Nirvana", "Romance", "Melancholic", "Grunge"),
    Song("Heaven or Las Vegas","Cocteau Twins", "Romance", "Upbeat", "Shoegaze"),
    Song("Konstantine","Something Corporate","Romance", "Slow", "Pop Punk"),
    Song("Understanding in a Car Crash","Thursday","Self-Discovery", "Melancholic", "Post-Hardcore"),
    Song("Allegations", "We're Not Friends Anymore","Heartbreak","Angsty","Post-Hardcore"),
    Song("Holding Someone's Hair Back", "Circa Survive","Desperation","Melancholic","Post-Hardcore"),
    Song("Bullet Holes in Concrete", "This Armistice","Isolation","Angsty","Post-Hardcore"),
    Song("Heaven Runs on Oil","Nightmare Of You", "Rebellion", "Upbeat","Alternative Rock"),
    Song("Gemini","Nova Charisma","Heartbreak","Angsty","Post-Hardcore"),
    Song("Pueblo Cicada", "Lower Definition","Desperation","Angsty","Post-Hardcore"),
    Song("Build God, Then We'll Talk", "Panic! At the Disco", "Hopelessness","Upbeat","Pop Punk"),
    Song("Drunken Lament", "Ludo","Hopelessness","Melancholic","Pop Punk"),
    Song("The Nerve", "The Brobecks","Desperation","Upbeat","Alternative Rock"),
    Song("Decode", "Paramore", "Desperation", "Angsty", "Alternative Rock"),
    Song("Domino Effect", "Ozma", "Self-Discovery", "Upbeat","Alternative Rock"),
    Song("Don't Wake Me Up", "The Hush Sound","Hopelessness","Melancholic","Alternative Rock"),
    Song("Maya the Psychic","Gerard Way","Hopelessness","Upbeat","Alternative Rock"),
    Song("Great Party", "Frank Iero", "Isolation", "Angsty", "Post-Hardcore"),
    Song("Los Angeles", "Sugarcult", "Loss","Upbeat","Pop Punk"),
    Song("17 Crimes", "AFI", "Rebellion","Dark","Post-Hardcore"),
    Song("If Looks Could Kill", "A Heartwell Ending", "Romance","Angsty","Pop Punk"),
    Song("Bulls Make Money, Bears Make Money, Pigs Get Slaughtered", "Chiodos", "Rebellion","Angsty","Post-Hardcore"),
    Song("Where I Started", "Danger Radio", "Self-Discovery", "Upbeat","Pop Punk"),
    Song("Listen to Me", "Appleseed", "Desperation", "Melancholic", "Emotional Hardcore"),
    Song("Got a thing for being stupid", "Lady Radiator","Self-Discovery","Upbeat","Post-Hardcore"),
    Song("I'd Do Anything", "Simple Plan", "Desperation","Upbeat","Pop Punk"),
    Song("Tastes Like Honey", "Swallow", "Romance","Slow","Shoegaze"),
    Song("Drain Cosmetics", "Serena-Maneesh","Isolation","Dark","Shoegaze"),
    Song("Tonight, Tonight", "The Smashing Pumpkins","Redemption","Upbeat","Alternative Rock"),
    Song("Digital Bath", "Deftones","Death","Dark","Alternative Rock"),
    Song("Trying to Escape the Inevitable", "Pencey Prep","Hopelessness","Angsty","Post-Hardcore"),
    Song("The Concept", "Teenage Fanclub","Heartbreak","Upbeat","Alternative Rock"),
    Song("Gekka no Yasoukyoku", "Malice Mizer", "Death", "Upbeat", "Goth")
    
    
]


    
@route
def index(state: State) -> Page:
    return Page(state, [
        "Welcome to Alternative Archive!",
        Button("Search", "search"),
        Button("Recommend", "recommend"),
        Button("About", "about_page"),
        ])
''' 
This function is the route function that takes the user to the home page of the website
Parameters:
state: State
Returns:
a page (Home)
'''
@route
def search (state:State)->Page:
    return Page(state,[
        "Find Your Song!",
        "Theme",
        SelectBox("theme",["Romance","Heartbreak","Rebellion","Isolation", "Self-Discovery", "Death", 
                           "Desperation", "Loss", "Redemption","Hopelessness", "Appreciation"]),
        "Mood",
        SelectBox("mood", ["Slow", "Upbeat", "Dark", "Angsty","Melancholic"]),
        "Genre",
        SelectBox("genre", [ "Grunge", "Post-Hardcore", "Pop Punk", "Goth", "Shoegaze", "Emotional Hardcore", "Alternative Rock"]),
        Button("Search", "perform_search"),
        ])
''' 
This function is the route function that takes the user to the search page of the website in which the user can
select which theme, mood, and genre they want the song they are matched with to have. The Search page has the Search button
which inplements the perform_search route
Parameters:
state: State
Returns:
a page (Search)
'''
@route
def perform_search(state: State, theme: str, mood: str, genre: str)->Page:
    state.search_theme = theme
    state.search_mood = mood
    state.search_genre = genre
    return result(state)

'''
This function is the route function that updates the state's search_theme, search_mood and search_genre parameters
based on what the user had selected in the Search
page before hitting the search button
Parameters:
state: State
theme:str
mood:str
genre:str
Returns:
Page (Result)
'''

@route
def result (state: State)->Page:
    matching_songs = []
    for song in state.library:
        if song.theme == state.search_theme and song.mood == state.search_mood and song.genre == state.search_genre:
            matching_songs.append(song)
    if len(matching_songs) == 0:
        state.result_message = "No matching songs found."
    else:
        song_picked = random.choice(matching_songs)
        state.result_message = song_picked.name + " by " + song_picked.artist
    return Page(state, [
        "Your Song Is:",
        state.result_message,
        Button("Home", "index"),
        ])

''' 
The result route is the function that allows the user to see their result and is implemented in perform_search. 
The function matches the state search_theme, search_mood, and search_genre to songs in the state.library with the same attributes. 
If no songs are matched the route updates the result_message to "No Mathching songs foud", if there are morethan one match,
the function will pick a random song from the list of matched songs
Parameters:
state:State
Returns:
Page
'''

@route
def about_page(state:State)-> Page:
    return Page(state, [
        "Welcome to Alternative Archive! This was made as a project for a University Computer Science class with the purpose of helping other alternative music fans find new music that fit their needs easily! I hope you enjoy!!",
        Button("Home", "index")
        ])
    
    ''' 
This function is the route function that takes the user to the about page of the website
Parameters:
state: State
Returns:
a page (About)
'''

@route
def recommend (state:State)-> Page:
    return Page(state, [
        state.submission_message,
        "Name:",
        TextBox("name"),
        "Artist:",
        TextBox("artist"),
        "Theme:",
        SelectBox("theme",["Romance","Heartbreak","Rebellion","Isolation", "Self-Discovery", "Death","Desperation", "Loss", 
                           "Redemption","Hopelessness", "Appreciation"]),
        "Mood:",
        SelectBox("mood", ["Slow", "Upbeat", "Dark", "Angsty", "Melancholic"]),
        "Genre:",
        SelectBox("genre", [ "Grunge", "Post-Hardcore" , "Pop Punk", "Goth", "Shoegaze", "Emotional Hardcore", "Alternative Rock"]),
        Button("Submit Song", "add_song"),
        Button("Home", "index"),
        ])
    ''' 
This function is the route function that takes the user to the recommend page of the website in which the user can
imput a song by entering its name, artists and selection a theme, mood, and genre for the song.
Once they hit submit song, the button will implement the add_song route.
Parameters:
state: State
Returns:
a page (recommend)
'''
        
@route
def add_song (state: State, name: str, artist: str, theme: str, mood: str, genre: str)->Page:
    if name.strip() == "" or artist.strip() == "":
        state.submission_message = "Please fill in all required fields."
    else:
        new_song = Song(name=name, artist=artist, theme=theme, mood=mood, genre=genre)
        state.library.append(new_song)
        state.submission_message = "Song successfully added to the archive!"
    
    return recommend(state)

'''
This function is the route function that creates a new Song datalcass and updates its search_theme, search_mood and search_genre parameters
based on what the user had selected in the recommend page before hitting the Submit song button and appends it to the state's library. 
Parameters:
state: State
name:str
artist:str
theme:str
mood:str
genre:str
Returns:
Page (Recommend)
'''


initial_state = State(
    library=INITIAL_SONGS.copy(),
    search_theme="",
    search_mood="",
    search_genre="",
    result_message="Find Your Song!",
    submission_message=""
)


if __name__ == "__main__":
    start_server(initial_state)

#unit tests
test_state = State(
    library = [Song("Vampires Will Never Hurt You", "My Chemical Romance", "Isolation", "Angsty", "Pop Punk"), Song("Pretty Punk", "Fall Out Boy", "Romance", "Upbeat", "Pop Punk")],
    search_theme="",
    search_mood="",
    search_genre="",
    result_message="Find Your Song!",
    submission_message=""
    )
perform_search(test_state, "Isolation","Angsty", "Pop Punk")
assert_equal(
