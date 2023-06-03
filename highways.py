import feedparser
import argparse

def current_incidents(road=None):
    if road == "ALL":
        road_ = "" # for parse into url
        road = "" # for naming by in lines 14,21,28
    else:
        road_ = f"/{road}" # for parse into url
        
    NewsFeed = feedparser.parse(f"https://m.highwaysengland.co.uk/feeds/rss/UnplannedEvents{road_}.xml")
    if NewsFeed.status == 200:
        if len(NewsFeed.entries) > 1:
            print(f"There are {len(NewsFeed.entries)} current incidents on {road}: \n")
            for entry in NewsFeed.entries:
                print(entry["published"])
                print(entry["description"])
                print("\n")

        elif len(NewsFeed.entries) == 1:
            print(f"There is {len(NewsFeed.entries)} current incident on {road}: \n")
            for entry in NewsFeed.entries:
                print(entry["published"])
                print(entry["description"])
                print("\n")

        else:
            if road != "": # if the road has an actual name
                print(f"No current incidents on {road}.") # the rss feed doesnt return a 404. An invalid road name will return a 200 with no entries.
            else: # if was parsed into function as ALL
                print("No current incidents.")
    
    else:
        print("Unknown error with RSS feed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highways england RSS feed.")
    parser.add_argument('road', type=str, default=None, help="The road name. Use ALL for all major trunk roads.")
    args = parser.parse_args()

    current_incidents(args.road.upper())
