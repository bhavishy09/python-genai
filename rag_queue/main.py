from .server import app
import uvicorn
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent / ".env")

def main():
    uvicorn.run(app, port=8080, host="0.0.0.0")



main()