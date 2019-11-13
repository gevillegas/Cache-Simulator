
import sys
if __name__ =="__main__":

    size_of_cache = sys.argv[1]
    cache_line_size = sys.argv[2]
    associativity = sys.argv[3]
    filename = sys.argv[4]

    if int(size_of_cache)>64 or int(size_of_cache)%2 ==1:
        print("size of cache is invalid")
        sys.exit()
    # else:
    #     print("size of cache: " + size_of_cache)

    if int(cache_line_size) > 128 or int(cache_line_size)%2 == 1:
        print("size of cache is invalid")
        sys.exit()
    # else:
    #     print("cache line size: " + cache_line_size)

    if int(associativity) < 1:
        print("associativity value is invalid")
        sys.exit()


    print("size of cache: " + size_of_cache)
    print("cache line size: " + cache_line_size)
    print("associativity: " + associativity)
