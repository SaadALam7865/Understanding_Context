from agents import Agent,Runner
from connection import config

# LLM Context: instrctions dena agent ko
agent = Agent(
    name='PoliteAssiatant',
    instructions="User ka name Saad he. Hamesha Polite raho or har response me 'Saad' name ko mentioned krna"
)

async def main():
    result = await  Runner.run(
        starting_agent=agent,
        input='what is the mother name of Mola Hussain A.S',
        run_config=config
    )

    print(result.final_output)