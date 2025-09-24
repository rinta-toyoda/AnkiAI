# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictBytes, StrictStr, field_validator
from typing import List, Optional, Tuple, Union
from typing_extensions import Annotated
from ankiai_generated.models.error_response import ErrorResponse
from ankiai_generated.models.generate_response import GenerateResponse
from ankiai_generated.models.generate_text_request import GenerateTextRequest
from ankiai_generated.security_api import get_token_BearerAuth

class BaseContentGenerationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseContentGenerationApi.subclasses = BaseContentGenerationApi.subclasses + (cls,)
    async def generate_media(
        self,
        target_lang: Annotated[StrictStr, Field(description="Target language code (ISO 639-1)")],
        prompt: Annotated[Optional[StrictStr], Field(description="Optional text prompt for generating flashcard content")],
        with_tts: Annotated[Optional[StrictBool], Field(description="Whether to generate text-to-speech audio")],
        max_terms: Annotated[Optional[Annotated[int, Field(le=50, strict=True, ge=1)]], Field(description="Maximum number of terms to generate")],
        max_meanings_per_term: Annotated[Optional[Annotated[int, Field(le=10, strict=True, ge=1)]], Field(description="Maximum number of meanings per term")],
        images: Annotated[Optional[Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(min_length=1, max_length=10)]], Field(description="Array of image files (1 to 10 files supported)")],
    ) -> GenerateResponse:
        """Generate vocabulary flashcards with audio from a text prompt and uploaded images"""
        ...


    async def generate_text(
        self,
        generate_text_request: GenerateTextRequest,
    ) -> GenerateResponse:
        """Generate vocabulary flashcards with audio from a text prompt"""
        ...
