glossary_dict = {
    'varible': 'assigning',
    'string': 'store_sentence',
    'list': 'mutable_ambiguous',
    'tuple': 'immutable_list',
    'dict': 'keys-values'
}

print(glossary_dict.items())
print("")
for key in glossary_dict:
    print(key, "-", glossary_dict[key])

for key in glossary_dict:
    print("\n", key,":", "\n\t", glossary_dict[key])
for key in glossary_dict:
    print(key, ":", glossary_dict[key])