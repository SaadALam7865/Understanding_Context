from agents import Agent,Runner, function_tool,RunContextWrapper
from connection import config
import asyncio
from dataclasses import dataclass

# Define local context
@dataclass
class UserInfo:
    name: str
    id: int

# Tool that uses local context and contributes to LLM context
@function_tool
async def get_user_age(wrapper:RunContextWrapper) -> str:
    return f"{wrapper.context.name} ke age 20 years he"

async def main():
    user_info = UserInfo(name='Saad', id=101)

    agent = Agent(
        name='Assistant',
        instructions="Use the 'get_user_age' tool and always only say exactly  what the tool returns",
        tools=[get_user_age]
    )

    res = await  Runner.run(
        starting_agent=agent,
        input='what is the age of the user?',
        context=user_info,
        run_config=config
    )

    print(res.final_output)

if __name__ == '__main__':
    asyncio.run(main())







