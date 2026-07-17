from models.song import Song

SONGS = [
    Song(
        id=1,
        title="Calm Down",
        artist="Rema",
        album="Rave & Roses",
        genre="Afrobeats",
        mood=["happy", "chill", "party"],
        duration=207,
        popularity=95.5,
        release_year=2022
    ),
    Song(
        id=2,
        title="Essence",
        artist="Wizkid",
        album="Made in Lagos",
        genre="Afrobeats",
        mood=["romantic", "chill"],
        duration=253,
        popularity=92.0,
        release_year=2020
    ),
    Song(
        id=3,
        title="Last Last",
        artist="Burna Boy",
        album="Love, Damini",
        genre="Afrobeats",
        mood=["sad", "chill"],
        duration=173,
        popularity=88.0,
        release_year=2022
    ),
    Song(
        id=4,
        title="Midnight City",
        artist="M83",
        album="Hurry Up",
        genre="Electronic",
        mood=["dreamy", "focus", "chill"],
        duration=243,
        popularity=85.0,
        release_year=2011
    ),
    Song(
        id=5,
        title="Power",
        artist="Kanye West",
        album="My Beautiful Dark Twisted Fantasy",
        genre="Hip-Hop",
        mood=["energetic", "motivation"],
        duration=292,
        popularity=90.0,
        release_year=2010
    )
]