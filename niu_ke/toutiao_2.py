def show_magicians(names):
    for name in names:
        print(name)


def make_gerat(names):
    add_str = 'the Great'
    length = len(names)
    for i in range(length):
        names[i] = names[i]+' '+add_str

if __name__ == '__main__':
    names = ['ann', 'lily', 'andy']
    make_gerat(names)
    show_magicians(names)