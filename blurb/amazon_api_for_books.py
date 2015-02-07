# Accessory functions
import amazonproduct
import time
config = {
    'access_key': 'AKIAJAEPJ2CLFMQOKA5A',
    'secret_key': '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',
    'associate_tag': 'blurber-20',
    'locale': 'us'
}

#hard coded for now. call -> getCategoriesOfBooks() for automating it.
node_ids_genre = ["25", "23", "4736"]
# List of tuples [(title,author,desc),(title,author,desc), . . .]
def getBooksFromAmazon():
    books_dict = {}
    print "hi"
    api = amazonproduct.API(cfg=config)
    for alphabet in node_ids_genre:
        lst_tuple = []
        #Expand the data set to thousands
        inner_children = getCategoriesOfBooks(alphabet)
        for child in inner_children:
            items = api.item_search('Books', BrowseNode=child,ResponseGroup="EditorialReview,ItemAttributes,BrowseNodes")
            tup = ()
            count = 0
            for book in items:
                #print '%s' % book.EditorialReviews.EditorialReview.Content
                #print '%s: "%s"' % (book.ItemAttributes.Author,book.ItemAttributes.Title)
                try:
                    tup = (book.ItemAttributes.Title, book.ItemAttributes.Author, book.EditorialReviews.EditorialReview.Content)
                except AttributeError:
                    continue
                lst_tuple.insert(count, tup)
                count += 1
        books_dict[alphabet] = lst_tuple
    return books_dict


def getCategoriesOfBooks(nodeid):
    print "Categories of books"
    api = amazonproduct.API(cfg=config)
    node_id = nodeid
    result = api.browse_node_lookup(node_id)
    list_of_child_nodes = []
    i = 0
    for child in result.BrowseNodes.BrowseNode.Children.BrowseNode:
        #print '%s (%s)' % (child.Name, child.BrowseNodeId)
        list_of_child_nodes.insert(i, child.BrowseNodeId)
        i += 1
    return list_of_child_nodes




#list_of_children = getCategoriesOfBooks("4736")
#print len(list_of_children)
#for child in list_of_children:
#    print child
final_books_dict = getBooksFromAmazon()
print len(final_books_dict)
print "hello"

