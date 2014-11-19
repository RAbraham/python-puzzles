from problems.gameoflife.GameOfLife1 import next_generation,Cell
def cells(tups):
    return frozenset({ Cell(x,y) for x,y in tups})

def test_gameOfLife():
#     //Still Lifes
#     // Block
    aBlock = cells([(10,10),(11,10),(11,11),(10,11)])
    assert next_generation(aBlock) == aBlock
#     //Beehive
    aBeehive = cells([(10,10),(11,9),(12,9),(13,10),(12,11),(11,11)])
    assert next_generation(aBeehive) == aBeehive
# Oscillators
# // Blinker
    assert next_generation(cells([(10,10),(11,10),(12,10)])) == cells([(11,9),(11,10),(11,11)])
# // Toad
    x = 10
    y = 10
    aToad = cells([(x-1,y+1),
                   (x,y),
                   (x,y+1),
                   (x+1,y),
                   (x+1,y+1),
                   (x+2,y)])
    
    nextToad = cells([(x-1,y),
                      (x-1,y+1),
                      (x,y+2),
                      (x+1,y-1),
                      (x+2,y),
                      (x+2,y+1)])
    
    assert next_generation(aToad) == nextToad
                   



# TODO: Random generate x,y ?