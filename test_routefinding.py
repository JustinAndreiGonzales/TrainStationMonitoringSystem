from routefinding import TrainLine, Layout, _find_route
from train_matrices import lrt1_fare_matrix
import logging

tl1 = TrainLine({"tl2":("A","E"),"tl3":("A","E")},{"A":{"A":0,"B":12,"C":13,},"B":{"A":12,"B":0,"C":12,},"C":{"A":13,"B":12,"C":0,}})
tl2 = TrainLine({"tl1":("E","A"), "tl3":("G","I")},{"D":{"D":0,"E":10,"F":21,"G":32},"E":{"D":1,"E":0,"F":10,"G":21},"F":{"D":2,"E":1,"F":0,"G":10},"G":{"D":3,"E":2,"F":1,"G":0}})
tl3 = TrainLine({"tl2":("I","G"),"tl1":("I","G")},{"H":{"H":0,"I":5},"I":{"H":5,"I":0}})

def test_layout():
    test_layout = Layout({"tl1":tl1,"tl2":tl2,"tl3":tl3})
    assert test_layout.find_line_of("A") == "tl1"
    assert test_layout.find_line_of("J") == None
    logging.info(_find_route(test_layout, "A","B") )
    logging.info(_find_route(test_layout, "A","C"))
    logging.info(_find_route(test_layout, "B","F"))
    logging.info(_find_route(test_layout, "B","H"))


def test_matrices():
    assert lrt1_fare_matrix["Baclaran"]["Libertad"] == 15