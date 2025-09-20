#pydantic

from pydantic import BaseModel
from typing import List,Optional

class StudyPlan(BaseModel):
    task: str
    chapters: List[int]
    reminder: str
    extra: Optional[str] = None


class FashionTip(BaseModel):
    occasion: str
    colors: List[str]
    outfits: str
    

class MoodBooster(BaseModel):
    mood: str
    suggestions: List[str]    

