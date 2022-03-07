import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

some_file_path = "meteo.json"
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/simulate", response_class=FileResponse)
async def simulate():
    return some_file_path

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
