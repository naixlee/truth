'''
Created on May 22, 2015

@author: xli1
'''
from bs4 import BeautifulSoup
from src.settings import config

class PageExtractor:
    def extract_title(self, record, rule):
        links = record.findAll('a')
        if len(links) == 0:
            return None
        if rule == 'wo_style':
            return links[0].text
        return None

    def extract_snippet(self, record, rule):
        return None

    def extract_srr_from_page(self, page_file, rule):
        dom_parser = BeautifulSoup(open(page_file))
        extract_rule = config.RECORD_RULE.split(';')
        record_tag = extract_rule[0]
        attr_condition = {}
        conditions = extract_rule[1].split(';')
        for c in conditions:
            attr_value = c.split(':')
            attr_condition[attr_value[0]] = attr_value[1]
        record_list = dom_parser.findAll(record_tag, attr_condition)

    def extract_srr_from_directory(self, page_directory, rule):
        return[]

if __name__ == '__main__':
    ex = PageExtractor()
    ex.extract_srr_from_page('/Users/xli1/project/eclipse_workspace/T-verifier/Data/testhome/alter_pages/Barack Obama is a /0.html', '')
