from pydantic import BaseModel
from pydantic.fields import Field


class Thumbnail(BaseModel):
    mini: str = Field(
        example="https://lh3.googleusercontent.com/EsHgCaaxJ6ICwcyHym6MoM_G7rols7a4LR7vXLUCQmogkLhfOJJSOUyLTj1u6g7vXxlqtgPJ5A-uzyD6NQ=w60-h60-l90-rj"
    )
    large: str = Field(
        example="https://lh3.googleusercontent.com/EsHgCaaxJ6ICwcyHym6MoM_G7rols7a4LR7vXLUCQmogkLhfOJJSOUyLTj1u6g7vXxlqtgPJ5A-uzyD6NQ=w120-h120-l90-rj"
    )


class Song(BaseModel):
    id: str = Field(example="c_sNBS-9Ras")
    title: str = Field(example="Crab Rave")
    length: str = Field(example="2:42")
    thumbnail: Thumbnail
    artists: list[str] = Field(example=["Noisestorm"])
    link: str = Field(example="https://music.youtube.com/watch?v=c_sNBS-9Ras")
