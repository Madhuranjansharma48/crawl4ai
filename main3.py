# main3.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
    CacheMode,
    MemoryAdaptiveDispatcher
)

# =====================
# FastAPI App
# =====================
app = FastAPI(
    title="Case Crawler API",
    description="API for crawling e-Jagriti case search data",
    version="1.0.0"
)

# =====================
# Input / Output Models
# =====================

class CaseSearchRequest(BaseModel):
    state: str
    commission: str
    search_value: str

class CaseResponse(BaseModel):
    case_number: str
    case_stage: str
    filing_date: str
    complainant: str
    complainant_advocate: str
    respondent: str
    respondent_advocate: str
    document_link: str


# =====================
# Utility: Parser (dummy for now)
# =====================
def extract_cases(markdown: str, payload: CaseSearchRequest) -> List[CaseResponse]:
    """
    Extract case details from crawled HTML/Markdown.
    This is placeholder logic — must be adapted to site HTML.
    """
    return [
        CaseResponse(
            case_number="123/2025",
            case_stage="Hearing",
            filing_date="2025-02-01",
            complainant="John Doe",
            complainant_advocate="Adv. Reddy",
            respondent="XYZ Ltd.",
            respondent_advocate="Adv. Mehta",
            document_link="https://e-jagriti.gov.in/.../case123"
        )
    ]


# =====================
# Routes
# =====================

@app.get("/")
async def root():
    return {"message": "Case Crawler API is running!"}

@app.get("/ping")
async def ping():
    return {"status": "ok", "message": "pong"}

@app.post("/case-search", response_model=List[CaseResponse])
async def case_search(payload: CaseSearchRequest):
    """
    Crawl the e-Jagriti case search site and return structured case info.
    """
    url = "https://e-jagriti.gov.in/advance-case-search"

    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        check_robots_txt=True,
        stream=False
    )

    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70.0,
        check_interval=1.0,
        max_session_permit=10
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun_many(
            urls=[url],
            config=run_config,
            dispatcher=dispatcher
        )

        if not results or not results[0].success:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to crawl {url}: {results[0].error_message if results else 'Unknown error'}"
            )

        return extract_cases(results[0].markdown, payload)
