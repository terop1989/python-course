with open('1.txt', 'r') as src_file:
    src_strings = src_file.readlines()

    print("\nsourse file:")
    for str in src_strings:
        print(str.strip())

    src_strings.reverse()
    with open('2.txt', 'w') as dest_file:
        dest_file.writelines(src_strings)

with open('2.txt', 'r') as dest_file:
    dest_strings = dest_file.readlines()
    print("\ndestination file:")
    for str in src_strings:
        print(str.strip())