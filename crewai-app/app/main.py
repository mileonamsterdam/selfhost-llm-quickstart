from crewai import Crew
from agents import dataset_question_agent
from openai import OpenAI
import os

client = OpenAI(
    api_key="local",
    base_url=os.getenv("OPENAI_BASE_URL")
)

MODEL = os.getenv("OPENAI_MODEL_NAME")
DATASET_ROOT = os.getenv("DATASET_ROOT")

def run():
    crew = Crew(
        agents=[dataset_question_agent(client, MODEL, DATASET_ROOT)],
        tasks=[]
    )

    result = crew.kickoff(
        inputs={
            "dataset": "solid",   # folder name under /datasets
            "topic": "SOLID principles"
        }
    )

    print(result)

if __name__ == "__main__":
    run()
