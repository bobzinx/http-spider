

# HTTP-Spyder

A Python-based web spider designed to recursively explore and collect all URLs from a given website. The spider follows only internal links within the same domain, ensuring it doesn't navigate outside the main site. It stores all discovered URLs in a file (`urls_collected.txt`).

---

## Features

- **Recursive Crawling**: Automatically follows links to all internal pages of the website.
- **Domain-Specific Navigation**: The spider only follows links within the same domain as the starting URL.
- **URL Collection**: All discovered URLs are saved to a text file (`urls_collected.txt`).
- **Throttling**: A small delay between requests to avoid overloading the server.

---

## Requirements

- Python 3.x
- External Libraries:
  - `requests`
  - `beautifulsoup4`

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. Install the dependencies:

   If you have a `requirements.txt` file, use:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the dependencies manually:

   ```bash
   pip install requests beautifulsoup4
   ```

---

## Usage

1. **Run the Script**:

   To start the spider, execute the following command, providing the initial URL of the website to crawl:

   ```bash
   python spider.py https://example.com
   ```

   - `https://example.com`: The initial URL where the spider will begin the search.

2. **No Depth Limit**:

   The spider will follow all internal links and visit every page. There is **no depth limit**—the spider will continue until all reachable pages have been visited.

3. **Output**:

   The spider will save all collected URLs in a file named `urls_collected.txt`. You can open this file to view the collected links.

---

## Example Execution

```bash
python spider.py https://example.com
```

This will start crawling the website from `https://example.com`, collecting all internal links.

---

## Project Structure

```bash
web-spider/
│
├── spider.py           # Main script for crawling
├── requirements.txt     # List of project dependencies
├── urls_collected.txt   # File where collected URLs are saved
└── README.md            # Project documentation (this file)
```

---

## Customization

### Modify the User-Agent

If you want to customize the **User-Agent** of the spider, modify the `HEADERS` variable in the script:

```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
```

### Add Proxies

To use the spider with proxies, you can configure the `proxies` variable in the script:

```python
proxies = {
    'http': 'http://user:password@proxyserver:port',
    'https': 'https://user:password@proxyserver:port',
}
```

Then, pass the `proxies` parameter in the request:

```python
response = requests.get(url, headers=HEADERS, proxies=proxies, timeout=5)
```

---

## Contribution

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b my-feature-branch`).
3. Make your changes.
4. Test your changes.
5. Submit a pull request explaining your modifications.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for more details.

---

### Acknowledgements

- **BeautifulSoup**: For simplifying HTML parsing and link extraction.
- **Requests**: For handling HTTP requests efficiently.

---

### Contact

If you have any questions or suggestions, feel free to send me a message or open an issue in the repository.

---

### Notes

Replace `https://github.com/your-username/repository-name.git` with the actual URL of your GitHub repository.

This README is tailored for GitHub and explains how to use and contribute to the project. If you need any further adjustments, let me know!