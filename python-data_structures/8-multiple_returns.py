#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length of the string and its first character."""
    first_char = sentence[0] if sentence else None
    return (len(sentence), first_char)
