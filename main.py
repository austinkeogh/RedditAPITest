import json
import pandas as pd
import requests
import comment_generator
import config
import time
import post_fetcher

subreddit = 'investing'
limit = 3
timeframe = 'week'  # hour, day, week, month, year, all
listing = 'top'  # controversial, best, hot, new, random, rising, top


def write_dataframe_to_file(df):
    data = df.to_json(default_handler=str)
    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    return

if __name__ == '__main__':
    r = post_fetcher.get_reddit(subreddit, listing, limit, timeframe)
    df = post_fetcher.get_results(r)
    #output = comment_generator.aggregate_ai_results(df)
    #write_dataframe_to_file(output)

