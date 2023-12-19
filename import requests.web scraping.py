import requests
from bs4 import BeautifulSoup

def scrape_stack_overflow():
    # URL of the Stack Overflow questions page
    url = 'https://stackoverflow.com/questions'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information about questions
        questions = soup.find_all('div', class_='question-summary')

        # Iterate through each question and print its title
        for question in questions:
            title = question.find('h3').text.strip()
            print(f"Question: {title}\n")

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_stack_overflow()
