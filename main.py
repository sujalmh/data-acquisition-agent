import sys
import asyncio
from fastapi import FastAPI, HTTPException, Depends, Query
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
from fastapi.security.api_key import APIKeyHeader
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

# Set the event loop policy for Windows to support subprocesses.
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

API_KEY = os.getenv("ACQ_API_KEY")
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

app = FastAPI(title="Agent Task Runner")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

def collect_data(task: str):
    agent = Agent(
        task=task,
        llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash"),
    )

    return asyncio.run(agent.run())

@app.get("/sync-task", dependencies=[Depends(verify_api_key)])
def get_data(task: str = Query(..., description="Task to collect data for")):
    data = collect_data(task)
    return {"data": data}
