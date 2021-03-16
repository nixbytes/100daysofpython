import textwrap

INDENTS = 4

def print_hanging_indents(poem):
    poem = poem.split('\n\n')
    for line in poem:
        print(textwrap.fill(line.strip(),initial_indent='',subsequent_indent=' ' * INDENTS, width=50))


