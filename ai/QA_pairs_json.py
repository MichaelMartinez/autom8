import pandas as pd
import openai
import os
import glob
import json
import jsonlines

# OpenAI API Key
# openai.api_base='http://localhost:1234/v1'
# openai.api_key = 'sk-12345'


def generate_question_and_answer(text_chunk, client, model_name="local"):
    # Define the question prompt
    question_prompt = f"You are a Professor writing an exam. Using the provided context: '{text_chunk}', formulate a single question that captures an important fact or insight from the context, e.g. 'What is this code doing?' or 'What different machining stratigies are useful for making new geometry?' or 'How do you create a chamfer in this script?' or 'When do use UI commands in this python script?' or 'Where can you program python to make extensions?'. Restrict the question to the context information provided."

    # Generate a question unconditionally
    question_response = client.completions.create(
        model=model_name, prompt=question_prompt, max_tokens=200
    )
    question = question_response.choices[0].text.strip()

    # Generate an answer unconditionally
    answer_prompt = f"Given the context: '{text_chunk}', give a detailed, complete answer to the question: '{question}'. Use only the context to answer, do not give references. Simply answer the question without editorial comments."
    answer_response = client.completions.create(
        model=model_name, prompt=answer_prompt, max_tokens=500
    )
    answer = answer_response.choices[0].text.strip()

    return question, answer


# Point to the local server
client = openai.OpenAI(base_url="http://localhost:5000/v1", api_key="not-needed")

# Directory containing text files
directory_path = "D:/CODE/LLM_Datasets/Fusion-360_Dataset_QA/chunk_text"

# List to store Q&A pairs
qa_data = []

# Iterate over each file in the directory
for file_path in glob.glob(os.path.join(directory_path, "*.txt")):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        text_chunk = file.read()

    print(f"Generating Q&A for file: {file_path}")

    # Generate question and answer
    question, answer = generate_question_and_answer(text_chunk, client)

    # Append the generated Q&A to the list
    qa_data.append({"user": question, "assistant": answer})

    # Write the list of Q&A pairs to a JSONL file
    with open(
        "D:/CODE/LLM_Datasets/Fusion-360_Dataset_QA/Q&A_API.jsonl",
        "w",
        encoding="utf-8",
        errors="ignore",
    ) as outfile:
        for qa_pair in qa_data:
            json.dump(qa_pair, outfile)
            outfile.write("\n")

# Print out the first few rows of the DataFrame to confirm structure
# with open("D:/CODE/LLM_Datasets/FusionCam/Q&A_full.jsonl") as file:
#     for i in range(5):
#         print(json.loads(file.readline()))
