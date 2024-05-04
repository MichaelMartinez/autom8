import tiktoken

# Choose the appropriate encoding based on the LLM you're using
encoding = "cl100k_base"  # Example for GPT-3.5 and GPT-4 models

tokenizer = tiktoken.get_encoding(encoding)
# open a text file to encode with utf-8
with open("output_uncompressed_output.txt", "r", encoding="utf-8") as file:
    text = file.read()
tokens = tokenizer.encode(text)

print(len(tokens))  # Output: the number of tokens
