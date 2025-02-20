import requests
import json
import pandas as pd

bearer_token = "My token" # You'll need to get this via OAuth 2.0

headers = {"Authorization": f"Bearer {bearer_token}"}
search_url = "https://api.twitter.com/2/tweets/search/recent"

# Query to find tweets related to buying and selling
query_params = {
    'query': '"buy" OR "buyam" OR "sellam" OR "BuyamHQ" -is:retweet -is:reply',
    'max_results': 10,  # Between 10 and 100
    'tweet.fields': 'created_at,text',
    'expansions': 'author_id',
    'user.fields': 'name,location'
}

try:
    response = requests.get(search_url, headers=headers, params=query_params)
    response.raise_for_status()

    json_response = response.json()

    if 'data' in json_response:
        tweets = json_response['data']

        # Extract user details (author name & location)
        users = {user['id']: (user.get('name', 'Unknown'), user.get('location', 'Unknown')) 
                 for user in json_response.get('includes', {}).get('users', [])}

        tweet_data = []
        for tweet in tweets:
            author_name, author_location = users.get(tweet['author_id'], ('Unknown', 'Unknown'))

            tweet_data.append({
                'created_at': tweet['created_at'],
                'text': tweet['text'],
                'author_name': author_name,
                'location': author_location  # Store location but don't filter it
            })

        # Save to CSV if there are results
        if tweet_data:
            df = pd.DataFrame(tweet_data)
            df.to_csv("buy_sell_tweets.csv", index=False, encoding='utf-8')
            print("Tweets saved to buy_sell_tweets.csv")
        else:
            print("No tweets found.")

    else:
        print("No tweets found.")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(response.text)  # Print API response for debugging
except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")