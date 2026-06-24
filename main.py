from fastapi import FastAPI,status,HTTPException,Path,Query
from .basemodel2 import CreateMovie,ResponseMovie,UpdateMovie

app = FastAPI()

movies = []

@app.post("/movies",response_model=ResponseMovie,status_code=status.HTTP_201_CREATED)
def add_movie(movie : CreateMovie):
    data_movie = movie.model_dump()
    data_movie["id"] = len(movies) + 1
    data_movie["secret"] = "admin"
    movies.append(data_movie)
    return data_movie

@app.get("/movies",response_model=list[ResponseMovie])
def show_movies(min_price : int | None = Query(None,ge=10,description="Serch by price",example=25),
                search : str | None = Query(None,min_length=4,max_length=15,description="Search by name")):
    result = movies
    if min_price:
        result = [movie for movie in result if movie["price"] >= min_price]
    if search:
        result = [movie for movie in result if search.lower() in movie["title"].lower()]
    return result
@app.get("/movies/{id}",response_model=ResponseMovie)
def search_movie(id:int = Path(ge=1,description="Movie id",example=5)):
    for movie in movies:
        if movie["id"] == id:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

@app.put("/movies/update/{id}",status_code=status.HTTP_200_OK,response_model=ResponseMovie)
def edit_book(update_data : UpdateMovie , id:int = Path(ge=1,description="Movie id",example=5)):
    for movie in movies:
        if movie["id"] == id:
            update_field = update_data.model_dump(exclude_unset=True)
            for key,value in update_field.items():
                movie[key] = value
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

@app.delete("/movies/delete/{id}",status_code=status.HTTP_200_OK)
def delete_book(id:int = Path(ge=1,description="Movie id",example=5)):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"detail":"deleted"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
            


