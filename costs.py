import os
import tiktoken
import matplotlib.pyplot as plt

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
    # Data
    data = {
        'Model': ['crawl4ai', 'firecrawl', 'plain_html'],
        'tokens': [],
        'gpt-4-turbo': [],
        'gpt-4o': [],
        'gpt-3.5-turbo-0125': []
    }

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'output')

    for folder in os.listdir(output_dir):
        firecrawl_offset = 0.001 if folder == 'firecrawl' else 0
        folder_path = os.path.join(output_dir, folder)
        for file in os.listdir(folder_path):
            if file.endswith(".md"):
                with open(os.path.join(output_dir, folder, file), "r") as f:
                    input_string = f.read()
                tokens = count_tokens(input_string)
                print("-" * 100)
                print(f"{folder}: {tokens} tokens \n")
                data['tokens'].append(tokens)
                for model, cost in model_costs.items():
                    cost = calculate_cost(input_string, cost) + firecrawl_offset
                    data[model].append(cost)
                    print(f"The total cost for using {folder} and {model} is: $US {cost:.6f}")
    print("-" * 100)


    # Create bar chart
    fig, ax = plt.subplots()

    bar_width = 0.2
    index = range(len(data['Model']))

    bar1 = [i for i in index]
    bar2 = [i + bar_width for i in index]
    bar3 = [i + 2 * bar_width for i in index]

    plt.bar(bar1, data['gpt-4-turbo'], bar_width, label='gpt-4-turbo')
    plt.bar(bar2, data['gpt-4o'], bar_width, label='gpt-4o')
    plt.bar(bar3, data['gpt-3.5-turbo-0125'], bar_width, label='gpt-3.5-turbo-0125')

    plt.xlabel('Models')
    plt.ylabel('Cost in $US')
    plt.title('Cost Comparison of Different Models')
    plt.xticks([r + bar_width for r in index], data['Model'])
    plt.legend()

    plt.show()

    # Create bar chart
    fig, ax = plt.subplots()

    bar_width = 0.2
    index = range(len(data['Model']))

    bar1 = [i for i in index]
    bar2 = [i + bar_width for i in index]
    bar3 = [i + 2 * bar_width for i in index]

    plt.bar(bar1, data['tokens'], bar_width, label='tokens')

    plt.xlabel('Models')
    plt.ylabel('Number of Tokens')
    plt.title('Token Comparison of Different Models')
    plt.xticks([r + bar_width for r in index], data['Model'])
    plt.legend()

    plt.show()