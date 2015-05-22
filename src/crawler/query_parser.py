'''
Created on May 22, 2015

@author: Xian Li

The QueryParser accepts user input queries in file, prepare query statements for crawler as a list
'''
class QueryParser:
    def __init__(self, input_file):
        self.input_file_path = input_file

    '''
    Get the topic query from file with doubtful statements.
    The format of doubtful statement is id \t statement \t doubt unit etc,...
    '''
    def get_topic_query(self):
        doubt_stmt_file = open(self.input_file_path, 'r')
        doubt_stmts = doubt_stmt_file.readlines()
        topic_queries = []
        for stmt in doubt_stmts:
            elems = stmt.split('\t')
            doubtful_statement = elems[1]
            doubt_unit = elems[2]
            topic_query = doubtful_statement.replace(doubt_unit, '')
            topic_queries.append(topic_query)
        return topic_queries