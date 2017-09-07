import random


def random_walk(step, moveset):
    """ Returns tuple in random 'step' direction of moveset list (square grid clockwise 0 == stay still) """
    directions = [(0,0),
                 (0,-1),
                 (1,-1),
                 (1,0),
                 (1,1),
                 (0,1),
                 (-1,1),
                 (-1,0),
                 (-1,-1)]
    
    walk_direction = random.randrange(len(moveset))
    
    return (directions[moveset[walk_direction]][0] * step,
            directions[moveset[walk_direction]][1] * step)


print(int(1178.908349057 // 30) - 1)