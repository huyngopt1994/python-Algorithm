class Underscore(object):
    # map
    # produces a new list of values by mapping each value through
    # a transformation function, lambda
    def map(self, iterable, function):
        for i in range(len(iterable)):
            iterable[i] = function(iterable[i])
        return iterable
    # reduce
    # boils the elements of a list down to a single value
    def reduce(self, iterable, function, memo):
        for num in iterable:
           memo = function(memo,num)
        return memo
    # find
    # determine whether a value exists within a list of values
    def find(self, iterable, function):
        for num in iterable:
            if function(num):
                return num
        return False
    # filter
    # looks through the values in a list returning an array of all the values
    # that meet a specific condition
    def filter(self, iterable, function):
        matches = []
        for num in iterable:
            if function(num):
                matches.append(num)
        return matches
    # reject
    # looks through the values in a list returning an array of all the values
    # that do not meet a specific condition
    def reject(self, iterable, function):
        rejected = []
        for num in iterable:
            if not function(num):
                rejected.append(num)
        return rejected