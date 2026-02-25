import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time

def get_price_history(player_id, player_name):
    url = f"https://www.futbin.com/24/player/{player_id}/{player_name}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # NEW: Extract the hidden price history from the HTML attribute
    div = soup.select_one(".highcharts-graph-wrapper.platform-pc-only.market-prices-only")

    if div is None:
        print(f"Could not find price graph for {player_name}")
        return None

    raw_json = div.get("data-pc-data")
    if not raw_json:
        print(f"No price data found for {player_name}")
        return None

    # Parse the JSON array
    price_array = json.loads(raw_json)

    # Convert to DataFrame (same structure as your original code)
    df = pd.DataFrame(price_array, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date
    df["player_id"] = player_id
    df["player_name"] = player_name

    # Reorder columns
    df = df[["player_id", "player_name", "date", "price"]]

    return df


def scrape_players(players):
    all_data = []

    for pid, name in players.items():
        print(f"Scraping {name}...")
        df = get_price_history(pid, name)
        if df is not None:
            all_data.append(df)
        time.sleep(2)  # be gentle

    if all_data:
        final_df = pd.concat(all_data)
        final_df.to_csv("data/raw/fut_prices_raw.csv", index=False)
        print("Saved to data/raw/fut_prices_raw.csv")
    else:
        print("No data scraped.")


if __name__ == "__main__":
    players = {"39": "lionel-messi",
                "150": "cristiano-ronaldo",
                "50": "neymar-jr",
                "243": "antonio-rudiger",
                "320": "alphonso-davies",
                "43": "ruben-dias",
                "300": "joshua-kimmich",
                "69": "bruno-fernandes",
                "228": "toni-kroos",
                "227": "federico-valverde",
                "52": "ter-stegen"}

    scrape_players(players)

