"""Base class for Content Generation API."""
from typing import List, Optional
from abc import ABC, abstractmethod
from fastapi import UploadFile
from pydantic import StrictBool, StrictStr

from ankiai_generated.models.generate_response import GenerateResponse
from ankiai_generated.models.generate_text_request import GenerateTextRequest


class BaseContentGenerationApi(ABC):
    """Base class for Content Generation API implementation."""

    @abstractmethod
    async def generate_text(
        self,
        generate_text_request: GenerateTextRequest,
    ) -> GenerateResponse:
        """Generate flashcard content from text prompt."""
        pass

    @abstractmethod
    async def generate_media(
        self,
        target_lang: StrictStr,
        prompt: Optional[StrictStr] = None,
        with_tts: Optional[StrictBool] = None,
        max_terms: Optional[int] = None,
        max_meanings_per_term: Optional[int] = None,
        images: Optional[List[UploadFile]] = None,
    ) -> GenerateResponse:
        """Generate flashcard content from text prompt and images."""
        pass