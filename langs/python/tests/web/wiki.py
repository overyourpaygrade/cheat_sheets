#!/usr/bin/env python
import wikipedia

# Search for a particular article
print wikipedia.search("Suits season")

# Get the summary of a page
print wikipedia.summary("List of Suits episodes")

# Assign and print sections of the results
suits = wikipedia.page("Nietzsche")

print(suits.content)
print(suits.sections)
