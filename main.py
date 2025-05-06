import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import networkx as nx
import matplotlib.pyplot as plt


class WebCrawler:
    def __init__(self, url, max_depth):
        self.base_url = url
        self.max_depth = max_depth
        self.visited = set()
        self.graph = nx.DiGraph()
        self.start_url = urlparse(url).netloc

    def validate_url(self, url):
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = 'https://' + url
            parsed_url = urlparse(url)
        return parsed_url.scheme in ("http", "https") and parsed_url.netloc == self.start_url

    def crawl(self):
        queue = [(self.base_url, 0)]
        self.visited.add(self.base_url)

        while queue:
            current_url, depth = queue.pop(0)
            print(f"Crawling: {current_url} at depth {depth}")
            if depth > self.max_depth:
                continue
            try:
                response = req.get(current_url, timeout=5)
                soup = BeautifulSoup(response.text, 'html.parser')

                for link in soup.find_all('a', href=True):
                    full_url = urljoin(current_url, link['href'])
                    full_url = full_url.split('#')[0]  # Remove fragment
                    if self.validate_url(full_url) and full_url not in self.visited:
                        self.visited.add(full_url)
                        self.graph.add_edge(current_url, full_url)
                        queue.append((full_url, depth + 1))
            except req.RequestException as e:
                print(f"Failed to fetch {current_url}: {e}")
        print("Crawling completed.")

    def visualize_graph(self):
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph, k=0.5)
        nx.draw(self.graph, pos, with_labels=False, node_size=50,
                node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
        plt.title("Web Crawler Graph")
        plt.show()


if __name__ == "__main__":
    url = input("Enter the URL to crawl: ")
    max_depth = int(input("Enter the maximum depth to crawl: "))
    parsed_url = urlparse(url)
    # Ensure the URL has a scheme
    if not parsed_url.scheme:
        url = 'https://' + url
        parsed_url = urlparse(url)

    crawler = WebCrawler(url, max_depth)
    crawler.crawl()
    crawler.visualize_graph()
