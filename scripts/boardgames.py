#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///

import requests
import xml.etree.ElementTree as ET
import json
import time
import logging
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def fetch_boardgame_collection(username: str) -> str:
    url = f"https://boardgamegeek.com/xmlapi2/collection?username={username}&own=1&stats=1&excludesubtype=boardgameexpansion"

    max_retries = 5
    retry_delay = 2

    for attempt in range(max_retries):
        response = requests.get(url)

        if response.status_code == 202:
            logger.info(
                f"Collection still processing, retrying in {retry_delay} seconds... (attempt {attempt + 1}/{max_retries})"
            )
            time.sleep(retry_delay)
            retry_delay *= 2
            continue

        response.raise_for_status()
        return response.text

    raise Exception(f"Failed to fetch collection after {max_retries} attempts")


def parse_collection_xml(xml_content: str) -> List[Dict[str, Any]]:
    root = ET.fromstring(xml_content)
    games = []

    for item in root.findall("item"):
        game = {
            "objectid": item.get("objectid"),
            "name": None,
            "yearpublished": None,
            "my_rating": None,
            "stats": {},
            "comment": None,
        }

        name_elem = item.find("name")
        if name_elem is not None:
            game["name"] = name_elem.text

        year_elem = item.find("yearpublished")
        if year_elem is not None:
            game["yearpublished"] = year_elem.text

        thumbnail_elem = item.find("image")
        if thumbnail_elem is not None:
            game["image"] = thumbnail_elem.text
        comment_elem = item.find("comment")
        if comment_elem is not None:
            game["comment"] = comment_elem.text

        stats_elem = item.find("stats")
        if stats_elem is not None:
            rating_elem = stats_elem.find("rating")
            if rating_elem is not None:
                game["stats"] = {
                    "minplayers": stats_elem.get("minplayers"),
                    "maxplayers": stats_elem.get("maxplayers"),
                    "playingtime": stats_elem.get("playingtime"),
                }
                if rating_elem.get("value") != "N/A":
                    game["my_rating"] = float(rating_elem.get("value"))
        games.append(game)
    games = sorted(games, key=lambda x: x["my_rating"] or 0, reverse=True)
    return games


def save_to_json(data: List[Dict[str, Any]], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    username = "sinon88"
    output_file = "../static/boardgames_collection.json"

    try:
        logger.info(f"Fetching board game collection for user: {username}")
        xml_content = fetch_boardgame_collection(username)

        logger.info("Parsing XML content...")
        games_list = parse_collection_xml(xml_content)

        logger.info(f"Found {len(games_list)} games in collection")

        logger.info(f"Saving to {output_file}...")
        save_to_json(games_list, output_file)

        logger.info(f"Successfully saved board game collection to {output_file}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data: {e}")
    except ET.ParseError as e:
        logger.error(f"Error parsing XML: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
