"""
Content Generation API endpoints that extend the generated OpenAPI code.

This module imports the generated base classes and extends them with
actual implementation. The generated code should NOT be modified.
"""

import sys
import os
from typing import List, Optional
from fastapi import APIRouter, File, Form, UploadFile
from pydantic import Field, StrictBool, StrictStr
from typing_extensions import Annotated

# Add the generated code to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../generated/src'))

# Import generated models and base classes
from ankiai_generated.models.generate_response import GenerateResponse
from ankiai_generated.models.generate_text_request import GenerateTextRequest
from ankiai_generated.apis.content_generation_api_base import BaseContentGenerationApi

router = APIRouter()

class ContentGenerationImpl(BaseContentGenerationApi):
    """Implementation of the generated ContentGeneration API base class."""

    async def generate_text(
        self,
        generate_text_request: GenerateTextRequest,
    ) -> GenerateResponse:
        """
        Generate flashcard content from text prompt.

        TODO: Implement content generation logic here.
        """
        # This is where you will add your implementation logic later
        raise NotImplementedError("Content generation logic not implemented yet")

    async def generate_media(
        self,
        target_lang: Annotated[StrictStr, Field(description="Target language code (ISO 639-1)")],
        prompt: Annotated[Optional[StrictStr], Field(description="Optional text prompt for generating flashcard content")],
        with_tts: Annotated[Optional[StrictBool], Field(description="Whether to generate text-to-speech audio")],
        max_terms: Annotated[Optional[int], Field(description="Maximum number of terms to generate")],
        max_meanings_per_term: Annotated[Optional[int], Field(description="Maximum number of meanings per term")],
        images: Annotated[Optional[List[UploadFile]], Field(description="Array of image files (1 to 10 files supported)")],
    ) -> GenerateResponse:
        """
        Generate flashcard content from text prompt and images.

        TODO: Implement media processing and content generation logic here.
        """
        # This is where you will add your implementation logic later
        raise NotImplementedError("Media content generation logic not implemented yet")

# Create an instance of the implementation
content_impl = ContentGenerationImpl()

# Define the FastAPI routes that call the implementation
@router.post("/generateText", response_model=GenerateResponse)
async def generate_text_endpoint(request: GenerateTextRequest) -> GenerateResponse:
    """Generate flashcard content from text prompt."""
    return await content_impl.generate_text(request)

@router.post("/generateMedia", response_model=GenerateResponse)
async def generate_media_endpoint(
    targetLang: str = Form(..., description="Target language code"),
    prompt: Optional[str] = Form(None, description="Optional text prompt"),
    withTTS: Optional[bool] = Form(False, description="Whether to generate TTS audio"),
    maxTerms: Optional[int] = Form(10, description="Maximum number of terms"),
    maxMeaningsPerTerm: Optional[int] = Form(3, description="Maximum meanings per term"),
    images: List[UploadFile] = File(..., description="Image files (1-10 files)")
) -> GenerateResponse:
    """Generate flashcard content from text prompt and images."""
    return await content_impl.generate_media(
        target_lang=targetLang,
        prompt=prompt,
        with_tts=withTTS,
        max_terms=maxTerms,
        max_meanings_per_term=maxMeaningsPerTerm,
        images=images
    )