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
