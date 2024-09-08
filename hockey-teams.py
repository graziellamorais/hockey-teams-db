import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a single page
def scrape_page(page_num):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={page_num}'
    response = requests.get(url)
    
    # Check if the page was retrieved successfully
    if response.status_code != 200:
        print(f"Error: Couldn't load page {page_num}")
        return []
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all rows with class 'team'
    teams = soup.find_all('tr', class_='team')
    
    # List to store data for each team
    team_data = []
    
    for team in teams:
        # Extract text data
        team_name = team.find('td', class_='name').get_text(strip=True)
        wins = team.find('td', class_='wins').get_text(strip=True)
        losses = team.find('td', class_='losses').get_text(strip=True)
        
        # Save the data in a dictionary
        team_data.append({
            'Team Name': team_name,
            'Wins': wins,
            'Losses': losses
        })
    
    return team_data

# Function to scrape all pages (24)
def scrape_all_pages():
    all_data = []
    
    for page_num in range(1, 25):  # Loop through pages 1 to 24
        print(f"Scraping page {page_num}...")
        page_data = scrape_page(page_num)
        all_data.extend(page_data)  # Add page data to the full list
    
    return all_data

# Run the scraper and store the data
teams_data = scrape_all_pages()

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(teams_data)

# Print the first few rows to check the data
print(df.head())

# Optionally, save the DataFrame to a CSV file
df.to_csv('teams_data.csv', index=False)