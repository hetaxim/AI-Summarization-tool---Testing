
import gradio as gr
from transformers import pipeline
from datetime import datetime
import os

# File export path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "summaries.txt")

# Load model once
summarizer = pipeline(
    task="summarization",
    model="sshleifer/distilbart-cnn-12-6",
)

print("✅ Model loaded successfully!")

# Themes
light_theme = gr.themes.Soft(primary_hue="blue")
dark_theme = gr.themes.Glass(primary_hue="blue")

def summarize_and_save(text):
    if not text or not text.strip():
        return "Please enter some text."

    result = summarizer(
        text,
        max_length=1000,
        min_length=20,
        do_sample=False
    )

    summary_text = result[0]["summary_text"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write("\n--- NEW SUMMARY ---\n")
        f.write(f"Time: {timestamp}\n\n")
        f.write("INPUT:\n")
        f.write(text.strip() + "\n\n")
        f.write("SUMMARY:\n")
        f.write(summary_text + "\n")

    return summary_text

demo = gr.Interface(
    fn=summarize_and_save,
    inputs=gr.Textbox(lines=8, label="Input Text"),
    outputs=gr.Textbox(lines=5, label="Summary"),
    title="Text Summarization Demo",
    #description="Dark theme – Hugging Face + Gradio",
    theme=dark_theme   # ✅ change to light_theme if needed
)

demo.launch()
