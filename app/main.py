"""
Main Gradio module.
"""

import gradio as gr

from src import requests


def respond_stream(
    message,
    chat_history,
    api_key,
    model,
    temperature,
    top_p,
    max_tokens,
    system,
):
    response = ""
    received_anything = False
    for chunk in requests.get_stream_chat_completion(
        message=message,
        chat_history=chat_history,
        model=model,
        api_key=api_key,
        temperature=temperature,
        top_p=top_p,
        max_tokens=int(max_tokens),
        system=system if system else None,
    ):
        response += chunk
        yield response
        received_anything = True
    if not received_anything:
        gr.Warning("Error: Invalid API Key")
        yield ""


with gr.Blocks(title="Mistral Playground") as demo:
    with gr.Row():
        api_key = gr.Textbox(lines=1, label="Mistral API Key")
        model = gr.Radio(
            choices=["mistral-tiny", "mistral-small", "mistral-medium"],
            value="mistral-tiny",
        )
    with gr.Row():
        temperature = gr.Slider(
            minimum=0.01, maximum=1.0, step=0.01, label="Temperature"
        )
        top_p = gr.Slider(minimum=0.01, maximum=1.0, step=0.01, label="Top P")
        max_tokens = gr.Slider(
            minimum=1, maximum=4000, step=1, label="Max Tokens", value=100
        )

    with gr.Row():
        system = gr.Textbox(lines=10, label="System Message")
        gr.ChatInterface(
            respond_stream,
            additional_inputs=[
                api_key,
                model,
                temperature,
                top_p,
                max_tokens,
                system,
            ],
        )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=8000,
    )
