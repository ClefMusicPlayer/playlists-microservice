import asyncio
from typing import List, Optional


from helpers.config import CLIENT_SECRET, CLIENT_ID


from async_spotify import SpotifyApiClient, spotify_errors
from async_spotify.authentification.authorization_flows import ClientCredentialsFlow


class SpotifyClient:
    def __init__(self):
        auth_flow = ClientCredentialsFlow(
            application_id=CLIENT_ID,
            application_secret=CLIENT_SECRET,
        )
        self.client = SpotifyApiClient(auth_flow, hold_authentication=True)
        self.init = False

    async def initialize(self):
        await self.client.create_new_client()
        await self.client.get_auth_token_with_client_credentials()
        self.init = True

    async def get_songs(self, playlist_id: str) -> Optional[List[str]]:
        if not self.init:
            await self.initialize()
        try:
            tracks = await self.client.playlists.get_tracks(playlist_id)
        except spotify_errors.SpotifyAPIError:
            return None
        if tracks.get("items") is None:
            return None
        songs = []
        for track in tracks["items"]:
            # complex statement to add track name and all artists
            songs.append(
                f"""{track['track']['name']} {" ".join(x['name'] for x in track['track']['artists'])}"""
            )
        return songs


def main():
    loop = asyncio.get_event_loop()
    client = SpotifyClient()
    print(loop.run_until_complete(client.get_songs("3cEYpjA9oz9GiPac4AsH4n")))
    return loop.run_until_complete(client.get_songs("3cEYpjA9oz9GiPac4AsH4n"))


if __name__ == "__main__":
    main()
