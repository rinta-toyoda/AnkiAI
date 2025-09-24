# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from ankiai_generated.apis.content_generation_api_base import BaseContentGenerationApi
import ankiai_generated.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from ankiai_generated.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBool, StrictBytes, StrictStr, field_validator
from typing import List, Optional, Tuple, Union
from typing_extensions import Annotated
from ankiai_generated.models.error_response import ErrorResponse
from ankiai_generated.models.generate_response import GenerateResponse
from ankiai_generated.models.generate_text_request import GenerateTextRequest
from ankiai_generated.security_api import get_token_BearerAuth

router = APIRouter()

ns_pkg = ankiai_generated.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/generateMedia",
    responses={
        200: {"model": GenerateResponse, "description": "Successfully generated flashcard content"},
        400: {"model": ErrorResponse, "description": "Bad request - invalid input parameters or files"},
        413: {"model": ErrorResponse, "description": "Payload too large - file size exceeds limits"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    tags=["content-generation"],
    summary="Generate flashcard content from text prompt and images",
    response_model_by_alias=True,
)
async def generate_media(
    target_lang: Annotated[StrictStr, Field(description="Target language code (ISO 639-1)")] = Form(None, description="Target language code (ISO 639-1)"),
    prompt: Annotated[Optional[StrictStr], Field(description="Optional text prompt for generating flashcard content")] = Form(None, description="Optional text prompt for generating flashcard content"),
    with_tts: Annotated[Optional[StrictBool], Field(description="Whether to generate text-to-speech audio")] = Form(False, description="Whether to generate text-to-speech audio"),
    max_terms: Annotated[Optional[Annotated[int, Field(le=50, strict=True, ge=1)]], Field(description="Maximum number of terms to generate")] = Form(10, description="Maximum number of terms to generate", ge=1, le=50),
    max_meanings_per_term: Annotated[Optional[Annotated[int, Field(le=10, strict=True, ge=1)]], Field(description="Maximum number of meanings per term")] = Form(3, description="Maximum number of meanings per term", ge=1, le=10),
    images: Annotated[Optional[Annotated[List[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(min_length=1, max_length=10)]], Field(description="Array of image files (1 to 10 files supported)")] = Form(None, description="Array of image files (1 to 10 files supported)"),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> GenerateResponse:
    """Generate vocabulary flashcards with audio from a text prompt and uploaded images"""
    if not BaseContentGenerationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentGenerationApi.subclasses[0]().generate_media(target_lang, prompt, with_tts, max_terms, max_meanings_per_term, images)


@router.post(
    "/generateText",
    responses={
        200: {"model": GenerateResponse, "description": "Successfully generated flashcard content"},
        400: {"model": ErrorResponse, "description": "Bad request - invalid input parameters"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    tags=["content-generation"],
    summary="Generate flashcard content from text prompt",
    response_model_by_alias=True,
)
async def generate_text(
    generate_text_request: GenerateTextRequest = Body(None, description=""),
    token_BearerAuth: TokenModel = Security(
        get_token_BearerAuth
    ),
) -> GenerateResponse:
    """Generate vocabulary flashcards with audio from a text prompt"""
    if not BaseContentGenerationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContentGenerationApi.subclasses[0]().generate_text(generate_text_request)
