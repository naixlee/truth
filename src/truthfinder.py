'''
Created on May 22, 2015

@author: xli1
'''
from crawler import simple_crawler
from crawler import query_parser

if __name__ == '__main__':
    query_parser = query_parser.QueryParser('/Users/xli1/project/eclipse_workspace/T-verifier/Data/ICDEData/doubtful_statements.txt')
    crawler = simple_crawler.SimpleCrawler('http://www.bing.com/search?q=$query&first=$start',
                            '/Users/xli1/project/eclipse_workspace/T-verifier/Data/test')
    queries = query_parser.get_topic_query()
    if queries is None or len(queries) < 1:
        exit(-1)
    for q in queries[1:]:
        query_urls = crawler.get_query_urls(q, 100)
        crawler.fetch_pages(q, query_urls, 5)