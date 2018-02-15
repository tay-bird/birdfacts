import logging

from twitter import OAuth
from twitter import Twitter

from lib.s3 import read_from_s3


def post_to_twitter(text):
    logging.info('Post to twitter: {}'.format(text))

    try:
        consumer_key, consumer_secret = read_from_s3(
            bucket='taybird-birdfacts-creds',
            key='consumer'
        ).replace('\n', '').split(',')

        access_token_key, access_token_secret = read_from_s3(
            bucket='taybird-birdfacts-creds',
            key='access'
        ).replace('\n', '').split(',')

        logging.info('Loaded credentials from S3.')

    except Exception:
        logging.exception('Failed to load twitter credentials')
        raise

    try:
        api = Twitter(
            auth=OAuth(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                token=access_token_key,
                token_secret=access_token_secret
            )
        )
        
        api.statuses.update(status=text)

        logging.info('Posted to twitter: {}'.format(text))

    except:
        logging.exception('Failed to post to twitter: {}'.format(text))
        raise
       
