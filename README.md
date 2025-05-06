# Web Crawler with Graph Visualization 🕸️📈

This project is a Python-based web crawler that explores internal links on a website up to a specified depth using **Breadth-First Search (BFS)**. It then visualizes the structure of the crawled site using a **directed graph** with `networkx` and `matplotlib`.

## 🔍 Features

- Crawls web pages starting from a given URL
- Traverses internal links only (same domain)
- Limits crawl by user-defined depth
- Builds a directed graph of page-to-page links
- Visualizes the link structure using `matplotlib`

## 📦 Dependencies

Make sure the following Python libraries are installed:

```bash
pip install requests beautifulsoup4 networkx matplotlib

🚀 Usage

Run the script:
python main.py
or
python3 main.py (for mac)

Then enter:

The starting URL (e.g. https://quotes.toscrape.com)
The maximum depth to crawl (e.g. 2)
Example:

Enter the URL to crawl: https://quotes.toscrape.com
Enter the maximum depth to crawl: 2
The crawler will display each page it visits, and finally show a graph where:

Nodes represent pages
Edges represent links from one page to another
📊 Output Example

The graph window will appear with the title: Web Crawler Graph.

You can customize node labels and styles in the visualize_graph() function.
