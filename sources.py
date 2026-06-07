import requests
from bs4 import BeautifulSoup
import json
from config import Config
import os
from dotenv import load_dotenv
load_dotenv()
class Sources:
    def __init__(self):
        self.EVENTBRITE_API_KEY = Config.EVENTBRITE_API_KEY
   
    def REDDIT_breakdown(self):
        with open("reddit_hackathons.json", "r") as f:
            return json.load(f)
        
    def meetup_test(self):
        # Test 1 - new GraphQL endpoint
        r1 = requests.post(
            "https://api.meetup.com/gql2",
            json={"query": "{ self { id } }"},
            headers={"Content-Type": "application/json"}
        )
        print("Test 1:", r1.status_code, r1.text[:200])

        # Test 2 - another common endpoint
        r2 = requests.post(
            "https://www.meetup.com/gql",
            json={"query": "{ self { id } }"},
            headers={"Content-Type": "application/json"}
        )
        print("Test 2:", r2.status_code, r2.text[:200])
    
    def MEETUP_breakdown(self):
        query = """
        {
        keywordSearch(filter: {query: "hackathon", source: EVENTS}) {
            edges {
            node {
                result {
                ... on Event {
                    title
                    dateTime
                    description
                    eventUrl
                    isOnline
                    venue {
                    name
                    city
                    state
                    country
                    }
                    group {
                    name
                    city
                    }
                    feeSettings {
                    amount
                    currency
                    }
                }
                }
            }
            }
        }
        }
        """

        response = requests.post(
            "https://api.meetup.com/gql2", 
            json={"query": query},
            headers={"Content-Type": "application/json"}
        )

        if not response.ok:
            print(f"Meetup failed: {response.status_code} - {response.text[:200]}")
            return []

        data = response.json()
        print(f"DATA: {data}")
        events = []

        for edge in data.get("data", {}).get("keywordSearch", {}).get("edges", []):
            print(f"LOOPING: {edge}")
            e = edge.get("node", {}).get("result", {})
            if not e:
                continue
            venue = e.get("venue") or {}
            fee = e.get("feeSettings") or {}

            events.append({
                "source": "meetup.com",
                "name": e.get("title", "N/A"),
                "date": e.get("dateTime", "N/A"),
                "location": f"{venue.get('city', 'Online')}, {venue.get('state', '')}".strip(", "),
                "url": e.get("eventUrl", "N/A"),
                "is_online": e.get("isOnline", False),
                "cost": f"{fee.get('amount', 'Free')} {fee.get('currency', '')}".strip(),
                "group": e.get("group", {}).get("name", "N/A"),
                "description": (e.get("description") or "")[:200],
            })

        return events

    def test_eventbrite(self):
    # Check what the endpoint needs
        r = requests.get(f"https://www.eventbriteapi.com/v3/events/?token={self.EVENTBRITE_API_KEY}")
        print(r.status_code, r.text[:300])

        # Try organization-based search instead
        r2 = requests.get(f"https://www.eventbriteapi.com/v3/users/me/events/?token={self.EVENTBRITE_API_KEY}")
        print(r2.status_code, r2.text[:300])

        # Try keyword search via different path
        r3 = requests.get(
            f"https://www.eventbriteapi.com/v3/events/",
            params={
                "token": self.EVENTBRITE_API_KEY,
                "name.keyword": "hackathon",
                "expand": "venue"
            }
        )
        print(r3.status_code, r3.text[:300])


    def EVENTBRITE_breakdown(self):
       
        if not self.EVENTBRITE_API_KEY:
            print("Could not find 'Eventbrites' API key")
            return []
        self.test_eventbrite()
        input()
        response = requests.get(
            "https://www.eventbriteapi.com/v3/events/search",
            params={
                "token": self.EVENTBRITE_API_KEY,
                "q": "hackathon",
                "categories": "102",
                "sort_by": "date",
                "expand": "venue,ticket_availability",
                "status": "live",
            }
        )

        if not response.ok:
            print(f"Eventbrite failed: {response.status_code} - {response.text[:200]}")
            return []

        data = response.json()
        events = []

        for e in data.get("events", []):
            ticket_info = e.get("ticket_availability", {})
            venue = e.get("venue", {})
            address = venue.get("address", {})

            events.append({
                "source": "eventbrite.com",
                "name": e.get("name", {}).get("text", "N/A"),
                "date": e.get("start", {}).get("local", "N/A"),
                "location": address.get("localized_address_display", "Online"),
                "url": e.get("url", "N/A"),
                "is_free": e.get("is_free", False),
                "cost": ticket_info.get("minimum_ticket_price", {}).get("display", "Free"),
                "is_online": e.get("online_event", False),
                "capacity": e.get("capacity", "N/A"),
            })

        return events

    def DEVFOILO_breakdown(self):
        response = requests.get(
        "https://devfolio.co/api/search/hackathons",
        params={
            "status": "open",
            "sort": "newest",
            "limit": 50
        },
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )

        data = response.json()
        events = []

        for h in data.get("results", []):
            events.append({
                "source":"devfolio.com/hackathons",
                "name": h.get("name", "N/A"),
                "date": f"{h.get('starts_at', 'N/A')} to {h.get('ends_at', 'N/A')}",
                "location": h.get("location", "Online"),
                "url": f"https://devfolio.co/hackathons/{h.get('slug', '')}",
                "prize_amount": h.get("prize_pool", "N/A"),
                "team_size": f"{h.get('min_team_size', 1)}-{h.get('max_team_size', 4)}",
                "is_online": h.get("is_online", False),
                "registration_fee": h.get("registration_fee", "Free"),
                "themes": h.get("themes", []),
                "applications_count": h.get("total_applications", 0),
            })
        return events

    def DEVPOST_breakdown(self,year:int=2026):
        response = requests.get(
        "https://devpost.com/api/hackathons",
        params={
            "order_by": "recently-added",
            "status": "open",
            "per_page": 50
        },
        headers={"Accept": "application/json"}
    )

        data = response.json()
        events = []

        for h in data.get("hackathons", []):
            events.append({
                "source": "devpost.com/hackathons",
                "name": h.get("title", "N/A"),
                "date": f"{h.get('submission_period_dates', 'N/A')}",
                "location": h.get("displayed_location", {}).get("location", "N/A"),
                "url": h.get("url", "N/A"),
                "prize_amount": h.get("prize_amount", "N/A"),
                "themes": [t.get("name") for t in h.get("themes", [])],
                "open_state": h.get("open_state", "N/A"),
                "registrations_count": h.get("registrations_count", 0),
            })
        return events

    def MLH_breakdown(self,year:int=2026):
        response = requests.get(f"https://mlh.io/seasons/{year}/events")
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
                "source": 'MLH.io',
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

    def build_hackthon_history_mlh(self):
        text = ""
        for i in range(6):
            year = 2020+i
            info_on_year = self.MLH_breakdown(year)
            if not info_on_year:
                text+=f"The year {year} has no available hackathons.\n"
                continue
            text+=f"{self.MLH_breakdown(year)}\n\n"
        return text

    def sources(self,typing:type=dict):
        """returns string if typing == str else return dict:\n
        {
            "reddit": ...,
            "MLH": ...,
            "devpost": ...
        }
        """
        if typing == str: return f"""
        DATA
        
        {self.DEVPOST_breakdown()}
        \n\n
        {self.build_hackthon_history_mlh()}
        \n\n
        {self.REDDIT_breakdown()}
        
        """
        else:
            return {
                "reddit": self.REDDIT_breakdown(),
                "MLH": self.MLH_breakdown(),
                "devpost": self.DEVPOST_breakdown()
            }
if __name__ == "__main__": 
    s = Sources()
    print(json.dumps(s.sources(int), indent=2))
    # req = sources()
    # print(f"STATUS:\n\t\u2022{req}\n")
   