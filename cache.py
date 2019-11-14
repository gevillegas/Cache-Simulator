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

        #Print arguements (only for testing)
        # print("ALL VALUES ARE VALID\n")
        # print("size of cache: " + str(size_of_cache))
        # print("cache line size: " + str(cache_line_size))
        # print("associativity: " + str(associativity))
        # print("filename: " + filename)

def output(total_references, total_hits, total_misses):
    print("Total number of memory references " + str(total_references))
    print("Cache hits: " + str(total_hits))
    print("Cache misses: " + str(total_misses))

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
    error_handling(size_of_cache, cache_line_size, associativity)

    list_of_all_adresses = openFileContents(filename)

    #takes the first elements that fit into the cache
    cache = list_of_all_adresses[0:size_of_cache]

    #takes the elements that didn't fit into the cache
    next_in_line = list_of_all_adresses[size_of_cache:]



    # output(1, 1, 1)
