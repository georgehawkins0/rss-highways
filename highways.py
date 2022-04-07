import feedparser
import argparse

def current_incidents(road=None):
    if road:
        road = f"/{road}"
    else:
        road = ""
        
    NewsFeed = feedparser.parse(f"https://m.highwaysengland.co.uk/feeds/rss/UnplannedEvents{road}.xml")
    if NewsFeed.status == 200:
        if len(NewsFeed.entries) > 1:
            print(f"There are {len(NewsFeed.entries)} current incidents: \n")
            for entry in NewsFeed.entries:
                print(entry["published"])
                print(entry["description"])
                print("\n")

        elif len(NewsFeed.entries) == 1:
            print(f"There is {len(NewsFeed.entries)} current incident: \n")
            for entry in NewsFeed.entries:
                print(entry["published"])
                print(entry["description"])
                print("\n")

        else:
            print("No current incidents.")
    
    else:
        print("Unknown error with RSS feed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highways england RSS feed")
    parser.add_argument('road', type=str, default=None, help="The road name")
    args = parser.parse_args()
    roads = ["A1","A1(M)","M25","M1","M2","M3","M4","M5","M6","M40","M42","M60","M62","M621"]

    if args.road.upper() in roads:
        current_incidents(args.road)
    else:
        print("Invalid road.")