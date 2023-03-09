#!/usr/bin/python3
import hidden_4


def main():
    n = dir(hidden_4)
    for i in range(len(n)):
        if (n[i][0] != '_'):
            print("{}".format(n[i]))


if __name__ == "__main__":
    main()
