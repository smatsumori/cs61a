import ants, importlib
importlib.reload(ants)
hive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
colony = ants.AntColony(None, hive, ants.ant_types(),
    ...         ants.dry_layout, dimensions)
ants.bees_win = lambda: None
# Testing damage multiplier
queen_tunnel, side_tunnel = [[colony.places['tunnel_{0}_{1}'.format(i, j)]
...         for j in range(9)] for i in range(2)]
queen = ants.QueenAnt()
back = ants.ThrowerAnt()
front = ants.ThrowerAnt()
guard = ants.BodyguardAnt()
guarded = ants.ThrowerAnt()
side = ants.ThrowerAnt()
bee = ants.Bee(10)
side_bee = ants.Bee(10)
queen_tunnel[0].add_insect(back)
queen_tunnel[1].add_insect(guard)
queen_tunnel[1].add_insect(guarded)
queen_tunnel[2].add_insect(queen)
queen_tunnel[3].add_insect(front)
side_tunnel[0].add_insect(side)
queen_tunnel[4].add_insect(bee)
side_tunnel[4].add_insect(side_bee)
queen.action(colony)
bee.armor
9
back.action(colony)
bee.armor
7
front.action(colony)
bee.armor
6
guard.action(colony)
bee.armor
5 
