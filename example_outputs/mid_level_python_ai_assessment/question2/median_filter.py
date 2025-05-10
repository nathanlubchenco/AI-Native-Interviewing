import sys

def median_filter(data):
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return sorted_data[n//2]
    else:
        return (sorted_data[n//2] + sorted_data[n//2 + 1]) / 2

if __name__ == "__main__":
    data = list(map(int, sys.argv[1:]))
    print(median_filter(data))
