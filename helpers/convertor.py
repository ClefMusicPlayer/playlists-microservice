import aiohttp


# from server.ytmusic.search import get_search_results


# class Converter:
#     async def get_song(self, song):

#         return get_search_results(query, limit)

#     async def get_songs(self, songs):
#         return [await self.get_song(song) for song in songs]


class ConvertorClient:
    def __init__(self):
        self.base_url = "https://ytmusic-interactions.blitzsite.repl.co/search?query="

    async def get_song(self, song: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url + song) as request:
                raw_data = await request.json()
                if not raw_data:
                    return f"Song not found => {song}"
                else:
                    return raw_data[0]

    async def get_songs(self, songs):
        return [await self.get_song(song) for song in songs]
