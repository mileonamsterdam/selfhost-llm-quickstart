import os
from crewai import Agent, Task

def load_corpus(path, max_chars=20000):
    chunks = []
    for root, _, files in os.walk(path):
        for f in files:
            full = os.path.join(root, f)
            try:
                with open(full, "r", encoding="utf-8") as fh:
                    chunks.append(fh.read())
            except:
                pass
    return "\n\n".join(chunks)[:max_chars]

def dataset_question_agent(client, model, dataset_root):
    def generate(inputs):
        dataset = inputs["dataset"]
        topic = inputs["topic"]

        corpus_path = os.path.join(dataset_root, dataset)
        corpus = load_corpus(corpus_path)

        prompt = f"""
You are a senior educator.

Corpus for topic '{topic}':

---
{corpus}
---

Generate:
- 10 conceptual questions
- 5 scenario questions
- 5 code-review questions

Rules:
- Use ONLY the corpus
- No external knowledge
- Questions must be deep and challenging
"""

        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
        )

        return completion.choices[0].message.content

    return Agent(
        name="Dataset Question Generator",
        role="Generates questions from local datasets using CAG.",
        goal="Transform local corpus into high-quality questions.",
        backstory="Expert educator who converts documents into exam-level questions.",
        tasks=[
            Task(
                description="Generate questions from the dataset using CAG.",
                expected_output="Structured list of questions.",
                function=generate
            )
        ]
    )
