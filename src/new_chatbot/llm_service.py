import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        self.endpoint = os.getenv("LOCAL_LLM_ENDPOINT", "http://localhost:11434/api/generate")
        self.model = os.getenv("LOCAL_LLM_MODEL", "qwen2.5-coder:3b")

    def get_streaming_response(self, messages):
        # Convert OpenAI format to a simple prompt for the local model
        # In a real scenario, we'd format the chat history properly.
        prompt = ""
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            prompt += f"{role}: {content}\n"
        prompt += "assistant: "

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True
        }

        try:
            response = requests.post(self.endpoint, json=payload, stream=True)
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode('utf-8'))
                    if 'response' in chunk:
                        yield chunk['response']
                    if chunk.get('done'):
                        break
        except Exception as e:
            yield f"Error: {str(e)}"

llm_service = LLMService()