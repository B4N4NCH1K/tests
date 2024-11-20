def my_code(data_graph, top_num, visited=None):
    if visited is None:
        visited = set()
    visited.add(top_num)
    print(f' {top_num}')  

    for tops in data_graph.get(top_num, []):
        if tops not in visited:
            my_code(data_graph, tops, visited)
    

data = {
    1: [2, 3],
    2: [4]
}

my_code(data, 1)

print('UwU')

data = {
    1: [2, 3],
    2: [3, 4],
    4: [1]
}

my_code(data, 1)
