from typing import List, Optional
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text: str = Field(description="The text on the button the user clicks")
    
    next_node: "StoryNodeLLM" = Field(description="The nested object representing the next story scene")

class StoryNodeLLM(BaseModel):
    content: str = Field(description="The main story text for this scene")
    is_ending: bool = Field(default=False, description="True if the story ends here")
    is_winning: bool = Field(default=False, description="True if this is a good ending")
    options: List[StoryOptionLLM] = Field(default=[], description="List of choices")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="The main title of the generated story")
    root_node: StoryNodeLLM = Field(description="The starting point of the story tree")


StoryOptionLLM.model_rebuild()
StoryNodeLLM.model_rebuild()