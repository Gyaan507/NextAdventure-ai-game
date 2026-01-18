import { useState } from 'react';
import { createStory, getStoryRoot, getNode } from './api';
import './App.css';

function App() {
  const [theme, setTheme] = useState("");
  const [loading, setLoading] = useState(false);
  const [currentNode, setCurrentNode] = useState(null);
  const [storyTitle, setStoryTitle] = useState("");

  // 1. Start the Game
  const handleStart = async () => {
    if (!theme) return;
    setLoading(true);
    try {
      // Create the story
      const storyRes = await createStory(theme);
      setStoryTitle(storyRes.title);
      
      // Get the first part of the story
      const rootNode = await getStoryRoot(storyRes.story_id);
      setCurrentNode(rootNode);
    } catch (error) {
      console.error("Failed to start game:", error);
      alert("Error starting game. Check the backend console!");
    }
    setLoading(false);
  };

  // 2. Handle Player Choice
  const handleChoice = async (nextNodeId) => {
    setLoading(true);
    try {
      const nextNode = await getNode(nextNodeId);
      setCurrentNode(nextNode);
    } catch (error) {
      console.error("Failed to load next node:", error);
    }
    setLoading(false);
  };

  // 3. Reset to Play Again
  const resetGame = () => {
    setCurrentNode(null);
    setTheme("");
    setStoryTitle("");
  };

  return (
    <div className="app-container">
      {/* HEADER */}
      <header>
        <h1>🤖 NextAdventure</h1>
        {storyTitle && <h2 className="subtitle">Playing: {storyTitle}</h2>}
      </header>

      {/* MAIN CONTENT */}
      <main>
        {!currentNode ? (
          // --- INPUT SCREEN ---
          <div className="start-screen">
            <p>Enter a theme, and AI will generate a full game for you.</p>
            <input 
              type="text" 
              placeholder="e.g., A detective in a cyberpunk city..." 
              value={theme}
              onChange={(e) => setTheme(e.target.value)}
              disabled={loading}
            />
            <button onClick={handleStart} disabled={loading || !theme}>
              {loading ? "Dreaming up story..." : "Start Adventure"}
            </button>
          </div>
        ) : (
          // --- GAME SCREEN ---
          <div className="game-screen">
            <div className="story-card">
              <p className="story-text">{currentNode.content}</p>
              
              <div className="choices-grid">
                {/* Render Choices */}
                {currentNode.options.map((option, idx) => (
                  <button 
                    key={idx} 
                    className="choice-btn"
                    onClick={() => handleChoice(option.next_node_id)}
                  >
                    {option.text}
                  </button>
                ))}

                {/* Render Ending / Reset */}
                {currentNode.is_ending && (
                  <div className={`ending-banner ${currentNode.is_winning_ending ? 'win' : 'lose'}`}>
                    <h3>{currentNode.is_winning_ending ? "🎉 YOU WON!" : "💀 GAME OVER"}</h3>
                    <button className="reset-btn" onClick={resetGame}>Play Again</button>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;