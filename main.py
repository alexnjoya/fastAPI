from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define a model for the post
class Post(BaseModel):
    title: str
    content: str

# In-memory storage for posts
posts = []

@app.get("/")
async def root():
    return {"message": "Hope you are doing something good today"}

@app.post("/createPost", response_model=Post)
def create_post(post: Post):
    posts.append(post)
    return post

@app.get("/posts", response_model=List[Post])
def get_posts():
    return posts

@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    if post_id >= len(posts) or post_id < 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts[post_id]

@app.delete("/posts/{post_id}", response_model=Post)
def delete_post(post_id: int):
    if post_id >= len(posts) or post_id < 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.pop(post_id)