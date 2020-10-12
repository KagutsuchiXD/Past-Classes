"""
=======================================================
module: dcorr.py
Connor Osborne
A01880782
=======================================================
"""

import numpy as np

def direct_corr(fixed, dancer):
    """
    Computes direct correlation matrix C b/w fixed and dancer.
    """

    fnr, fnc = fixed.shape
    dnr, dnc = dancer.shape
    C = np.zeros(((fnr + dnr - 1), (fnc + dnc - 1)))

    for r in range((fnr + dnr - 1)):
        for c in range((fnc + dnc - 1)):
            value = 0
            for x in range(fnr):
                for y in range(fnc):
                    fval = fixed[x, y]
                    if x-(r-dnr+1) < 0 or x-(r-dnr+1) >= dnr or y-(c-dnc+1) < 0 or y-(c-dnc+1) >= dnc:
                        dval = 0
                    else:
                        dval = dancer[x-(r-dnr+1)][y-(c-dnc+1)]
                    value += fval * dval
            C[r, c] = value

    return C
