from pydantic import BaseModel,Field

class CreateMovie(BaseModel):
    title : str = Field(
        min_length= 4,
        max_length= 15,
        description="Movie title",
        example="interstellar"
    )
    director : str = Field(
        min_length= 4,
        max_length=15,
        description="Movie director",
        example="nolan"
    )
    year : int = Field(
        ge=2000,
        le=2026,
        description="Movie year",
        example=2020
    )
    price : int = Field(
        ge=10,
        description="Movie price",
        example=25
    )

class ResponseMovie(CreateMovie):
    id : int

class UpdateMovie(BaseModel):
    title : str | None =  Field(
        None,
        min_length= 4,
        max_length= 15,
        description="Movie title",
        example="interstellar"
    )
    director : str | None =  Field(
        None,
        min_length= 4,
        max_length=15,
        description="Movie director",
        example="nolan"
    )
    year : int | None =  Field(
        None,
        ge=2000,
        le=2026,
        description="Movie year",
        example=2020
    )
    price : int | None =  Field(
        None,
        ge=10,
        description="Movie price",
        example=25
    )

