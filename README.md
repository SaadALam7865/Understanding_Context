Agentic AI Context Management Demo 🤖
Welcome to my Agentic AI SDK demo showcasing local context vs LLM context using Python and the Gemini API! 💻 This project demonstrates how to manage private user data (local context) and feed dynamic responses to the AI (LLM context) for smart, efficient agents. 🚀
🎯 What’s This About?
This demo shows how to:

Use a UserInfo dataclass for local context to store private user data (name, ID).
Create a get_user_age tool that uses local context to generate responses.
Guide the LLM with a system prompt and user input (LLM context).
Run an async agent with the Gemini API for clean, precise outputs.

Why it matters: Understanding context management is key to building intelligent AI agents that handle data securely and respond accurately. This is my first step into AI-driven development! 🌟
🛠️ Setup Instructions
Prerequisites

Python 3.8+
Gemini API key (get it from Google Cloud)
pip install python-dotenv google-generativeai (or your Agentic AI SDK dependencies)

Steps

Clone the repo:
git clone https://github.com/your-username/your-repo.git
cd your-repo


Set up environment:Create a .env file in the project root:
GEMINI_API_KEY=your-gemini-api-key-here


Install dependencies:
pip install -r requirements.txt

Note: Create a requirements.txt with:
python-dotenv
google-generativeai
# Add your Agentic AI SDK package here


Run the demo:
python context_management_demo.py

Expected Output:
Saad ke age 20 years he



💻 Code Overview
Below is the core code that powers this demo. It uses the Agentic AI SDK (with Gemini API) to manage local and LLM context.
# Import Agentic AI SDK modules
from agents import Agent, Runner, function_tool, RunContextWrapper
from agents import AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel
import asyncio
from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Load Gemini API key
load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError('❌ GEMINI_API_KEY is not found')

# Configure Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

# Set up Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",  # Verify model name
    openai_client=external_client
)

# Define run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Local context: private user data
@dataclass
class UserInfo:
    name: str
    id: int

# Tool: uses local context to generate LLM response
@function_tool
async def get_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"{wrapper.context.name} ke age 20 years he"

# Main function
async def main():
    user_info = UserInfo(name='Saad', id=101)
    agent = Agent[UserInfo](
        name='Assistant',
        instructions="Use the 'get_user_age' tool and always only say exactly what the tool returns",
        tools=[get_user_age]
    )
    res = await Runner.run(
        starting_agent=agent,
        input='what is the age of the user?',
        context=user_info,
        run_config=config
    )
    print(res.final_output)  # Output: Saad ke age 20 years he

if __name__ == '__main__':
    asyncio.run(main())

🧠 How It Works
Local Context

What: UserInfo(name='Saad', id=101) stores private data (not visible to the LLM).
How: The get_user_age tool accesses name via wrapper.context.name.
Why: Keeps sensitive data private, used only by the code.

LLM Context

What: Includes:
System prompt: "Use the 'get_user_age' tool and always only say exactly what the tool returns".
User input: "what is the age of the user?".
Tool output: "Saad ke age 20 years he".


How: The Gemini model uses this conversation history to generate the response.

🚀 Why It’s Cool

Secure Data Handling: Local context keeps user data private.
Smart AI Responses: LLM context ensures precise, tool-driven outputs.
Scalable: Easy to add more tools for complex agent behaviors.

🌟 Connect with Me

Check out my portfolio: [https://saad-portfolio-navy.vercel.app]


📝 License
MIT License - feel free to use and modify this code!
Made & Designed by ❤️ Saad