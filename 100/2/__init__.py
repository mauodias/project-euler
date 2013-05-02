def main():
    total = 0
    current = 1
    before = 1
    limit = raw_input()
    while current < int(limit):
        tmp = current + before
        before = current
        current = tmp
        if current % 2 == 0:
            total += current
    print total
    
if __name__ == '__main__':
    main()