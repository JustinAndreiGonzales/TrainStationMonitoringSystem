from __future__ import annotations
from train_matrices import lrt1_fare_matrix, lrt2_fare_matrix, mrt3_fare_matrix

class TrainLine:
    def __init__(self, connections: dict[str,tuple[str, str]], matrix: dict[str, dict[str, int]] ):
        self.matrix = matrix
        self.connections = connections

class Layout:
    def __init__(self, train_lines: dict[str,TrainLine]):
        self.train_lines = train_lines

    def find_line_of(self,station: str) -> str | None:
        for key, value in self.train_lines.items():
            try:
                value.matrix[station]
                return key
            except KeyError:
                continue

    def check_connections(self, line: str) -> dict[str,tuple[str, str]]:
        return self.train_lines[line].connections
        
class Route:
    def __init__(self, path: list[tuple[str,str]], cost: list[int]):
        self.path = path
        self.cost = cost

    def __add__(self, other: Route) -> Route:
        return Route (self.path+other.path, self.cost+other.cost)

    def as_dict(self):
        return {"path":self.path, "cost":self.cost}
    
    def __repr__(self) -> str:
        return str(self.as_dict())

def _find_route(given_layout: Layout, src: str, dst: str) -> Route:
    src_line = given_layout.find_line_of(src)
    dst_line = given_layout.find_line_of(dst)

    match src_line, dst_line:
        case None,_:
            return Route([],[])
        case _, None:
            return Route([],[])
        case x, y:
            if x == y:
                return Route([(src, dst)],[given_layout.train_lines[x].matrix[src][dst]])
                #return str(given_layout.train_lines[x].matrix[src][dst])
            try: 
                next_hop, transfer = given_layout.check_connections(x)[y]
                return Route([(src, next_hop)],[given_layout.train_lines[x].matrix[src][next_hop]]) + _find_route(given_layout, transfer, dst)
                #return str(given_layout.train_lines[x].matrix[src][next_hop]) + "," + find_route(given_layout, transfer, dst)
                ...
            except KeyError:
                return Route([],[])
        

#connection needs to know the 2 stations that are connected to one another, and the lines they connect to