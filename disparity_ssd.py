import cv2 as cv
import numpy as np
import  pandas as pd
import numpy as np
import  pandas as pd
def disparity_ssd(L,R,ksize=11,max_offset=6):
    L_r, L_c  = L.shape
    R_r, R_c  = R.shape
    border = int((ksize - 1) / 2)
    D_L = np.zeros(L.shape, dtype=np.float32)
    for r in range(border, L_r-border):
        tr_min, tr_max = max(int(r - border), 0), min(int(r + border + 1),L_r)
        for c in range(border, L_c-border):
            best_offset=0
            prev_ssd = border ** 2
            tc_min = max(int(c - border), 0)
            tc_max = min(int(c + border + 1), L_c)
            tpl = L[tr_min:tr_max, tc_min:tc_max].astype(np.float32)
            rc_min = max(int(c-max_offset/2), border)
            rc_max = min(int(c+max_offset/2), L_c - border)
            for offset in range(rc_min,rc_max):
                ssd = 0
                s=tpl-R[tr_min:tr_max,offset-border:offset+border+1]
                ssd=np.sum(s**2)
                #for j in range(-border,border+1):
                 #   for i in range(-border,border+1):
                  #      a=min(  i+offset, L_c-border)
                   #     ssd_temp = float(L[r + j, c + i]-R[r + j, a])
                    #    ssd += ssd_temp * ssd_temp

                if ssd < prev_ssd:
                    prev_ssd=ssd
                    best_offset=c-offset
                    D_L[r, c] = best_offset

    return D_L