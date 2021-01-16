
import internetarchive as ia
import requests 
import json
from datetime import datetime
import csv

IA_URL = 'https://be-api.us.archive.org/views/v1/short/'

# gets item stats and adds them to the specified dictionary
def get_item_stats(item):
    # sample item identifier: ALCFJamesKilgoreClip5217

    # data on number of views
    stats_url = IA_URL + item.identifier 
    item_stats = requests.get(stats_url)

    # update view stats json to include identifier, title, and timestamp
    this_item = item_stats.json()
    this_item[item.identifier]['identifier'] = item.identifier
    this_item[item.identifier]['title'] = item.metadata['title']
    this_item[item.identifier]['creator'] = item.metadata['creator']
    this_item[item.identifier]['timestamp'] = str(datetime.now())

    return this_item

def get_collection_items(collection_id):
    search_string = 'collection:' + collection_id
    search_results = ia.search_items(search_string)
    item_objects = []
    for item in search_results.iter_as_items():
        item_objects.append(item)
    print("Items found in collection: %d" %(len(item_objects)))
    return item_objects

def get_collection_stats(collection_id):
    url = IA_URL + collection_id
    collection_stats = requests.get(url)
    print("Collection view stats are:")
    print(json.dumps(collection_stats.json(), indent=3))
    return collection_stats

if __name__ == '__main__':
    collection_url = input("Paste the collection URL or id here:")
    collection_id = collection_url.split("/")[-1]
    collection_id = collection_id.split("?")[0]  # clean up url
    
    # print collection stats
    get_collection_stats(collection_id)

    # get all items from collection
    print("Grabbing all items from this collection...")
    items = get_collection_items(collection_id)

    # grab all item stats
    collection_stats = {}
    for item in items: 
        item_info = get_item_stats(item)
        collection_stats.update(item_info)
    
    # print collection stats to CSV
    print("Writing all data to file...")
    filename = collection_id + '-stats-' + str(datetime.now()) + '.csv'
    datafile = open(filename, 'w')
    csv_writer = csv.writer(datafile)
    count = 0
    for item in collection_stats:
        if count == 0:
            header = collection_stats[item].keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(collection_stats[item].values())
    datafile.close()

    print("Stats printed to " + filename)
    
    
