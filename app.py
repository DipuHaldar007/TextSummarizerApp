from pathlib import Path
import re

import torch
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Project directory
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "saved_summary_model"

# Initialize FastAPI
app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)

# Load model and tokenizer
model = T5ForConditionalGeneration.from_pretrained(str(MODEL_DIR))
tokenizer = T5Tokenizer.from_pretrained(str(MODEL_DIR))

# Select device
if torch.cuda.is_available():
    device = torch.device("cuda")
elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

model.to(device)
model.eval()

# HTML templates
templates = Jinja2Templates(directory=str(BASE_DIR))


# Input schema
class DialogueInput(BaseModel):
    dialogue: str


# Clean text
def clean_data(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# Summarization function
def summarize_dialogue(dialogue: str) -> str:
    dialogue = clean_data(dialogue)

    if not dialogue:
        raise ValueError("Please enter some dialogue.")

    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    with torch.inference_mode():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=150,
            num_beams=4,
            early_stopping=True
        )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


# API endpoint
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    try:
        summary = summarize_dialogue(dialogue_input.dialogue)
        return {"summary": summary}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )
