from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

books=[
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"},]
app=FastAPI()

@app.get("/books")
def get_books():
    return books
class Book(BaseModel):
    title:str
    author:str
@app.post("/book")
def create_book(book:Book):
    new_book=book.model_dump()
    books.append(new_book) 
    return new_book
class BookUpdate(BaseModel):
    title:str
    author:str
@app.put("/book/{book_id}")
def update_book(book_id:int,book:BookUpdate):
    for b in books:
        if b["id"]==book_id:
            b["title"]=book.title
            b["author"]=book.author
            return b
    raise HTTPException(status_code=404,detail="Book not found")  
@app.delete("/book/{book_id}")
def delete_book(book_id:int):
    for b in books:
        if b["id"]==book_id:
            books.remove(b)
            return {"message":"Book deleted successfully"}
    raise HTTPException(status_code=404,detail="Book not found")  
