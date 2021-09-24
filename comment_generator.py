import pandas as pd
import time
import json
import requests
import config


def get_openai_text(r):
    data = requests.post("https://api.deepai.org/api/text-generator",
        data={'text': r,
        },headers={'api-key': config.api_key}
    )
    results = json.loads(data.text)
    return(results['output'])

def aggregate_ai_results(titles):
    df2 = pd.DataFrame()
    for i in titles.title:
        j = titles.title[i]
        time.sleep(3)
        data = {'Title': [titles.title[i]], 'Content': [get_openai_text(j)]}
        result = pd.DataFrame(data)
        df2 = df2.append(result)
        print(df2)
    print(df2.index)
    return df2