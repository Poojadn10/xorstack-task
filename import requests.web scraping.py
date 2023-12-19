from bs4 import Beautifulsoup
import requests
URL = "https://stackoverflow.com/questions"
PAGE_LIMIT = 1

def build_url(base_url=URL, tab="newest",page=1):
    return f"{base_url}?tab={tab}&page={page}" # example: stackoverflow.com/questions?tab=newest&page=1


def scrape_page(page=1):
    """
    function to scrape a single page on stackoverflow
    """
response = requests.get(build_url(page=page))
page_questions= []
soup=Beautifulsoup(response.text, "html.parser")
question_summary = soup.find_all("div", class_="question-summary")
for summary in question_summary:
    question = summary.find(class_="question-hyperlink").text
    vote_count = summary.find(class_="vote-count-post").find("strong").text
    answer_count = summary.find(class_="status").find("strong").text
    view_count = summary.find(class_="views").text.split()[0]
    page_questions.append(
    "question":question,
    "answers":answers_count,
    "views":view_count,
    "votes": vote_count
    ) 
    return page_questions

    
def scrape():
    """
    function to scrape to PAGE_LIMIT
    """
    questions = []
    for i in range(1, PAGE_LIMIT + 1):
        page_questions = scrape_page(1)
        questions.extend(page_questions)
        return questions


print(scrape())
