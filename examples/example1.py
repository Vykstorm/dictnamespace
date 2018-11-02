
'''
Usage example of class DictNamespace
This example reads the JSON document called colors.json (on the same directory as this script)
and decodes it into python objects using JSON module.
Then it uses a DictNamespace instance as a proxy to access its data.
'''


from json import load
from dictnamespace import DictNamespace


if __name__ == '__main__':
    with open('colors.json') as document:
        data = load(document)

    colors = DictNamespace(data)

    # Access data using attribute indexation...
    print(colors.aquamarine, colors.azure, colors.chocolate)

    # Or normal indexation via [] operator
    print(colors['blue'], colors['beige'], colors['antiquewhite'])

    # Modify an entry via attribute indexation...
    colors.bisque[0] = 0
    colors.aliceblue = [240, 248, 255, .45]
    