if __name__ == "__main__":
    f = open('test.txt', 'r')
    print(f.read(len('0x3e7c800c2e48')))
    f.close()