from pydantic import BaseModel, Field
from typing import List


class AnalyzeRequest(BaseModel):
    text: str = Field(min_length=1)


class SentimentResult(BaseModel):
    score: float
    label: str


class AnalyzeResponse(BaseModel):
    sentiment: SentimentResult
    keyPhrases: List[str]