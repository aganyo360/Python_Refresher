invitees = ['Nyakiti', 'Elizabeth', 'Phillip', 'Dinna']
message= 'Brice invites you, '
print(message, invitees[0])
print(message, invitees[1])
print(message, invitees[2])
print(message, invitees[3])

print(f'unforutnaly {invitees.pop(-3)} will not be available')
invitees.insert(-3, 'Bigsmoke')
print(invitees)
invitees.insert(-1, 'brice')
print(invitees)