import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)

    print("Scores entered:", scores)
    print("Sum:", total)
    print("Average:", average)
    minimun = min(scores)
    maximum = max(scores)
    print("Maximum:",minimun)
    print("Maximum:",maximum)