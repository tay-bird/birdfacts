from lib import facts, tweeter


if __name__ == '__main__':
    tries = 3

    while tries > 0:
        try:
            fact = facts.get_fact()
        except:
            raise
        else:
            if len(fact) < 280:
                break
        finally:
            tries = tries - 1
    
    if fact:
        print 'Posting fact! "{}"'.format(fact)
        tweeter.post_to_twitter(fact)
    else:
        print 'bad fact :('
