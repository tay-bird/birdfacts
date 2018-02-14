from lib import facts, tweeter


if __name__ == '__main__':
    fact = facts.get_fact()
    
    print fact

    tweeter.post_to_twitter(fact)
