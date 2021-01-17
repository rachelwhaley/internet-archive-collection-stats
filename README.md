# internet-archive-collection-stats
Python script to scrape viewership data for every item in an Internet Archive collection.

### To run 
```python main.py```

### Usage
Copy the URL or id of a collection from [Internet Archive](https://archive.org/) and enter when prompted. 

For example: https://archive.org/details/al-larvick-fund

### Sample output

A csv file with one row for each item in the collection:

| all_time	| have_data	| last_30day | last_7day | identifier | title | timestamp |
| :-------- | :-------: | :--------: | :-------: | :--------: | :---: | --------: |
| 159 | TRUE | 10 | 6 | ALCFJamesKilgoreClip5217 | ALCF James Kilgore Films Clip 5217 | 2021-01-16 14:30:00 |

See definitions of the views fields (all_time, have_data, last_30day, last_7day) here: https://archive.org/services/docs/api/views_api.html