# IMPORTS
import pandas as pd
import requests



#FUNCTIONS


def get_data_from_api(url):
    data = []
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            results = json_data['results']
            data.extend(results)
            url = json_data['next']
            if url is None:
                break
        else:
            print(f"Error: {response.status_code}")
            break
    return data


def save_data_as_csv(data, filename):
    df = pd.DataFrame(data)
    df.reset_index(drop=True, inplace=True)  # Reset index
    df.to_csv(filename, index=False)


def fetch_data_from_api(base_url, endpoint, filename):
    url = f"{base_url}/{endpoint}/"
    data = get_data_from_api(url)
    save_data_as_csv(data, filename)

def concatenate_csv_files(csv_files):
    dfs = []
    for file in csv_files:
        df = pd.read_csv(file)
        dfs.append(df)
    concatenated_df = pd.concat(dfs, ignore_index=True)
    return concatenated_df


