from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from typing import Optional

app = FastAPI()
 # key = "219725bbkborbourrp2cd4";

# Allow CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Server running"}

@app.get("/dood_random")
async def get_dood_random(page: int, per_page: int, key: str,fld_id: Optional[str] = None):
    url = f"https://doodapi.com/api/file/list?key={key}&page={page}&per_page={per_page}&fld_id={fld_id}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/dood_info")
async def get_dood_info(file_code: str, key: str):
    url = f"https://doodapi.com/api/file/info?key={key}&file_code={file_code}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@app.get("/dood_cari")
async def get_dood_cari(search_term: str, key: str):
    url = f"https://doodapi.com/api/search/videos?key={key}&search_term={search_term}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

