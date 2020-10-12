import numpy as np


def dc3prob(p, q, n):  # Divide and Conquer with 3 Subproblems
    pq = np.zeros((2*n))
    nextsize = (n // 2)
    qlh = np.zeros(nextsize)
    plh = np.zeros(nextsize)
    if n == 1:
        pq[0] = p[0] * q[0]
        return pq
    elif n == 2:
        PQll = p[0] * q[0]
        PQhh = p[1] * q[1]
        Lo = ((p[0] + p[1]) * (q[0] + q[1])) - PQll -PQhh
        return [PQll, Lo, PQhh]
    else:
        pl = p[0:nextsize]
        ph = p[nextsize:]
        ql = q[0:nextsize]
        qh = q[nextsize:]
        for i in range(nextsize):
            qlh[i] = ql[i] + qh[i]
            plh[i] = pl[i] + ph[i]
        Sll = dc3prob(pl, ql, nextsize)
        Shh = dc3prob(ph, qh, nextsize)
        qlh_plh = dc3prob(qlh, plh, nextsize)

        for i in range(len(Sll)):
            pq[i] += Sll[i]
            pq[i + nextsize] += qlh_plh[i] - Sll[i] - Shh[i]
            pq[i + n] += Shh[i]
        return pq
