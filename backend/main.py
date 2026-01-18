from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from sqlalchemy.orm import Session
from core.config import settings
from db.database import engine, get_db
from models import story as story_models
from services.story_generator import StoryGeneratorService

# Create Tables
story_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.post("/generate")
async def generate_story_api(theme: str, db: Session = Depends(get_db)):
    try:
        # Call the Service
        story = await StoryGeneratorService.generate_story(
            db=db, 
            theme=theme, 
            session_id="user_demo_1"
        )
        return {"status": "success", "story_id": story.id, "title": story.title}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/story/{story_id}/root")
def get_story_root(story_id: int, db: Session = Depends(get_db)):
    # Helper to find the start of the game
    node = db.query(story_models.StoryNode).filter(
        story_models.StoryNode.story_id == story_id,
        story_models.StoryNode.is_root == True
    ).first()
    
    if not node:
        raise HTTPException(status_code=404, detail="Story not found")
    return node

@app.get("/node/{node_id}")
def get_node(node_id: int, db: Session = Depends(get_db)):
    node = db.query(story_models.StoryNode).filter(story_models.StoryNode.id == node_id).first()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return node