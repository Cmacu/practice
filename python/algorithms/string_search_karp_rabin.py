import math


class RollingHash:

    def __init__(self, length):
        self.size = 257
        self.mod = 1000000007
        self.hash = 0
        self.length = length
        self.text = ""
        self.power = 1
        for i in range(length):
            # prevent overflow
            self.power = (self.power * self.size) % self.mod

    def append(self, c):
        self.text += c
        ordC = ord(c)  # prehash to ordinal of the char
        self.hash = self.hash * self.size + ordC  # add char
        self.hash %= self.mod  # don't overflow
        print 'append:', c, ordC, self.hash, self.text

        return True

    def skip(self, c):
        self.text = self.text[1:]
        ordC = ord(c)  # prehash to ordinal of char
        self.hash -= self.power * ordC  # remove last char
        self.hash %= self.mod  # don't overflow
        if self.hash < 0:
            self.hash += self.mod  # fix negative hash
        print 'skip:', c, ordC, self.hash, self.text

        return True


def karp_rabin_search(context, search):
    length = len(search)
    if search == context[:length]:
        return 0, length

    print 'search:'
    search_hash = RollingHash(length)
    for c in search:
        search_hash.append(c)

    print 'context:'
    context_hash = RollingHash(length)
    for c in context[:length]:
        context_hash.append(c)

    print ''

    for i in range(length, len(context)):
        context_hash.append(context[i])
        context_hash.skip(context[i-length])
        if search_hash.hash == context_hash.hash:
            start = i - length + 1
            end = i + 1
            text = context[start:end]
            if search == text:
                return start, end

    return None, None


problem = "Willy !werther warhol wendy --> Waldo <--"
search = 'Waldo'
start, end = karp_rabin_search(problem, search)
if start is None:
    print 'Not found'
else:
    print start, end, problem[start:end]
