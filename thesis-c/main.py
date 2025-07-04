from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
import asyncio
from typing import List, Dict
import json

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FINE_TUNED_MODELS = {
    "Normal": "",
    "65-year-old female": "",
    "20-year-old female": "",
}

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    message = body["message"]
    history = body.get("history", [])
    persona = body["persona"]
    model_id = FINE_TUNED_MODELS[persona]

    async def stream_response():
        try:
            messages = []
            messages.append(
                {"role": "system", "content": "You are an expert Ayurvedic assistant."}
            )
            for user, assistant in history:
                messages.append({"role": "user", "content": user})
                messages.append({"role": "assistant", "content": assistant})
            messages.append({"role": "user", "content": message})

            stream = openai.chat.completions.create(
                model=model_id,
                messages=messages,
                temperature=0.7,
                stream=True,
            )
            full_response = ""
            for chunk in stream:
                delta = getattr(chunk.choices[0].delta, "content", "")
                if delta is not None:
                    full_response += str(delta)
                    yield f"data:{json.dumps({'token': delta})}\n\n"
            yield f"data:{json.dumps({'done': True, 'full_response': full_response})}\n\n"
        except Exception as e:
            import traceback

            print("Exception in stream_response:", e)
            traceback.print_exc()
            yield f"data:{json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(stream_response(), media_type="text/event-stream")
