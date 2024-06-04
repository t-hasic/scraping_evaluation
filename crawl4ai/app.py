"""

Crawl4AI is a library that allows for the scraping of websites using a variety of methods, including:

- LLMExtractor: simply extracts the html/markdown content from the website and uses a language model

- CosineSimilaritExtractor: embeds chunks of the website "document" and compares them to input query using cosine similarity

- TopicExtractor: uses simple frequency analysis to extract the most common words from the website

- ContentSummarizationExtractor: uses tranformers to summarize the content of the website

"""

from crawl4ai import WebCrawler
from datetime import datetime
import os

if __name__ == "__main__":
    # Create the WebCrawler instance 
    crawler = WebCrawler() 

    # Run the crawler with keyword filtering and CSS selector
    result = crawler.run(url="https://scrapeme.live/shop/")

    # NOTE: markdown does not contain any meaningful content; LLM approach must use HTML (simply sanitizes the HTML content)
    def sanitize_html(html):
        # Replace all weird and special characters with an empty string
        sanitized_html = html
        # sanitized_html = re.sub(r'[^\w\s.,;:!?=\[\]{}()<>\/\\\-"]', '', html)

        # Escape all double and single quotes
        sanitized_html = sanitized_html.replace('"', '\\"').replace("'", "\\'")

        return sanitized_html
    clean_html = sanitize_html(result.html)

    def save_html_data(html_data, timestamp, output_folder='../output/crawl4ai'):
        # Save the raw markdown data to the output folder with timestamp in filename:
        html_output_path = os.path.join(output_folder, f'htmlData_{timestamp}.md')
        
        with open(html_output_path, 'w', encoding='utf-8') as f:
            f.write(html_data)
        print(f"HTML data saved to {html_output_path}")

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Save the sanitized HTML data
    save_html_data(clean_html, timestamp)

