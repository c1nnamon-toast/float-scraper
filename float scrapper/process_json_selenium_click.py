import json

def parse_steam_url(base_url, listingid, assetid):
    parsed_url = base_url.replace('%listingid%', str(listingid)).replace('%assetid%', str(assetid))
    
    return parsed_url


if __name__ == "__main__":
    file = open("./float scrapper/output.json", encoding="utf-8");
    data = json.load(file);

    for listing in data["listinginfo"].values():
        listing_id = listing["listingid"];
        asset_id = listing["asset"]["id"];
        raw_inspect_link = listing["asset"]["market_actions"][0]["link"];

        print(parse_steam_url(raw_inspect_link, listing_id, asset_id))