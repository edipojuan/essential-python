from fastapi import FastAPI
import httpx
import uvicorn

app = FastAPI()

def main():
    uvicorn.run("essential_python.fastapi:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/")
async def root():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/users/edipojuan")
    return {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "test": { "name": "test 123" },
    }