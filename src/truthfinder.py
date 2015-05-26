'''
Created on May 22, 2015

@author: xli1
'''
from crawler import simple_crawler
from crawler import query_parser
from argparse import ArgumentParser
from settings import config
from alterfinder import extractor

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-d', '--home', type=str, required=True)
    parser.add_argument('-s', '--search_engine', type=str, required=False)

    args = parser.parse_args()
    input_doubt_file = args.file
    home_directory = args.home
    search_engine = None
    return home_directory, input_doubt_file, search_engine

def collect_alterunit_pages(truth_home, input_doubt_file, search_engine):
    if search_engine is None:
        search_engine = config.BING_SEARCH
    qparser = query_parser.QueryParser(truth_home+'/'+input_doubt_file)
    crawler = simple_crawler.SimpleCrawler(search_engine, truth_home + '/' + config.ALTER_PAGES_PATH)
    queries = qparser.get_topic_query()
    if queries is None or len(queries) < 1:
        exit(-1)
    for q in queries:
        query_urls = crawler.get_query_urls(q, 100)
        crawler.fetch_pages(q, query_urls, 5)
    return queries

if __name__ == '__main__':
    truth_home, input_doubt_file, search_engine = get_args()
    queries = collect_alterunit_pages(truth_home, input_doubt_file, search_engine)
    page_extractor = extractor.PageExtractor()
    titles, snippets =