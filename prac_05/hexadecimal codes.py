import collections

def main():
    with open('hexadecimal codes.txt','r') as hexfile:
        lines = hexfile.readlines()
    hexkey = list()
    hexval = list()
    for line in lines:
        line.strip('\t')
        line.strip('\n')
        hashspot = line.find('#')
        hexkey.append(line[0:hashspot-1])
        hexval.append(line[hashspot:-1])
    hexdict = collections.OrderedDict(zip(hexkey, hexval))
    print(hexdict)

main()

