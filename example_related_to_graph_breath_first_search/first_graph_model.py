# We will use dictionary to display the relationship and list to display multiple neighbours
from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(seller):
    """

    :param seller:  the name of seller
    :return: return if this guy is mango seller or not
    """
    print(seller)
    return seller[-1].lower() == 'm'

def search(name):
    mango_sellers = deque()
    mango_sellers += graph[name]
    print(mango_sellers)
    searched = []
    while mango_sellers:
        seller = mango_sellers.popleft()
        if not seller in searched:
            if person_is_seller(seller):
                print('yep we found %s' % seller)
                return True
            else:

                # add this seller neighbours
                mango_sellers += graph[seller]  # No they aren't , add all this person's friends to search queu
                searched.append(seller)
    return False

search('you')
