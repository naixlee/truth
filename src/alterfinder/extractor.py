'''
Created on May 22, 2015

@author: xli1
'''
from bs4 import BeautifulSoup
from src.settings import config

import os

class PageExtractor:
    def extract_title(self, record, rule):
        links = record.findAll('a')
        if len(links) == 0:
            return None
        if rule == 'wo_style':
            return links[0].text
        return None

    def extract_snippet(self, record, rule):
        extract_rule = config.SNIPPET_RULE.split(';')
        record_tag = extract_rule[0]
        attr_condition = {}
        conditions = extract_rule[1].split(';')
        for c in conditions:
            attr_value = c.split(':')
            attr_condition[attr_value[0]] = attr_value[1]
        if not record.find(record_tag, attr_condition) is None:
            return record.find(record_tag, attr_condition).find('p').text
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
        title = []
        snippet = []
        for record in record_list:
            title.append(self.extract_title(record, rule))
            snippet.append(self.extract_snippet(record, rule))

        return title, snippet

    def extract_srr_from_directory(self, page_directory, rule):
        titles = []
        snippets = []
        if not os.path.isdir(page_directory):
            return titles, snippets
        for page in os.listdir(page_directory):
            titles.append(self.extract_srr_from_page(page, rule))
            snippets.append(self.extract_srr_from_page(page, rule))
        return titles, snippets
