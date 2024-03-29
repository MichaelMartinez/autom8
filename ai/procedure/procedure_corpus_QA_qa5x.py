# Import os library
import os
import json
import random

# Import requests library
import requests


preprompt = """
<|im_start|>system
You are an assistant that is great at interpreting text and creating questions based on the context<|im_end|>
<|im_start|>user
Below is an excerpt from a book. Based on this excerpt, please write 5 detailed in-depth Questions and answers about the text. Make sure that answers follow the same style as the excerpt.
Every question should start with "fill_in_yourself:" and every answer should start with "fill_in_yourself:" Questions have to be very complex, detailed and in-depth.

CONTEXT START
"""

afterprompt = """
CONTEXT STOP

Above is an excerpt from a book. Based on this excerpt, please write 5 detailed in-depth Questions and answers about the text. Make sure that answers follow the same style as the excerpt.

ASSISTANT:
Sure, below are 5 detailed and complex questions and answers that can be inferred based on the content of the CONTEXT, the person asking the question is "fill_in_yourself:" and the person who responds is called "fill_in_yourself:".
I made sure that the questions are created are in context to the CONTEXT.
I also made sure to create multiple questions, I won't stop at one!
I made sure that the style of the response matches the style of the excerpt.

(Question 1 of 5)
fill_in_yourself:
"""


def call_api(prompt, config):
    url = "http://127.0.0.1:5001/api/v1/generate"

    with open(config, "r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)

    data = {
        "prompt": f"{prompt}",
        **config_data,
    }
    response = requests.post(url, json=data)

    try:
        response_json = response.json()
        response_text = response_json.get("results", [{}])[0].get("text", "")
        return response_text
    except json.JSONDecodeError:
        print("API response could not be decoded as JSON.")
        return ""


while True:
    # Construct the file name using string formatting
    file_name = "fill_in_yourself/book_cleaned.txt"
    # Call the action function with the file name
    # Check if the file exists
    if os.path.exists(file_name):
        # Open the file in read mode
        with open(file_name, encoding="utf8", errors="ignore") as f:
            # Read the file content
            text = f.read()
            # Get the length of the text
            length = len(text)
            # Define an empty list to store the chunks
            chunks = []
            # Loop through the text with a step of 1000
            for i in range(0, length, 12000):
                # Get a slice of 1000 characters from the text
                chunk = text[i : i + 12000]
                # Append the chunk to the list
                chunks.append(chunk)
            # Store the list in a variable
            output = chunks
            chunkcount = str(len(output))
            # Define the url of the koboldcpp api
            url = "http://127.0.0.1:5001/api/v1/generate"
            # Define an empty list to store the responses from the koboldcpp api
            responses = []
            # Loop through the output list
            file_size_limit = 50 * 1024 * 1024  # 50 megabytes
            corpus_file_name = "fill_in_yourself/book_corpus1.txt"
            corpus_file = open(corpus_file_name, "a", encoding="utf-8")
            k = 0
            for chunk in output:
                k = k + 1
                ki = str(k)
                progress = (
                    "\nProcessing chunk " + ki + " out of " + chunkcount + " chunks\n"
                )
                print(progress)
                data1 = preprompt + chunk + afterprompt
                data = data1.encode("utf-8")
                header = {"Content-Type": "text/plain; charset=utf-8"}
                # Send a post request with the chunk as data
                response = response = call_api(data, "config.json")
                # Check if the response is successful
                if response:
                    # Store the response in a variable
                    result = "fill_in_yourself:" + response
                    result = "<s>" + result + "</s>"
                    # Append the result to the responses list
                    responses.append(result)
                    # Print the result with a newline
                    print(result + "\n")
                    corpus_file.write(result + "\n\n\n")
                    corpus_file.flush()  # Ensure data is written immediately
                    # Check if the file size exceeds the limit
                    if os.path.getsize(corpus_file_name) > file_size_limit:
                        break
            else:
                # Print an error message
                print("Something went wrong. Please check the url and the chunk.")
    else:
        # Print an error message
        print("The file does not exist. Please check the file name and location.")
