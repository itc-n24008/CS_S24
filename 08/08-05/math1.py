#円周率πをシュミレーションで求めることを考えます。原点を中心として半径１の円と、これを取り込む１辺が２の正方形を考えます。ｘ座標とｙ座標がともに正

import math
import random

total = 0
num_inside = 0
sim_pi = 0
while not math.isclose(sim_pi, math.pi, abs_tol=1e-5):
    x = random.random()
    y = random.random()
    L = pow(x**2 + y**2, 0.5)
    total += 1
    if L <= 1:
        num_inside += 1
    sim_pi = 4 * num_inside / total
print(sim_pi)
print(total)
