import requests
from bs4 import BeautifulSoup
import json

def MLH_breakdown():
    response = requests.get("https://mlh.io/seasons/2025/events")
    soup = BeautifulSoup(response.text, "html.parser")

    events = []

    # Each event is wrapped in an <a> tag with itemtype="Event"
    for event in soup.find_all("a", itemtype="https://schema.org/Event"):
        
        # Name lives in the <h4> tag
        name_tag = event.find("h4")
        name = name_tag.text.strip() if name_tag else "N/A"
        
        # Dates are in the visible <span> elements
        spans = event.find_all("span", class_="text-sm truncate")
        date = spans[0].text.strip() if len(spans) > 0 else "N/A"
        location = spans[1].text.strip() if len(spans) > 1 else "N/A"
        
        # Free/paid and format live in the badge spans
        badges = event.find_all("span", class_=lambda c: c and "rounded-full" in c)
        tags = [b.text.strip() for b in badges]
        
        # Start/end dates from meta tags
        start = event.find("meta", itemprop="startDate")
        end = event.find("meta", itemprop="endDate")
        url = event.find("meta", itemprop="url")
        is_free = event.find("meta", itemprop="isAccessibleForFree")

        events.append({
            "name": name,
            "date": date,
            "location": location,
            "tags": tags,
            "start_date": start["content"] if start else "N/A",
            "end_date": end["content"] if end else "N/A",
            "url": url["content"] if url else "N/A",
            "is_free": is_free["content"] if is_free else "N/A",
        })
    return events

if __name__ == "__main__": 
    
    print(json.dumps(MLH_breakdown(), indent=2))