import sys
import os
import io

def FIFO(inputfile):
    number_of_misses = 0
    
    file = open(inputfile, 'r')
    params = file.readline().strip().split() 
    data = file.read().strip().split()
    #print(params, data)
    cache = []
    for i in range(int(params[1])):
        
        if data[i] not in cache:
            number_of_misses += 1
            if len(cache) < int(params[0]):
                cache.append(data[i])
            else:
                cache.pop(0)
                cache.append(data[i])     
        #print(len(cache), cache)        
    file.close()
    
    return number_of_misses

    
def LRU(inputfile):
    number_of_misses = 0
    cache = []
    file = open(inputfile, 'r')
    params = file.readline().strip().split() 
    data = file.read().strip().split()
    #print(params, data)
    for i in range(int(params[1])):
        if data[i] not in cache:
            #print("miss", data[i])
            number_of_misses += 1
            if len(cache) < int(params[0]):
                cache.append(data[i])
            else:
                cache.pop(0)
                cache.append(data[i])     
        else:
            #print("hit", data[i], "moved to back")
            cache.remove(data[i])
            cache.append(data[i])
        #print(len(cache), cache)


   

    return number_of_misses


def OPTFF(inputfile):
    number_of_misses = 0
    cache = set()

    file = open(inputfile, 'r')
    params = file.readline().strip().split()
    data = file.readline().strip().split()
    file.close()

    # print(params)
    # print(data)

    capacity = int(params[0])
    number_of_requests = int(params[1])

    for index, request in enumerate(data):
        if request in cache:
            continue # hit
            
        number_of_misses += 1 # miss
        cache.add(request)

        if len(cache) > capacity: # evict
            furthest = -1
            evict = None
            for item in cache:
                if item == request:
                    continue
                try:
                    next_index = data.index(item, index + 1)
                except:
                    next_index = sys.maxsize # not used again
                if next_index > furthest:
                    furthest = next_index
                    evict = item
            cache.remove(evict)

    return number_of_misses


def main():
    if len(sys.argv) != 2:
        print("Usage: python cache.py <inputfile>")
        sys.exit(1)

    inputfile = sys.argv[1]

    FIFO_misses = FIFO(inputfile)
    LRU_misses = LRU(inputfile)
    OPTFF_misses = OPTFF(inputfile)

    # Your program must output:
    # FIFO  : <number_of_misses>
    # LRU   : <number_of_misses>
    # OPTFF : <number_of_misses>

    # Use at least three nontrivial input files (each containing 50 or more requests)

    print(f"FIFO  : {FIFO_misses}")
    print(f"LRU   : {LRU_misses}")
    print(f"OPTFF : {OPTFF_misses}")
    

    return 0


if __name__ == "__main__":
    main()

