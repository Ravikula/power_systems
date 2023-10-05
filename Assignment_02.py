import math
import cmath
import numpy as np

#Data

pg = 100        #MVA    Generator rated power
pm = 100        #MVA    Motor rated power
vg = 13.8       #kV     Generator rated voltage
vm = 13.8       #kV     Motor rated voltage

vp_tf12 = 13.8  #kV     Transformer 1,2 primary voltage
vs_ft12 = 132   #kV     Transformer 1,2 secondary voltage

vp_tf3 = 13.8   #kV     Transformer 3 primary voltage
vs_ft3 = 132    #kV     Transformer 3 secondary voltage


#POSITIVE SEQUENCE

pos_seq = {"xg" : 0.15j,    #0 - generator positive sequance reactance
           "xm" : 0.2j,     #1 - motor positive sequance reactance
           "xt" : 0.105j,   #2 - Transmission line positive sequance reactance
           "xtf12": 0.10j,  #3 - Transformer 1,2 positive sequance reactance
           "xtf3":0.10j}    #4 - transformer 3 positive sequance reactance

#NEGATIVE SEQUENCE

neg_seq = {"xg" : 0.170j,   #0 - generator negative sequance reactance
           "xm" : 0.21j,    #1 - motor negative sequance reactance
           "xt" : 0.105j,   #2 - Transmission line negative sequance reactance
           "xtf12": 0.10j,  #3 - Transformer 1,2 negative sequance reactance
           "xtf3":0.10j}    #4 - transformer 3 negative sequance reactance


#ZERO SEQUANCE

#NEGATIVE SEQUENCE

zero_seq = {"xg" : 0.050j,  #0 - generator negative sequance reactance
           "xm" : 0.1j,     #1 - motor negative sequance reactance
           "xt" : 0.315j,   #2 - Transmission line negative sequance reactance
           "xtf12": 0.100j, #3 - Transformer 1,2 negative sequance reactance
           "xtf3":0.10j}    #4 - transformer 3 negative sequance reactance

def parallel_impedance(a,b):
  c = 1/((1/a)+(1/b))
  return c

#PART 1

#POSITIVE SEQUENCE

left_side_reactance = pos_seq["xm"]+pos_seq["xtf3"]+pos_seq["xt"]
right_side_reactance = parallel_impedance(pos_seq["xtf12"]+pos_seq["xg"],pos_seq["xtf12"]+pos_seq["xg"])
Z_th_pos = parallel_impedance(left_side_reactance, right_side_reactance)
#print("Z_th_pos: "+str(abs(Z_th_pos)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_pos)))+" (degrees)")
print("Z_th_pos: "+str(round(abs(Z_th_pos),6)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_pos)))+" (degrees)")


#NEGATIVE SEQUENCE

left_side_reactance = neg_seq["xm"]+neg_seq["xtf3"]+neg_seq["xt"]
right_side_reactance = parallel_impedance(neg_seq["xtf12"]+neg_seq["xg"],neg_seq["xtf12"]+neg_seq["xg"])
Z_th_neg = parallel_impedance(left_side_reactance, right_side_reactance)
#print("Z_th_neg: "+str(abs(Z_th_neg)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_neg)))+" (degrees)")
print("Z_th_neg: "+str(round(abs(Z_th_neg),6)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_neg)))+" (degrees)")


#ZERO SEQUENCE

left_side_reactance = zero_seq["xm"]+zero_seq["xtf3"]+zero_seq["xt"]
right_side_reactance = parallel_impedance(zero_seq["xtf12"]+zero_seq["xg"],zero_seq["xtf12"]+zero_seq["xg"])
Z_th_zero = parallel_impedance(left_side_reactance, right_side_reactance)
#print("Z_th_zero: "+str(abs(Z_th_zero)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_zero)))+" (degrees)")
print("Z_th_zero: "+str(round(abs(Z_th_zero),6)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_zero)))+" (degrees)")

