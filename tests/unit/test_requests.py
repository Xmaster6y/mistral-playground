"""
Module for testing requests.
"""

import os

import pytest

from src import requests


class TestChatCompletion:
    @pytest.mark.api_key_required
    def test_get_stream_chat_completion(self):
        api_key = os.environ.get("MISTRAL_API_KEY")
        generator = requests.get_stream_chat_completion(
            "",
            [["Hello", "Hi"]],
            "mistral-tiny",
            api_key,
            max_tokens=2,
            temperature=0.01,
            top_p=0.01,
        )
        generated_text = "".join(list(generator))
        assert generated_text == "Hello!"

    @pytest.mark.api_key_required
    def test_get_stream_chat_completion_system(self):
        api_key = os.environ.get("MISTRAL_API_KEY")
        generator = requests.get_stream_chat_completion(
            "Hi, who are you?",
            [],
            "mistral-tiny",
            api_key,
            system="You are Mistral AI",
            max_tokens=7,
            temperature=0.01,
            top_p=0.01,
        )
        generated_text = "".join(list(generator))
        assert generated_text == "Hello! I am Mistral AI"

    def test_get_stream_chat_completion_error(self):
        generator = requests.get_stream_chat_completion(
            "",
            [],
            "mistral-tiny",
            "invalid_api_key",
            max_tokens=1,
        )
        with pytest.raises(StopIteration):
            next(generator)
