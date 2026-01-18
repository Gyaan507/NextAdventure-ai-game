import json
import google.generativeai as genai
from sqlalchemy.orm import Session
from core.config import settings
from models.story import Story, StoryNode
from schemas.llm_schemas import StoryLLMResponse

# Initialize Gemini
genai.configure(api_key=settings.GOOGLE_API_KEY)

class StoryGeneratorService:
    
    @classmethod
    async def generate_story(cls, db: Session, theme: str, session_id: str) -> Story:
        print(f"Service: Requesting rich, branching story for theme '{theme}'...")

        
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            generation_config={
                "temperature": 1,
                "response_mime_type": "application/json"
            }
        )

        prompt = f"""
        You are a fast game engine. Create a 'Choose Your Own Adventure' game about: "{theme}".
        
        STORY RULES:
        1. **Fast & Punchy**: Keep descriptions under 2 sentences. Action-oriented.
        2. **Structure**: Create a tree exactly 3 levels deep.
        3. **Choices**: strictly 2 choices per node (unless ending).
        4. **Endings**: At least 1 winning, 1 losing.

        OUTPUT JSON (Strictly follow this, no markdown):
        {{
            "title": "Short Title",
            "root_node": {{
                "content": "Quick situation description...",
                "is_ending": false,
                "is_winning": false,
                "options": [
                    {{
                        "text": "Choice 1",
                        "next_node": {{
                            "content": "Result...",
                            "is_ending": false,
                            "is_winning": false,
                            "options": [ ... ]
                        }}
                    }}
                ]
            }}
        }}
        """

        try:
           
            response = model.generate_content(prompt)
            raw_json = json.loads(response.text)
            
            
            validated_story = StoryLLMResponse(**raw_json)

          
            db_story = Story(
                title=validated_story.title,
                session_id=session_id
            )
            db.add(db_story)
            db.commit()
            db.refresh(db_story)

           
            cls._process_node_recursive(db, db_story.id, validated_story.root_node, is_root=True)
            
            print(f"Story '{db_story.title}' successfully generated!")
            return db_story

        except Exception as e:
            print(f" Generation Error: {e}")
            raise e

    @classmethod
    def _process_node_recursive(cls, db: Session, story_id: int, node_data, is_root: bool = False) -> StoryNode:
        """
        Recursively saves a node and its children to the database.
        """
        db_node = StoryNode(
            story_id=story_id,
            content=node_data.content,
            is_root=is_root,
            is_ending=node_data.is_ending,
            is_winning_ending=node_data.is_winning,
            options=[] 
        )
        
        db.add(db_node)
        db.commit()
        db.refresh(db_node)

        saved_options = []
        if not db_node.is_ending and node_data.options:
            for option in node_data.options:
                child_node = cls._process_node_recursive(db, story_id, option.next_node, is_root=False)
                
                saved_options.append({
                    "text": option.text,
                    "next_node_id": child_node.id
                })

        db_node.options = saved_options
        db.add(db_node)
        db.commit()

        return db_node