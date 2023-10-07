import cmath
import math
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

xgg = 0.04j      #pu     Generator 1,2 Grounding impedance
xgm = 0.05j      #pu     Motor grounding impedance


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

zero_seq = {"xg" : 0.050j,  #0 - generator negative sequance reactance
           "xm" : 0.1j,     #1 - motor negative sequance reactance
           "xt" : 0.315j,   #2 - Transmission line negative sequance reactance
           "xtf12": 0.100j, #3 - Transformer 1,2 negative sequance reactance
           "xtf3":0.10j}    #4 - transformer 3 negative sequance reactance

a = cmath.rect(1, math.radians(120))
a2 = cmath.rect(1, math.radians(240))

#TRANSFORMATION MATRIX
T = np.array([[1, 1, 1],
              [1, a2, a],
              [1, a, a2]])

#INVERSE TRANSFORMATION MATRIX
T_1 = np.array([[1, 1, 1],
                [1, a, a2],
                [1, a2, a]])

d = 6     #No of decimal places

#Function to calculate parallel impedance

def z_p(a,b):
  c = 1/((1/a)+(1/b))
  return c

#PART 1

#POSITIVE SEQUENCE

xp1 = pos_seq["xm"]+pos_seq["xtf3"]+pos_seq["xt"]
xp2 = z_p(pos_seq["xtf12"]+pos_seq["xg"],pos_seq["xtf12"]+pos_seq["xg"])
Z_th_pos = z_p(xp1, xp2)

print("Z_th_pos: "+str(round(abs(Z_th_pos),d)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_pos)))+" (degrees)")


#NEGATIVE SEQUENCE

xn1 = neg_seq["xm"]+neg_seq["xtf3"]+neg_seq["xt"]
xn2 = z_p(neg_seq["xtf12"]+neg_seq["xg"],neg_seq["xtf12"]+neg_seq["xg"])
Z_th_neg = z_p(xn1, xn2)

print("Z_th_neg: "+str(round(abs(Z_th_neg),d)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_neg)))+" (degrees)")


#ZERO SEQUENCE

Z_th_zero = zero_seq["xtf12"]+zero_seq["xg"]+xgg*3
print("Z_th_zero: "+str(round(abs(Z_th_zero),d)) + " (Magnitude)  " + str(math.degrees(cmath.phase(Z_th_zero)))+" (degrees)")

#PART 2

# For balanced faults, only the positive sequance is considered.
vf_pre = 1.02

I0_2 = 0
Ip_2 = vf_pre/Z_th_pos
In_2 = 0

#Sequence currents
I_seq_2 = np.array([[I0_2],
                  [Ip_2],
                  [In_2]])

If_ph_2 = np.dot(T, I_seq_2)

print("Ia = : " +str(np.abs(If_ph_2[0])) + "  " +str(np.angle(If_ph_2[0], deg=True)))
print("Ib = : " +str(np.abs(If_ph_2[1])) + "  " +str(np.angle(If_ph_2[1], deg=True)))
print("Ic = : " +str(np.abs(If_ph_2[2])) + "  " +str(np.angle(If_ph_2[2], deg=True)))

from re import I
#PART 3

#Assume fault occur between phase A and Groung. Therefore, current flows only in phase A. Therefore, Ib=0 and Ic =0
Ip_3 = vf_pre/(Z_th_pos+Z_th_neg+Z_th_zero)
In_3 = Ip_3
I0_3 = Ip_3

I_seq_3 = np.array([[I0_3],
                    [Ip_3],
                    [In_3]])

If_ph_3 = np.dot(T, I_seq_3)

print("Ia = : " +str(np.abs(If_ph_3[0])) + "  " +str(np.angle(If_ph_3[0], deg=True)))
print("Ib = : " +str(np.abs(If_ph_3[1])) + "  " +str(np.angle(If_ph_3[1], deg=True)))
print("Ic = : " +str(np.abs(If_ph_3[2])) + "  " +str(np.angle(If_ph_3[2], deg=True)))

Ia = Ip_3 + In_3 + I0_3
Ib =0
Ic =0

print("Ia = : " +str(abs(Ia)) + "  " +str(np.angle(Ia, deg=True)))
print("Ib = : " +str(abs(Ib)) + "  " +str(np.angle(Ib, deg=True)))
print("Ic = : " +str(abs(Ic)) + "  " +str(np.angle(Ic, deg=True)))

#PART 4

Ip_4 = vf_pre/(Z_th_pos+Z_th_neg)

In_4 = -Ip_4
I0_4 = 0

I_seq_4 = np.array([[I0_4],
                    [Ip_4],
                    [In_4]])

If_ph_4 = np.dot(T, I_seq_4)

print("Ia = : " +str(np.abs(If_ph_4[0])) + "  " +str(np.angle(If_ph_4[0], deg=True)))
print("Ib = : " +str(np.abs(If_ph_4[1])) + "  " +str(np.angle(If_ph_4[1], deg=True)))
print("Ic = : " +str(np.abs(If_ph_4[2])) + "  " +str(np.angle(If_ph_4[2], deg=True)))


print(round(-2.27421069e-14, 4))

#PART 5

#Assume fault is between phase B and C and ground. Then VB = VC = 0, IA = 0 and IB+IC = IF, Vp = Vn = V0

Ip_5 = vf_pre/(Z_th_pos + z_p(Z_th_neg,Z_th_zero))
Vp = z_p(Z_th_neg,Z_th_zero)*Ip_4

In_5 = -(Vp/Z_th_neg)
I0_5 = -(Vp/Z_th_zero)

I_seq_5 = np.array([[I0_5],
                    [Ip_5],
                    [In_5]])
If_ph_5 = np.dot(T, I_seq_5)

print("Ia = : " +str(np.abs(If_ph_5[0])) + "  " +str(np.angle(If_ph_5[0], deg=True)))
print("Ib = : " +str(np.abs(If_ph_5[1])) + "  " +str(np.angle(If_ph_5[1], deg=True)))
print("Ic = : " +str(np.abs(If_ph_5[2])) + "  " +str(np.angle(If_ph_5[2], deg=True)))

A = np.array([[-17j, 5j, 2j],
              [5j, -14j, 4j],
              [2j, 4j, -6j]], dtype=complex)

A_inv = np.linalg.inv(A)

print("Inverse of A:")
print(A_inv)

V_ph = np.array([[cmath.rect(280, math.radians(0))],
                 [cmath.rect(260, math.radians(-120))],
                 [cmath.rect(300, math.radians(115))]])


V = np.dot(T_1, V_ph)/3

print(np.abs(V))
print(np.angle(V, deg=True))

import numpy as np

# Create a 2D NumPy array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Access elements in a 2D array
element = arr_2d[1, 2]  # Access the element at row 1, column 2 (6)

print("Element:", element)

import numpy as np

# Create a 3x3 matrix
matrix_3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# Create a 3x1 column vector
vector_3x1 = np.array([[1],
                       [2],
                       [3]])

# Perform matrix multiplication using numpy.dot() or numpy.matmul()
result = np.dot(matrix_3x3, vector_3x1)  # or np.matmul(matrix_3x3, vector_3x1)

print("Result of matrix multiplication:")
print(result)
