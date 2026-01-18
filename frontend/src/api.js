import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const createStory = async (theme) => {
    // This calls your POST /generate endpoint
    const response = await axios.post(`${API_URL}/generate`, null, {
        params: { theme },
        //  signal: signal
    });
    return response.data;
};

export const getStoryRoot = async (storyId) => {
    // This gets the first node of the game
    const response = await axios.get(`${API_URL}/story/${storyId}/root`);
    return response.data;
};

export const getNode = async (nodeId) => {
    // This gets any subsequent node when the user clicks a choice
    const response = await axios.get(`${API_URL}/node/${nodeId}`);
    return response.data;
};