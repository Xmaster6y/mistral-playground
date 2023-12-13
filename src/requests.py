"""
Module to perform requests to Mistral API.
"""

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def get_stream_chat_completion(
    message, chat_history, model, api_key, system=None, **kwargs
):
    messages = []
    if system is not None:
        messages.append(ChatMessage(role="system", content=system))
    for chat in chat_history:
        human_message, bot_message = chat
        messages.extend(
            (
                ChatMessage(role="user", content=human_message),
                ChatMessage(role="assistant", content=bot_message),
            )
        )
    messages.append(ChatMessage(role="user", content=message))
    client = MistralClient(api_key=api_key)
    for chunk in client.chat_stream(
        model=model,
        messages=messages,
        **kwargs,
    ):
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content
