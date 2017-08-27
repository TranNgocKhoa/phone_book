# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    queries = []
    for i in range (n):
        str_ = input()
        queries.append(Query(str_.split(' ')))
    return queries

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    mycontacts = {}

    for cur_query in queries:
        if cur_query.type == 'add':
                mycontacts[cur_query.number] = cur_query.name

        elif cur_query.type == 'del':
            if cur_query.number in mycontacts:
                mycontacts.pop(cur_query.number)
        else:
            response = 'not found'
            if cur_query.number in mycontacts:
                response = mycontacts.get(cur_query.number)
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

