import gradio as gr
import subprocess

def run_app(audio, question):
    if audio is None or question.strip() == "":
        return "Upload audio and ask a question."

    # Existing script run kar rahe hain, koi change nahi
    result = subprocess.run(
        ["python", "voice_rag.py", audio, question],
        capture_output=True,
        text=True
    )

    return result.stdout if result.stdout else result.stderr


with gr.Blocks() as demo:
    gr.Markdown("# 🎤 Voice RAG Assistant")

    audio = gr.Audio(type="filepath", label="Upload Audio")
    question = gr.Textbox(label="Ask a question")
    output = gr.Textbox(label="Answer")

    gr.Button("Submit").click(run_app, [audio, question], output)

demo.launch()
