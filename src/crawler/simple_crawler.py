import codecs
import os
import requests
import time

'''
The SimpleCrawler class is able to crawl a given query file line by line using get method.
It crawls search engine gently with a configurable time interval.
It is designed to fetch the top N results from search engine.
'''

class SimpleCrawler:
    query_place_holder = '$query'
    start_place_holder = '$start'

    def __init__(self, base_url_pattern, output_directory):
        self.base_url_pattern = base_url_pattern
        self.output_directory = output_directory

    def get_query_urls(self, query, num_records):
        if len(query) == 0:
            return
        # generate bing query
        query_words = query.strip().split(' ')
        concat_query_words = ''
        for word in query_words:
            concat_query_words = concat_query_words + word + '+'
        base_fetch_url = self.base_url_pattern.replace(self.query_place_holder, concat_query_words[:-1])
        query_urls = []
        for first_record_number in range(1, num_records, 10):
            fetch_url = base_fetch_url.replace(self.start_place_holder, str(first_record_number))
            query_urls.append(fetch_url)
        return query_urls

    def fetch_pages(self, query, query_urls, time_interval_sec):
        if query_urls is None or len(query_urls) < 1:
            return
        seq = 0
        if not os.path.exists(self.output_directory):
                os.mkdir(self.output_directory)
        err = codecs.open(self.output_directory + '/' + 'error', 'a', 'utf-8')
        for url in query_urls:
            print 'crawling ', url, 'starts...'
            r = requests.get(url)
            if not os.path.exists(self.output_directory + '/' + query + '/'):
                os.mkdir(self.output_directory + '/' + query + '/')
            f = codecs.open(self.output_directory + '/' + query + '/' + str(seq) + '.html', 'w', 'utf-8')
            seq = seq + 1
            f.write(r.text) if r.ok else err.write(query + '\n')
            f.close()
            print 'crawling ', url, 'finish...'
            time.sleep(time_interval_sec)
        err.close()