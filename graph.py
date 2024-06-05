import matplotlib.pyplot as plt

# Data
data = {
    'Model': ['crawl4ai', 'firecrawl', 'plain_html'],
    'gpt-4-turbo': [0.152670, 0.013310, 0.153020],
    'gpt-4o': [0.076335, 0.007155, 0.076510],
    'gpt-3.5-turbo-0125': [0.007633, 0.001616, 0.007651]
}

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