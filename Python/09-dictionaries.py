# dictionaries : they are the collection of unordered unique key:value pair / Fast because they use hashing, allow us to    
#                access the value quickly

capitals = {'USA' : 'Washington DC',
            'India' : 'New Delhi',
            'China' : 'Beijing'
            }

# ! Content Access

print(capitals['USA'])
print(capitals.get('India'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

# ! Adding

capitals.update({'Germany' : 'Berlin'})
capitals['Russia'] = 'Moscow'

# ! Deleting

capitals.pop('Russia')

capitals.clear()


