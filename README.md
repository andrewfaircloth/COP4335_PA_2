# COP4533_PA_2

**Programming Assignment 2: Greedy Algorithms**

## Authors

Alexander Neil - 16230392

Andrew Faircloth - 87943837

## Getting Started

### Installation

Clone the repository

```
git clone https://github.com/andrewfaircloth/COP4533_PA_2
```

Navigate to the repository

```
cd ../COP4533_PA_2
```

### Cache

`src/cache.py`

The Cache takes in a file with parameters (# capacity and # of requests) and data (string of requests) and prints the number of misses using different cache replacement strategies

```
python src/cache.py <input_file> <output_file>
```

Example:

```
python src/cache.py data/example1.in data/example1.out
```



## Input

### <input_file> Format

* First line: (capacity of cache) (number of requests)
* Second line: list of requests in order

Example Input:

```
2 10
1 2 3 4 5 6 7 8 9 10
```
## Output

## <output_file> Format

* First line: "FIFO:" followed by the number of cache misses using the replacement strategy
* Second line: "LRU:" followed by the number of cache misses using the replacement strategy
* Third Line:"OPTFF:" followed by the number of cache misses using the replacement strategy

Example Output:

```
FIFO  : 10
LRU   : 10
OPTFF : 10
```

## Written Component

[Written Portion](ProgrammingAssignment2_WrittenPortion.pdf)