from drafter import *
from dataclasses import dataclass

hide_debug_information()
set_website_title("Alternative Archive")
set_website_framed(False)

@dataclass
class State:
    library: list[Song]
    search_theme: str
    search_mood:str
    search_genre:str
    result_message:str
    submission_message:str
    
@dataclass
class Song:
    name: str
    artist:str
    theme:str
    mood: str
    genre: str
    
    
@route
def index(state: State) -> Page:
    return Page(state, [
        "Welcome to Alternative Archive!",
        Button("Search", "search"),
        Button("Recommend", "recommend"),
        Button("About", "about_page"),
        ])
@route
def search (state:State)->Page:
    return Page(state,[
        "Find Your Song!",
        "Theme",
        SelectBox("theme",["Romance","Heartbreak","Rebellion","Isolation", "Self-Discovery", "Death", "Desperation", "Loss", "Redemption","Hopelessness", "Appreciation"]),
        "Mood",
        SelectBox("mood", ["Slow", "Upbeat", "Dark", "Angsty","Melancholic"]),
        "Genre",
        SelectBox("genre", [ "Grunge", "Post-Hardcore", "Pop Punk", "Goth", "Shoegaze", "Emotional Hardcore", "Alternative Rock"]),
        Button("Search", "perform_search"),
        ])

@route
def perform_search(state: State, theme: str, mood: str, genre: str)->Page:
    state.search_theme = theme
    state.search_mood = mood
    state.search_genre = genre
    return result(state)

@route
def result (state: State)->Page:
    matching_songs = []
    for song in state.library:
        if song.theme == state.search_theme and song.mood == state.search_mood and song.genre == state.search_genre:
            matching_songs.append(song)
    if len(matching_songs) == 0:
        state.result_message = "No matching songs found."
    else:
        state.result_message = matching_songs[0].name + " by " + matching_songs[0].artist
    return Page(state, [
        "Your Song Is:",
        state.result_message,
        Button("Home", "index"),
        ])

    

@route
def about_page(state:State)-> Page:
    return Page(state, [
        "Welcome to Alternative Archive! This was made as a project for a University Computer Science class with the purpose of helping other alternative music fans find new music that fit their needs easily! I hope you enjoy!!",
        Button("Home", "index")
        ])

@route
def recommend (state:State)-> Page:
    return Page(state, [
        state.submission_message,
        "Name:",
        TextBox("name"),
        "Artist:",
        TextBox("artist"),
        "Theme:",
        SelectBox("theme",["Romance","Heartbreak","Rebellion","Isolation", "Self-Discovery", "Death","Desperation", "Loss", "Redemption","Hopelessness", "Appreciation"]),
        "Mood:",
        SelectBox("mood", ["Slow", "Upbeat", "Dark", "Angsty", "Melancholic"]),
        "Genre:",
        SelectBox("genre", [ "Grunge", "Post-Hardcore" , "Pop Punk", "Goth", "Shoegaze", "Emotional Hardcore", "Alternative Rock"]),
        Button("Submit Song", "add_song"),
        Button("Home", "index"),
        ])
        
@route
def add_song (state: State, name: str, artist: str, theme: str, mood: str, genre: str)->Page:
    if name.strip() == "" or artist.strip() == "":
        state.submission_message = "Please fill in all required fields."
    else:
        new_song = Song(name=name, artist=artist, theme=theme, mood=mood, genre=genre)
        state.library.append(new_song)
        state.submission_message = "Song successfully added to the archive!"
    
    return recommend(state)

                   
initial_songs = [
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
    Song("Alison", "Slowdive", "Desperation", "Slow", "Shoegaze")
]


initial_state = State(
    library=initial_songs,
    search_theme="",
    search_mood="",
    search_genre="",
    result_message="Find Your Song!",
    submission_message=""
)


if __name__ == "__main__":
    start_server(initial_state)
