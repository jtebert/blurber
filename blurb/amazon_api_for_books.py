# -*- coding: utf-8 -*-
# Accessory functions
import amazonproduct
import utils
config = {
    'access_key': 'AKIAJAEPJ2CLFMQOKA5A',
    'secret_key': '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',
    'associate_tag': 'blurber-20',
    'locale': 'us'
}

def dehtml(str):
    b = 0
    i = 0
    for c in str:
        if c == '(' :
            b += 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == ')':
            b -= 1
            str = str[:i] + str[i+1:]
            i -= 1
        if c == '<' :
            b += 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == '>':
            b -= 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == '\\':
            b -= 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif b > 0:
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == '—':
            str = str[:i] + '-' + str[i+1:]
        i += 1

    return str

#hard coded for now. call -> getCategoriesOfBooks() for automating it.
node_ids_genre = ["25"]
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
                    tup = (book.ItemAttributes.Title, book.ItemAttributes.Author, dehtml(book.EditorialReviews.EditorialReview.Content))
                except AttributeError:
                    continue

                lst_tuple.insert(count, tup)
                count += 1
                if count == 5:
                    break
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

for rec in final_books_dict:
    list_of_tuples = final_books_dict[rec]
    tuple_st = utils.generate_all(utils.clean(list_of_tuples))
    print "-----------------"
    print dehtml(tuple_st[0])
    print dehtml(tuple_st[1])
    print dehtml(tuple_st[2])




