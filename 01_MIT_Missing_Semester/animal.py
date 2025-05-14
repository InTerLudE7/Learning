import sys

def cat():
    print('Meow!')

def default():
    if sys.argv[1] == 'cat':
        cat()
    else:
        print('Hello')

def main():
    default()

if __name__ == '__main__':
   main()
