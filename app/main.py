from fastapi import FastAPI, HTTPException
from helpers.spotify import SpotifyClient
from helpers.convertor import ConvertorClient

# from ytmusic.recommendations import get_recommendations
from ytmusic.search import get_search_results
from app.models import Song

app = FastAPI()
spotify_client = SpotifyClient()
converter = ConvertorClient()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get(
    "/search",
    response_model=list[Song],
    response_description="Returns youtube search result for a query",
)
async def search(query: str, limit: int = 10) -> list[Song]:
    # TODO: use multithreading to stop blocking
    return get_search_results(query, limit)


@app.get(
    "/get_songs_api",
    response_model=list[Song],
    response_description="Returns youtube raw data results of multiple songs using the old api",
)
async def test_api(songs: list[str]) -> list[Song]:
    songs = await converter.get_songs(songs)
    if songs is None:
        raise HTTPException(status_code=404, detail="playlist not found on youtube")
    return songs


@app.get(
    "/get_songs",
    response_model=list[Song],
    response_description="Returns youtube raw data results of multiple songs",
)
async def test(songs: list[str]):
    if not songs:
        raise HTTPException(status_code=400, detail="Song is required")
    return [get_search_results(song, lim=1)[0] for song in songs]


@app.get(
    "/get_song",
    response_model=Song,
    response_description="Returns youtube raw data results of a song",
)
async def get_song(songs: str):
    if not songs:
        raise HTTPException(status_code=400, detail="Song is required")
    return [get_search_results(song, lim=1)[0] for song in songs]


@app.get(
    "/spotify_playlist/{playlist_id}",
    response_model=list[Song],
    response_description="Returns youtube raw data results of songs in a spotify playlist",
)
async def get_spotify_playlist(playlist_id: str):
    # query spotify api for songs in playlist
    songs = await spotify_client.get_songs(playlist_id)
    if songs is None:
        raise HTTPException(status_code=404, detail="playlist not found on spotify")
    songs = [get_search_results(song, lim=1)[0] for song in songs]
    if songs is None:
        raise HTTPException(status_code=404, detail="playlist not found on youtube")
    return songs
