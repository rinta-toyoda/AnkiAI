# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictBytes, StrictStr, field_validator  # noqa: F401
from typing import List, Optional, Tuple, Union  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from ankiai_generated.models.error_response import ErrorResponse  # noqa: F401
from ankiai_generated.models.generate_response import GenerateResponse  # noqa: F401
from ankiai_generated.models.generate_text_request import GenerateTextRequest  # noqa: F401


def test_generate_media(client: TestClient):
    """Test case for generate_media

    Generate flashcard content from text prompt and images
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    data = {
        "prompt": 'prompt_example',
        "target_lang": 'target_lang_example',
        "with_tts": False,
        "max_terms": 10,
        "max_meanings_per_term": 3,
        "images": ['/path/to/file']
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/generateMedia",
    #    headers=headers,
    #    data=data,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generate_text(client: TestClient):
    """Test case for generate_text

    Generate flashcard content from text prompt
    """
    generate_text_request = {"target_lang":"zh-CN","max_terms":4,"max_meanings_per_term":6,"with_tts":0,"prompt":"HSK2向けに『替・觉得・认为』。各語義ごとに短義＋例文を。"}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/generateText",
    #    headers=headers,
    #    json=generate_text_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

