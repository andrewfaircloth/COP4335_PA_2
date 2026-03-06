import sys
import os
import io


def FIFO(inputfile, outputfile):
    number_of_misses = 0
    
    
    return number_of_misses

    
def LRU(inputfile, outputfile):
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

def OPTFF(inputfile, outputfile):
    number_of_misses = 0
    return number_of_misses


def main():
    if len(sys.argv) != 3:
        print("Usage: python cache.py <inputfile> <outputfile>")
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    FIFO_misses = FIFO(inputfile, outputfile)
    LRU_misses = LRU(inputfile, outputfile)
    OPTFF_misses = OPTFF(inputfile, outputfile)

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

