# AnkiAI Backend

FastAPI backend for generating Anki flashcards with AI-powered content and audio generation.

## Features

- **Content Generation**: Generate vocabulary flashcards from text prompts
- **Media Processing**: Process images to generate relevant vocabulary
- **Text-to-Speech**: Generate audio pronunciation for flashcard terms
- **Multi-language Support**: Support for Chinese, Japanese, Korean, and European languages
- **RESTful API**: Clean OpenAPI 3.0 compliant REST endpoints
- **Docker Support**: Containerized development and deployment

## Quick Start

### Prerequisites

- Docker and Docker Compose
- [Task](https://taskfile.dev/) (task runner)

### Setup

1. **Clone and navigate to backend directory**
   ```bash
   cd backend/
   ```

2. **Set up environment**
   ```bash
   task setup
   ```

3. **Start development server**
   ```bash
   task dev
   ```

4. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health
   - OpenAPI Schema: http://localhost:8000/api/v1/openapi.json

## API Endpoints

### Content Generation

#### `POST /api/v1/generateText`
Generate flashcard content from text prompt.

**Request:**
```json
{
  "prompt": "HSK2向けに『替・觉得・认为』。各語義ごとに短義＋例文を。",
  "targetLang": "zh-CN",
  "withTTS": true,
  "maxTerms": 10,
  "maxMeaningsPerTerm": 3
}
```

**Response:**
```json
{
  "items": [
    {
      "term": "替",
      "generated": "### 替\n- 読み: tì\n- 品詞: 動詞\n\n1) …の代わりにする\n   - 例文: 他替我参加了会议。\n   - 訳: 彼は私の代わりに会議に参加しました。",
      "audio": [
        {
          "meaningIndex": 1,
          "variant": "normal",
          "filename": "ti_sense1_norm.mp3",
          "ext": "mp3",
          "base64": "BASE64_MP3_NORMAL"
        }
      ]
    }
  ]
}
```

#### `POST /api/v1/generateMedia`
Generate flashcard content from text prompt and images.

**Request:** `multipart/form-data`
- `prompt` (optional): Text prompt
- `targetLang`: Target language code
- `withTTS`: Generate audio (boolean)
- `maxTerms`: Maximum terms to generate
- `maxMeaningsPerTerm`: Maximum meanings per term
- `images[]`: Image files (1-10 files)

## Supported Languages

- `zh-CN`: Chinese (Simplified)
- `zh-TW`: Chinese (Traditional)
- `ja-JP`: Japanese
- `ko-KR`: Korean
- `en-US`: English
- `es-ES`: Spanish
- `fr-FR`: French
- `de-DE`: German

## Development Commands

### Environment Management
```bash
task setup          # Initial project setup
task dev            # Start development server
task dev-detached   # Start in background
task stop           # Stop all services
task restart        # Restart services
```

### Code Quality
```bash
task format         # Format code with black and isort
task lint           # Run linting with flake8 and mypy
task test           # Run tests with pytest
task test-coverage  # Run tests with coverage report
```

### Utilities
```bash
task shell          # Access container shell
task logs           # Show all service logs
task logs-backend   # Show backend logs only
task health         # Check service health
task clean          # Clean Docker resources
```

### Production
```bash
task prod-build     # Build production image
task prod-run       # Run production container
```

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/        # API endpoint implementations
│   │       │   ├── content.py    # Content generation endpoints
│   │       │   ├── auth.py       # Authentication endpoints
│   │       │   ├── users.py      # User management
│   │       │   ├── decks.py      # Deck CRUD operations
│   │       │   ├── cards.py      # Card CRUD operations
│   │       │   └── study.py      # Study session management
│   │       └── api.py           # Main API router
│   ├── core/
│   │   └── config.py           # Application configuration
│   ├── schemas/
│   │   ├── content.py          # Content generation schemas
│   │   └── __init__.py
│   └── main.py                 # FastAPI application entry
├── openapi.yaml                # OpenAPI 3.0 specification
├── docker-compose.yml          # Docker services configuration
├── Dockerfile                  # Container definition
├── Taskfile.yml               # Task runner configuration
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

## Configuration

Copy `.env.example` to `.env` and update the values:

```bash
# Application Settings
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256

# Token Settings
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Server Settings
SERVER_NAME=AnkiAI
SERVER_HOST=http://localhost

# CORS Settings
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]
```

## Docker

The application is fully containerized for consistent development and deployment:

### Development
```bash
# Build and start services
task dev

# View logs
task logs-backend
```

### Production
```bash
# Build production image
task prod-build

# Run production container
task prod-run
```

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json
- **OpenAPI YAML**: Available in `openapi.yaml`

## Health Monitoring

The application includes health check endpoints:

- **Health Check**: `GET /health`
- **Root Info**: `GET /`

```bash
# Check service health
curl http://localhost:8000/health
```

## Error Handling

All API endpoints return structured error responses:

```json
{
  "error": "validation_error",
  "message": "The prompt field is required",
  "details": {
    "field": "prompt",
    "code": "required"
  }
}
```

## Next Steps

1. **Implement Content Generation Logic**: Add actual AI-powered content generation
2. **Add Authentication**: Implement JWT-based user authentication
3. **Database Integration**: Add database models and persistence
4. **Testing**: Add comprehensive unit and integration tests
5. **Monitoring**: Add logging, metrics, and health monitoring
6. **Deployment**: Set up production deployment pipeline

## Contributing

1. Follow the existing code style (enforced by `black` and `isort`)
2. Write tests for new features
3. Update documentation for API changes
4. Use the provided task commands for development workflow