lokasi = ['Toko A', 'Toko B', 'Toko C', 'Toko D']
jarak = {
    'Toko A': {'Toko B': 8, 'Toko C': 15, 'Toko D': 6},
    'Toko B': {'Toko A': 8, 'Toko C': 7, 'Toko D': 3},
    'Toko C': {'Toko A': 15, 'Toko B': 7, 'Toko D': 12},
    'Toko D': {'Toko A': 6, 'Toko B': 3, 'Toko C': 12}
}

def iterative_deepening_search(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        found, result = dls(start, goal, depth, visited, path)
        if found:
            return result
    return None

def dls(node, goal, depth, visited, path):
    visited.add(node)
    path.append(node)
    if node == goal:
        return True, list(path)
    if depth == 0:
        path.pop()
        return False, None
    for neighbor in jarak[node]:
        if neighbor not in visited:
            found, result = dls(neighbor, goal, depth - 1, visited, path)
            if found:
                return True, result
    path.pop()
    return False, None

from itertools import permutations

def total_jarak(route):
    total = 0
    for i in range(len(route) - 1):
        total += jarak[route[i]][route[i+1]]
    return total

def cari_rute_terbaik(start):
    tujuan = [lok for lok in lokasi if lok != start]
    rute_terbaik = None
    jarak_min = float('inf')

    for urutan in permutations(tujuan):
        rute = [start] + list(urutan) + [start]
        if all(iterative_deepening_search(rute[i], rute[i+1], max_depth=3) for i in range(len(rute) - 1)):
            jrk = total_jarak(rute)
            if jrk < jarak_min:
                jarak_min = jrk
                rute_terbaik = rute
    return rute_terbaik, jarak_min

rute, jrk = cari_rute_terbaik('Toko A')
print("Rute terbaik (IDS):", ' → '.join(rute))
print("Total jarak:", jrk, "km")
