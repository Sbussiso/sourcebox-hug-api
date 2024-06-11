# main.py
from fastapi import FastAPI, Query
from transformers import pipeline
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"response": "API connection successful!"}
    


@app.get("/sent-pipe")
def sent_pipe(prompt: str = Query(..., prompt="The prompt to analyze")):
    sentiment_pipeline = pipeline("sentiment-analysis")
    data = [prompt]
    pipe = sentiment_pipeline(data)
    print(pipe)
    return {"response": str(pipe)}