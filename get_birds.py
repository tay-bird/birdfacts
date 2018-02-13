from __future__ import print_function
import re

import wikipedia


def get_birds():
    birds = wikipedia.page('List_of_birds_by_common_name').links
    
    for bird in birds:
        try:
            summary = wikipedia.summary(bird)
        except:
            next
        
        summary = re.sub(bird, '@@SPECIES@@', summary)

        with open('names.txt', 'a') as f:
            f.write(bird.encode('ascii','ignore') + '\n')

        with open('summaries.txt', 'a') as f:
            f.write(summary.encode('ascii', 'ignore') + '\n')


if __name__ == '__main__':
    get_birds()
