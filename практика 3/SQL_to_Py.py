
#реализовать функцию query
'''
SELECT event.id, event.name, asset.id, asset.name
FROM events as event LEFT JOIN assets as asset ON event.asset_id = asset.id ORDER BY event.id
LIMIT 100
'''

def query(events: list, assets: list) -> list:
    final_list=[]
    for events_int in events:
        for assets_int in assets:
            if events_int[3] == assets_int[0]:
                final_list.append([events_int[0],events_int[2],assets_int[0],assets_int[1]])
            if events_int[3] == None:
                final_list.append([events_int[0],events_int[2],None,None])
                break
    return sorted(final_list)

#Пример использования
events = [
    [4, "2024-03-28", "Event 4", 1],
    [1, "2024-03-26", "Event 1", 1],
    [6, "2024-03-29", "Event 6", 3],
    [3, "2024-03-28", "Event 3", 2],
    [5, "2024-03-29", "Event 5", None],
    [2, "2024-03-27", "Event 2", None],
     #Дополнительные события...
]
assets = [
    [4, 'Asset 4'],
    [1, 'Asset 1'],
    [3, 'Asset 3'],
    [2, 'Asset 2'],
    #Дополнительные активы...
]
     
result = query(events, assets)
for row in result:
    print(row)
#Вывод
# [1, 'Event 1', 1, 'Asset 1']
# [2, 'Event 2', None, None]
# [3, 'Event 3', 2, 'Asset 2']
# [4, 'Event 4', 1, 'Asset 1']
# [5, 'Event 5', None, None]
# [6, 'Event 6', 3, 'Asset 3']
