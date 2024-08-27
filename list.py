if __name__ == '__main__':
    N = list(map(int, input("please enter a number: ")))
    print("here is the list", N)
    
    N.insert(2,6)
    print("inserted list", N)

    N.remove(1)
    print("Remove number", N)

    N.append(7)
    print("append list", N)

    N.sort()
    print("sorted list", N)

    N.pop()
    print("pop number", N)

    N.reverse()
    print("reverse list", N)