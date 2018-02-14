import twitter

from lib.s3 import read_from_s3


def post_to_twitter(text):                                                                                                                                                                                                            
    consumer_key, consumer_secret = read_from_s3(
        bucket='taybird-birdfacts-creds',
        key='consumer'
    ).split(',')

    access_token_key, access_token_secret = read_from_s3(
        bucket='taybird-birdfacts-creds',
        key='access'
    ).split(',')

    api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )

    api.PostUpdate(text)
