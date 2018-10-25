"""This program implements a simplified information retrieval function using Whoosh
"""

from whoosh.fields import *
from whoosh.index import create_in
import os.path, glob
    
# index documents
def clean_index(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    index = create_in(dirname, schema=get_schema())
    writer = index.writer()
    for path in glob.glob('../collection/*.txt'):
        add_doc(writer, path)
    writer.commit()
    return index

def get_schema():
    from whoosh.analysis import StemmingAnalyzer
    stem_ana = StemmingAnalyzer()
    return Schema(path=ID(unique=True, stored=True), content=TEXT(stored=True, analyzer=stem_ana))

# incremental indexing
def add_doc(writer, path):
    import codecs
    # read in unicode characters and ignore non-unicode ones
    with codecs.open(path, 'r', 'utf-8', errors='ignore') as fileobj:
        content = fileobj.read()
        writer.add_document(path=path, content=content)
    
# search an index    
def search(query, index):
    from whoosh.qparser import QueryParser
    from whoosh.highlight import highlight
    with index.searcher() as searcher:
        query = QueryParser("content", index.schema).parse(query)
        # search and record per-document matches
        results = searcher.search(query, terms=True)
        # Show more context before and after
        results.fragmenter.surround = 50
        print ("Your query has " + str(len(results)) + " hits")
        i = 0
        for hit in results:
            i += 1
            # print out the matched snippet
            print(i, '...' + re.sub("[\t\r\n ]+", " ", hit.highlights("content", top=1)) + '...')
    
if __name__ == "__main__":
    indexdir = "indexdir"
    clean_index(indexdir)
    import whoosh.index as index
    query = input("Enter your query:")
    while(query!="exit"):
        search(query, index.open_dir(indexdir))
        query = input("\nEnter your query:")
    