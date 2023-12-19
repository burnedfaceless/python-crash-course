favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# In Python a set doesn't have key value pairs and each item must be unique

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
