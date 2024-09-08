# hockey-teams-db
**Building a web scraper that can conduct searches and paginate through the results.**

This Python script is designed to scrape NHL team statistics from a website that contains historical data, specifically from 1990 onwards. The goal is to browse through multiple pages of data, extract team information, and handle common website components like pagination and search.

The script achieves this by following these steps:

**Pagination Handling**: The URL structure of the website includes a page_num parameter, which is used to navigate between different pages of the team statistics. The scrape_page function dynamically updates the URL based on the current page number, allowing the script to scrape data from each page.

**Web Scraping with BeautifulSoup**: For each page, the script sends an HTTP request using the requests library. If the page loads successfully, the HTML content is parsed using BeautifulSoup, and the relevant data—team names, wins, and losses—are extracted from the table rows on the page.

**Data Collection and Storage**: The extracted data is stored in a list of dictionaries, where each dictionary represents an NHL team and its corresponding statistics (team name, wins, losses). This data is then converted into a Pandas DataFrame for easier manipulation and analysis.

**Search Simulation**: Although this specific implementation does not yet handle search queries, the framework of the scraper could be extended to include URL modifications based on search filters or form parameters, simulating user interactions like searching for teams from a specific year or conference.

**CSV Output**: After scraping all pages, the data is saved to a CSV file for further analysis or record-keeping. Intermediate data is also saved periodically in case of interruptions during the scraping process.

**Error Handling and Request Throttling**: The script includes basic error handling to ensure that missing data or failed page loads do not break the loop. Additionally, a delay between requests is added to prevent overloading the website with too many requests in a short period, mimicking the behavior of a human browsing the site.

This scraper is a useful tool for automating data collection from multi-page websites, especially when dealing with pagination and potentially search features, which are common components of web interfaces.
