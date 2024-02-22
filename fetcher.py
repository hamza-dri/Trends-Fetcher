import requests
import os
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key = openai_api_key)

def classify_trend(trends_list):
    trends_list_str = ', '.join([f"'{trend}'" for trend in trends_list])  
    prompt = f"""Classify each of the following Twitter trends into one of these sectors: Entertainment, Technology, Fashion, Sports, Politics or Other. Provide your answers as a JSON object where each trend is followed by its classified sector. Trends: [{trends_list_str}].Your response should be in this format: {{'trend1': 'Sector', 'trend2': 'Sector', ...}}"""
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024,  
    )

    
    return completion.choices[0].message.content.strip()


def trendList(country : str):
    # Get response from the URL.
    url = f"https://trends24.in/{country}"
    response = requests.get(url)

    # HTML parser.
    soup = BeautifulSoup(response.text, "html.parser")

    # Get the first matching element.
    tagElements = soup.find('div', attrs={'id': 'trend-list'})

    # Get the list of tag elements.
    trend_cards = tagElements.findAll('div', attrs={'class': 'trend-card'})

    # Initialize an empty dictionary to store trends and their tweet counts.
    trends_dict = {}

    # Iterate through all the trend cards.
    first_card = trend_cards[0] if trend_cards else None

    if first_card:
        # Get all list items in the ordered list of the first trend card
        list_items = first_card.ol.findAll('li')

        # Iterate through each list item
        for item in list_items:
            # Extract the trend name from the 'a' tag.
            trend_name = item.a.get_text().strip()
            
            # Find the 'span' tag with class 'tweet-count' for the tweet count, if available.
            tweet_count_span = item.find('span', class_='tweet-count')
            
            # If a tweet count is available, extract and convert it.
            if tweet_count_span:
                tweet_count = tweet_count_span.get_text()
            else:
                # Assign a default value if no tweet count is provided.
                tweet_count = None
            # Add the trend name and tweet count to the dictionary.
            trends_dict[trend_name] = tweet_count
            
    sector_dict = eval(classify_trend(list(trends_dict.keys())))


    return trends_dict,sector_dict