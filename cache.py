import sys

def error_handling(size_of_cache, cache_line_size, associativity):
        if size_of_cache >64 or size_of_cache%2 ==1:
            print("size of cache is invalid")
            sys.exit()

        if cache_line_size > 128 or cache_line_size%2 == 1:
            print("size of cache is invalid")
            sys.exit()

        if associativity < 1:
            print("associativity value is invalid")
            sys.exit()


def output(total_references, total_hits, total_misses):
    print("Total number of memory references " + str(total_references))
    print("Cache hits: " + str(total_hits))
    print("Cache misses: " + str(total_misses))

#returns a list of ints with all the addresses in the given file
def openFileContents(filename):
    list_of_adresses = []
    file = open(filename, 'r')

    for i in file:
        list_of_adresses.append(int(i))
    file.close()
    return list_of_adresses



if __name__ =="__main__":

    size_of_cache = int(sys.argv[1])
    cache_line_size = int(sys.argv[2])
    associativity = int(sys.argv[3])
    filename = sys.argv[4]

    cache_hits = 0
    cache_misses = 0

    error_handling(size_of_cache, cache_line_size, associativity)

    list_of_all_adresses = openFileContents(filename)


    #takes the elements that fit into the cache
    cache = []
    #takes the elements that didn't fit into the cache
    next_in_line = []

    for i in list_of_all_adresses:
        if i in cache:
            cache_hits +=1
        else:
            if(len(cache) < size_of_cache):
                cache_misses +=1
                cache.append(i)
            else:
                next_in_line.append(i)



    for i in next_in_line:
        if i in cache:
            cache_hits += 1
            print(str(i) + " is a hit")
            #these two lines remove the found element and add to the top of the list (MRU)
            cache.remove(i)
            cache.insert(0,i)
        else:
            cache_misses += 1
            print(str(i) + " is a miss")
            #these two lines remove the last element (LRU) and the new miss element to the top of the list (MRU)
            cache.pop()
            cache.insert(0, i)


    print("----------------------------------")
    print("total hits: " + str(cache_hits))
    print("total misses: " + str(cache_misses))

    print("----------------------------------")
    print(cache)
    # output(1, 1, 1)
