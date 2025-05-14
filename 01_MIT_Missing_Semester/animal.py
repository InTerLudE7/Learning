import sys

def dog():
    print('woof!')

def wolf():
    print('wolf!')

def default():
    if sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'wolf':
        wolf()
    else:
        print('Hello')

def main():
    default()

if __name__ == '__main__':
   main()
