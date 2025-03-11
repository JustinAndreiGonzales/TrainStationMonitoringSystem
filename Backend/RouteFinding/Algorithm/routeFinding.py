from .cost_matrices import lrt1_fare_matrix, lrt2_fare_matrix
from .station_id import STATION_ID_TO_NAME, STATION_NAME_TO_ID

LRT1 = [
    "Roosevelt",
    "Balintawak",
    "Monumento",
    "5th Avenue",
    "R. Papa",
    "Abad Santos",
    "Blumentritt",
    "Tayuman",
    "Bambang",
    "Doroteo Jose",
    "Carriedo",
    "Central Terminal",
    "United Nations",
    "Pedro Gil",
    "Quirino",
    "Vito Cruz",
    "Gil Puyat",
    "Libertad",
    "EDSA",
    "Baclaran"
]

LRT2 = [
    "Recto",
    "Legarda",
    "Pureza",
    "V. Mapa",
    "J. Ruiz",
    "Gilmore",
    "Betty Go-Belmonte",
    "Araneta-Cubao",
    "Anonas",
    "Katipunan",
    "Santolan2",
    "Marikina",
    "Antipolo"
]

MRT3 = [
    "North Avenue",
    "Quezon Avenue",
    "Kamuning",
    "Cubao",
    "Santolan3",
    "Ortigas",
    "Shaw Blvd.",
    "Boni",
    "Guadalupe",
    "Buendia",
    "Ayala",
    "Magallanes",
    "Taft"
]

def get_line(station: str):
    if station in LRT1:
        return "LRT1"
    if station in LRT2:
        return "LRT2"
    if station in MRT3:
        return "MRT3"

def get_path(src: str, dest: str, src_line: str, dest_line: str):
    if src_line == dest_line:
        return [src, dest]
    else:
        match src_line, dest_line:
            case "LRT2", "MRT3":
                return [src, "Araneta-Cubao", "Cubao", dest]
            case "MRT3", "LRT2":
                return [src, "Cubao", "Araneta-Cubao", dest]
            case "LRT1", "LRT2":
                return [src, "Doroteo Jose", "Recto", dest]
            case "LRT2", "LRT1":
                return [src, "Recto", "Doroteo Jose", dest]
            case "LRT1", "MRT3":
                if MRT3.index(dest) <=  8:
                    return [src, "Doroteo Jose", "Recto", "Araneta-Cubao", "Cubao", dest]
                else:
                    return [src, "EDSA", "Taft", dest]
            case "MRT3", "LRT1":
                if MRT3.index(src) <= 8:
                    return [src, "Cubao", "Araneta-Cubao", "Recto", "Doroteo Jose", dest]
                else:
                    return [src, "Taft", "EDSA", dest]
            case _, _:
                return None
            
def get_station_distance(start, end, line):
    station_line = {"LRT1": LRT1, "LRT2": LRT2, "MRT3": MRT3}
    s_line = station_line[line]
    return abs(s_line.index(end) - s_line.index(start))

def get_mrt3_fare(start, end):
    distance = get_station_distance(start, end, "MRT3")
    if 1 <= distance <= 2:
        return 13
    if 3 <= distance <= 4:
        return 16
    if 5 <= distance <= 7:
        return 20
    if 8 <= distance <= 10:
        return 24
    if 11 <= distance <= 12:
        return 28
    return 0
            
def get_cost_in_line(src: str, dest: str, line: str):
    match line:
        case "LRT1":
            return lrt1_fare_matrix[src][dest]
        case "LRT2":
            return lrt2_fare_matrix[src][dest]
        case "MRT3":
            return get_mrt3_fare(src, dest)
    
def get_route_cost(src: int, dest: int):
    src_name = STATION_ID_TO_NAME[src]
    dest_name = STATION_ID_TO_NAME[dest]
    src_line = get_line(src_name)
    dest_line = get_line(dest_name)

    path = get_path(src_name, dest_name, src_line, dest_line)
    
    final_path = []
    cost = []
    for i in range(int(len(path)/2)):
        curr = i * 2
        curr_line = get_line(path[curr])
        start = path[curr]
        next = path[curr+1]
        final_path.append((STATION_NAME_TO_ID[start], STATION_NAME_TO_ID[next], get_station_distance(start, next, curr_line)))
        cost.append(get_cost_in_line(start, next, curr_line))

    return {"path": final_path, "cost": cost}