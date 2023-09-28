"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item = str(item)
        if item not in frequencies.keys():
            frequencies.update({item : 1})
        else:
            frequencies.update({item : frequencies.get(item) + 1})
    return frequencies