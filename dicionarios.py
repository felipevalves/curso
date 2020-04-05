participant = {'name': 'Ola', 'country':'Poland', 'favorite_numbers':[67,33,2]}

print(participant['name'])

participant['favorite_language'] = 'Python'

print(participant)

# para remover usar pop
participant.pop('favorite_numbers')

print(participant)