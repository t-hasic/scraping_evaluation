import tiktoken
import os

model_costs = {
    "gpt-4-turbo": 10,
    "gpt-4o": 5,
    "gpt-3.5-turbo-0125": 0.5,
}

def count_tokens(input_string: str) -> int:
    tokenizer = tiktoken.get_encoding("cl100k_base")

    tokens = tokenizer.encode(input_string)

    return len(tokens)

def calculate_cost(input_string: str, cost_per_million_tokens: float = 5) -> float:
    num_tokens = count_tokens(input_string)

    total_cost = (num_tokens / 1_000_000) * cost_per_million_tokens

    return total_cost

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'output')

    for folder in os.listdir(output_dir):
        firecrawl_offset = 0.001 if folder == 'firecrawl' else 0
        folder_path = os.path.join(output_dir, folder)
        for file in os.listdir(folder_path):
            if file.endswith(".md"):
                with open(os.path.join(output_dir, folder, file), "r") as f:
                    input_string = f.read()
                print("-" * 100)
                print(f"{folder}: {count_tokens(input_string)} tokens \n")
                for model, cost in model_costs.items():
                    cost = calculate_cost(input_string, cost) + firecrawl_offset
                    print(f"The total cost for using {folder} and {model} is: $US {cost:.6f}")
    print("-" * 100)