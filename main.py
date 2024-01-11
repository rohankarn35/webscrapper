from fastapi import FastAPI, Depends
from scrapper import Scrapper
app = FastAPI()

quotes = Scrapper()

@app.get("/{cat}")

async def home(cat:str ,scrapper: Scrapper = Depends()):
    return quotes.scrappeddata(cat)