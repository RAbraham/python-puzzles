'''
Created on Nov 17, 2014

@author: rajivabraham
'''
import itertools
from collections import namedtuple
import operator
import functools
from collections import Counter

Cell = namedtuple('Cell', 'x y')    

# List[K] => List[(K,Count)]
def frequency(seqR):
    return list(Counter(seqR).items())

def filter_cells(cell_count_pairs,cells_to_filter,filterFunc):
    cells_livecount = [ n_l for n_l in cell_count_pairs if n_l[0] in cells_to_filter]
    new_cells = {n_l[0] for n_l in cells_livecount
                                    if filterFunc(n_l[1])}
    return new_cells
    
    
def next_generation(live_cells):
    neighborsSeq = flatMap(live_cells, neighbors_xy)
    neighbors = frozenset(neighborsSeq)
    neighbor_livecount = frequency(neighborsSeq)
    
# TODO: Don't like that I do filter_cells twice
    nearby_dead_cells =  frozenset(neighbors) - live_cells
    newborn_cells = filter_cells(neighbor_livecount, nearby_dead_cells, lambda c: c == 3)

    live_cells_with_neighbors = live_cells & neighbors
    stable_cells = filter_cells(neighbor_livecount,
                                live_cells_with_neighbors,
                                lambda c: c == 2 or c == 3)
    return newborn_cells | stable_cells
    
    
# Cell => Set[(X,Y)]
def neighbors_xy(cell):

#   Set of top_row + left + right + bottom_row
    triad = frozenset([cell.x-1,cell.x,cell.x+1]) #duplication
    top_row = zip(triad,itertools.repeat(cell.y-1,3)) # duplication
    bottom_row = zip(triad,itertools.repeat(cell.y+1,3))
    
    left = Cell(cell.x-1,cell.y)
    right = Cell(cell.x+1,cell.y)
    
    top_row_xy = frozenset([ Cell(x,y) for (x,y) in top_row])
    bottom_row_xy = frozenset([Cell(x,y) for (x,y) in bottom_row])
    
    return top_row_xy.union(bottom_row_xy).union(frozenset([left,right ]))
   
def live_neighbors(live_cell,live_cells):
    return [neighbor for neighbor in neighbors_xy(live_cell) if neighbor in live_cells]
    
    
def conway_live_rules(live_neighbors_size):
    pass


def println(mySeq):
    for l in mySeq:
        print(l)
        
# mapFunc: Any => Seq[Any]
def flatMap(seqR,mapFunc):
    seqOfSeqs = [mapFunc(x) for x in seqR]
    return [r for y in seqOfSeqs for r in y]
    
if __name__ == '__main__':
    pass
    
