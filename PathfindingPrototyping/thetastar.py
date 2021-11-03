# priority queue dictionary
from pqdict import pqdict
import quadtree
from mapgen import IMPASSABLE, PASSABLE

##############
## UL ## UR ##
##############
## LL ## LR ##
##############
UL = 0
UR = 1
LL = 2
LR = 3

def thetastar(adjafunc, distfunc, heurfunc, start, goal, quadtree):
    """ adjafunc: node -> List(nodes)
        distfunc: node, node -> double
        start: start node
        goal: end node. Terminate when reached.

        Return dict node -> absolute dist from start, dict node -> path predessor node
    """
    D = {start: 0}                   # final absolute distances
    P = {}                           # predecessors
    Q = pqdict({start: 0})           # fringe/frontier maps unexpanded node to estimated dist to goal

    considered = 0           # count how many nodes have been considered on multiple paths

    # keep expanding nodes from the fringe
    # until goal node is reached
    # or no more new nodes can be reached and fringe runs empty

    for n, estimation in Q.popitems():   # pop node with min estimated costs from queue
        if n == goal:                    # reached goal node
            break                        # stop expanding nodes

        for neighb in adjafunc(n):      # for all neighbours/adjacent of current node n
            considered += 1
            dist = D[n] + distfunc(n, neighb)        # calculate distance to neighbour: cost to current + cost reaching neighbour from current
            if neighb not in D or D[neighb] > dist:  # if neighbour never visited or shorter using this way
                D[neighb] = dist                     # found (shorter) distance to neighbour
                Q[neighb] = dist + heurfunc(neighb, goal)   # estimate distance from neighbour to goal
                P[neighb] = n                        # remember we reached neighbour via n

                # This bit is new to theta* vs A*. If line of sight passes,
                # the path is clear to skip the current tile and go stright from
                # parent instead, use that distance instead
                if n in P and line_of_sight_clear(P[n], neighb, quadtree):
                    skip_dist = D[P[n]] + distfunc(P[n], neighb)
                    D[neighb] = skip_dist
                    Q[neighb] = skip_dist + heurfunc(neighb, goal)
                    P[neighb] = P[n]

    # expanding done: distance map D populated

    if goal not in D:                # goal node not in distance map
        return None, D, considered   # no path to goal found

    # build path from start to goal
    # by walking backwards on the predecessor map

    path = []              # start with empty path
    n = goal               # at the goal node

    while n != start:      # while not yet at the start node
        path.insert(0, n)  #     prepend node to path
        n = P[n]           #     get predecessor of node

    path.insert(0, start)  # dont forget the start node

    return path, D, considered

def point_box_intersection(x, y, xb, yb, wb, hb):
    return (x > xb and x < xb + wb) and (y > yb and y < yb + hb)

def line_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    s1_x = x2 - x1
    s1_y = y2 - y1
    s2_x = x4 - x3
    s2_y = y4 - y3
    denom = (-s2_x * s1_y + s1_x * s2_y)
    if denom == 0:
        return False
    s = (-s1_y * (x1 - x3) + s1_x * (y1 - y3)) / denom
    t = (s2_x * (y1 - y3) - s2_y * (x1 - x3)) / denom
    return s >= 0 and s <= 1 and t >= 0 and t <= 1

def line_box_intersection(x1, y1, x2, y2, xb, yb, wb, hb):
    if point_box_intersection(x1, y1, xb, yb, wb, hb) or point_box_intersection(x2, y2, xb, yb, wb, hb):
        return True
    return line_line_intersection(x1, y1, x2, y2, xb, yb, xb + wb, yb) or line_line_intersection(x1, y1, x2, y2, xb + wb, yb, xb + wb, yb + hb) or line_line_intersection(x1, y1, x2, y2, xb, yb + hb, xb + wb, yb + hb) or line_line_intersection(x1, y1, x2, y2, xb, yb, xb, yb + hb)

# True when line segment intersects an impassable tile within the provided one
def line_quadtree_intersection(x1, y1, x2, y2, tile):
    if not line_box_intersection(x1, y1, x2, y2, tile.bb.x, tile.bb.y, tile.bb.w, tile.bb.h): # total miss
        return False
    if not tile.childs: # leaf node, if not PASSABLE there is collision
        return tile.color != PASSABLE
    return line_quadtree_intersection(x1, y1, x2, y2, tile.childs[UL]) or line_quadtree_intersection(x1, y1, x2, y2, tile.childs[UR]) or line_quadtree_intersection(x1, y1, x2, y2, tile.childs[LL]) or line_quadtree_intersection(x1, y1, x2, y2, tile.childs[LR])

def line_of_sight_clear(start, end, tile):
    return not line_quadtree_intersection(start.bb.center()[0], start.bb.center()[1], end.bb.center()[0], end.bb.center()[1], tile)
