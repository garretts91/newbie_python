from operator import add


roster =    {'Larkin':'Center',
            'Raymond':'Right Wing',
            'Bertuzzi':'Left Wing',
            'Seider': 'Right Defense',
            'Edvinsson':'Left Defesnse'}
print(roster)
print(roster['Seider'])
print(roster['Raymond'])
#maps and keys
#maps are used to store data based on a key, not order
del roster['Bertuzzi']
print(roster)
roster['Perron']='Left Wing'
print(roster)
print(roster['Perron'])

new_name = input("Enter a player: ")
new_position = input("Enter a position: ")
roster[new_name]=new_position
print(roster)
new_name=input("Enter a player name to search their position: ")
print("%s plays %s" % (new_name, roster[new_name]))