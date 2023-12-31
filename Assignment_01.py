# -*- coding: utf-8 -*-
##Transmission Line model

#Assignment 01 - Answers
import cmath
import math
import matplotlib.pyplot as plt

#PART 1
#Data

z = 0.017 + 0.301j  #Series impedance per unit length (ohm/km)
y = 0 + 0.0000049j  #Shunt admittance per unit length (S/km)

V = 750             #Transmission line rated voltage (kV)
l = 300             #Transmission line length (kA)

ph_angle = 33       #Practical limit for phase angle (deg)

Ifl = 1.88          #Full load current (kA)
Vr = 0.9525         #Recieving end voltage (pu)

E = 73              #Shunt reactive compensation(%)
C_series =37        #Series Capacitive compensation(%)

#PART 1 - (a) - i

gamma = cmath.sqrt(z*y)
print("Propegation constant: "+str(gamma))

#PART 1 - (a) - ii

Zc = cmath.sqrt(z/y)
Yc = cmath.sqrt(y/z)
print("Characteristic Impedence: " +str(Zc))

#PART 1 - (a) - iii

#Exact ABCD Parameters

A = cmath.cosh(gamma*l)
B = Zc*cmath.sinh(gamma*l)
C = Yc*cmath.sinh(gamma*l)
D =A

print("A: "+str(abs(A)) + " (Magnitude)  " + str(math.degrees(cmath.phase(A)))+" (degrees)")
print("B: "+str(abs(B)) + " (Magnitude)  " + str(math.degrees(cmath.phase(B)))+" (degrees)")
print("C: "+str(abs(C)) + " (Magnitude)  " + str(math.degrees(cmath.phase(C)))+" (degrees)")
print("D: "+str(abs(D)) + " (Magnitude)  " + str(math.degrees(cmath.phase(D)))+" (degrees)")

#PART 1 - (a) - iv

#Z' and Y'

Z = B           #Z' value
Y = 2*((A-1)/B) #Y' value

print("Z': "+str(abs(Z)) + " (ohm) " + str(math.degrees(cmath.phase(Z))) +" (degree)")
print("Y': "+str(abs(Y)) + " (S) " + str(math.degrees(cmath.phase(Y))) +" (degree)")

#PART 1 - (b)

#function to calculate nominal Z and Y values
def nominal_values(l):
  Z = abs(z*l)
  Y = abs(y*l)/2

  return Z, Y

def exact_values(l):
  A = cmath.cosh(gamma*l)
  B = Zc*cmath.sinh(gamma*l)
  C = Yc*cmath.sinh(gamma*l)
  D =A

  Z = abs(B)
  Y = abs(2*((A-1)/B))/2

  return Z,Y

lengths = [*range(200, 1001, 50)]

Z_nominal, Y_nominal, Z_exact, Y_exact =[],[],[],[]

for i in lengths:
  Z_nominal.append(nominal_values(i)[0])
  Y_nominal.append(nominal_values(i)[1])

for i in lengths:
  Z_exact.append(exact_values(i)[0])
  Y_exact.append(exact_values(i)[1])

#Comparison of Z values

plt.plot(lengths, Z_nominal)
plt.plot(lengths, Z_exact)

plt.xlabel("Length (km)")
plt.ylabel("Z' (Ohm)")
plt.title("Variation of Z nominal and Z exact with Line length")
plt.legend(["Nominal Z'","Exact Z'"], loc ="lower right")

#Comparison of Y'/2 values

plt.plot(lengths, Y_nominal)
plt.plot(lengths, Y_exact)

plt.xlabel("Length (km)")
plt.ylabel("Y'/2 (S)")
plt.title("Variation of Y nominal and Y exact with Line length")
plt.legend(["Nominal Y'/2","Exact Y'/2"], loc ="lower right")

#PART 2 - (a) - i

rated_voltage = V
surge_impedence = Zc.real
SIL = rated_voltage**2/surge_impedence

print("SIL: "+ str(SIL) + " (MW)")

#PART 2 - (a) - ii

thetaA = cmath.phase(A)
thetaB = cmath.phase(B)

p_max_real = (V**2*math.cos(0))/abs(B)-(abs(A)*V**2*math.cos(thetaB-thetaA))/abs(B)

#print(p_max_real)

#theoretical maximum real power delivery as a percentage of SIL

SIL_percentage = p_max_real*100/SIL
print("Theoretical maximum real power delivery: " + str(SIL_percentage) +" %")

#PART 2 (b)

V_new = 500 #Nominal voltage

SIL_new = V_new**2/surge_impedence
print("SIL: "+str(SIL_new) +" (MW)")

p_max_real_new = (V_new**2*math.cos(0))/abs(B)-(abs(A)*V_new**2*math.cos(thetaB-thetaA))/abs(B)
print("Theoretical Maximum real power transfer: " + str(p_max_real_new) + " (MW)")

#PART 3 - (a) - i

V_base = V

V_sending_pu = 1.02
V_sending = V_sending_pu*V_base

V_recieving_pu = 0.98
V_recieving = V_recieving_pu*V_base


p_max_real_practical = (V_sending*V_recieving*math.cos(thetaB-math.radians(ph_angle)))/abs(B)-(abs(A)*V_recieving**2*math.cos(thetaB-thetaA))/abs(B)

SIL_percentage_practical = p_max_real_practical*100/SIL
print("Practical line loadability: " + str(SIL_percentage_practical) + " %")

#PART 3 - (b)

V_base_new = 500  #Nominal voltage

V_sending_pu = 1.02
V_sending = V_sending_pu*V_base_new

V_recieving_pu = 0.98
V_recieving = V_recieving_pu*V_base_new

p_max_real_practical_new = (V_sending*V_recieving*math.cos(thetaB-math.radians(ph_angle)))/abs(B)-(abs(A)*V_recieving**2*math.cos(thetaB-thetaA))/abs(B)

SIL_percentage_practical_new = p_max_real_practical_new*100/SIL
print("Practical line loadability: " + str(p_max_real_practical_new) + " (MW)")

#PART 4 - i

#Sending end voltage can be calculated using Two port equation. (Full load)
Vs_FL = A*Vr*V + B*Ifl*math.sqrt(3)

print("Vs_FL: "+str(abs(Vs_FL))+ " (kV)")
print("Angle(FL): "+str(math.degrees(cmath.phase(Vs_FL))) + " (degree)")

#PART 4 - ii

#No load operation
Vr_NL = Vs_FL/A

print("Vr_NL: " + str(abs(Vr_NL)) +" (kV)")
print("Angle (NL): " + str(math.degrees(cmath.phase(Vr_NL))) +" (degree)")

#PART 4 -iii

Vr_FL = Vr*V_base

V_regulation = 100*(abs(Vr_NL)-abs(Vr_FL))/abs(Vr_FL)

print("Voltage Regulation: "+str(V_regulation) + " %")

#PART 5 - (a) - i

#Y' = G' + jB'
G = Y.real
B_1 = Y.imag

B_new = (1-E/100)*B_1
Y_new = complex(G, B_new)


#B=Z'
B_new = Z

#A = (B*Y'/2)+1
A_new = (B_new*Y_new/2)+1

print("A_new: "+str(abs(A_new)) + " (Magnitude)   " + str(math.degrees(cmath.phase(A_new)))+ " (degree)")
print("B_new: "+str(abs(B_new)) + " (Magnitude)   " + str(math.degrees(cmath.phase(B_new))) + " (degree)")

#PART 5 - (a) - ii.

Vs_FL_new = A_new*Vr*V_base + B_new*Ifl*math.sqrt(3)

print("Vs_FL_new: "+str(abs(Vs_FL_new))+ " (kV)")
print("Angle (FL_new): "+str(math.degrees(cmath.phase(Vs_FL_new))) + " (degree)")

#PART 5 - (a) - iii.
#No load operation
Vr_NL_new = Vs_FL_new/A_new

print("Vr_NL_new: " + str(abs(Vr_NL_new)) +" (kV)")
print("Angle (NL_new): " + str(math.degrees(cmath.phase(Vr_NL_new))) +" (degree)")

#PART 5 - (a) - iv.

V_regulation_new = ((abs(Vr_NL_new)-abs(Vr_FL))*100)/abs(Vr_FL)

print("Voltage Regulation: "+str(V_regulation_new)+" %")

#PART 5 - (a) - v

Vr_NL_A_new = Vs_FL/A_new

print("Vr_NL_A_new: " + str(abs(Vr_NL_A_new)) +" (kV)")
print("Angle (NL_A_new): " + str(math.degrees(cmath.phase(Vr_NL_A_new))) +" (degree)")

#PART 5 - (a) - vi

V_regulation_A_new = ((abs(Vr_NL_A_new)-abs(Vr_FL))*100)/abs(Vr_FL)

print("Voltage Regulation: "+str(V_regulation_A_new)+" %")

#PART 5 - (b)

Vr_FL_500 =500
Vr_NL_500 = 500/A_new

V_regulation_new_500 = ((abs(Vr_NL_500)-abs(Vr_FL_500))*100)/abs(Vr_FL_500)

print("Voltage Regulation: "+str(V_regulation_new_500)+" %")

#PART 6 - (a) -i

#C_series = 100

X_dash = Z.imag
Z_cap = complex(0,-0.5*X_dash*C_series/100)
print("Z_cap: " + str(Z_cap))

#PART 6 - (a) - ii.

A_eq = A + C*Z_cap
B_eq = C*(Z_cap**2) + (A+D)*Z_cap + B

print("A_eq: "+str(abs(A_eq)) + " (Magnitude)  " + str(math.degrees(cmath.phase(A_eq))) + " (degrees)")
print("B_eq: "+str(abs(B_eq)) + " (Magnitude)  " + str(math.degrees(cmath.phase(B_eq))) + " (degrees)")

#PART 6 - (a) - iii

#at max power, |Vr_comm| = |Vs_comm| = |V_rated| and Cos(Theta_B - delta) = 1

thetaA_eq = cmath.phase(A_eq)
thetaB_eq = cmath.phase(B_eq)

Pr = (V**2*math.cos(0))/abs(B_eq)-(abs(A_eq)*V**2*math.cos(thetaB_eq-thetaA_eq))/abs(B_eq)

print("Theoretical maximum loadability: "+str(Pr)+" (MW)")

#PART 6 - (a) - iv

Pr_uncomp = p_max_real      #Real power of uncompensated line
Pr_comp = Pr                #Real power of compensated line

print(str((Pr_comp-Pr_uncomp)*100/SIL)+" %")

#PART 6 - (a) - v

V_base = V

V_sending_pu = 1.02
V_sending = V_sending_pu*V_base

V_recieving_pu = 0.98
V_recieving = V_recieving_pu*V_base

p_max_real_comp = (V_sending*V_recieving*math.cos(thetaB_eq-math.radians(ph_angle)))/abs(B_eq)-(abs(A_eq)*V_recieving**2*math.cos(thetaB_eq-thetaA_eq))/abs(B_eq)

print("Practical line loadability: " + str(p_max_real_comp) + " (MW)")

#PART 6 - (a) - vi

Pr_practical_uncomp = p_max_real_practical
print(str((p_max_real_comp-Pr_practical_uncomp)*100/SIL)+ " %")

#PART 6 - (b)

V_base = 500      #Nominal voltage

V_sending_pu = 1.02
V_sending = V_sending_pu*V_base

V_recieving_pu = 0.98
V_recieving = V_recieving_pu*V_base

p_max_real_comp = (V_sending*V_recieving*math.cos(thetaB_eq-math.radians(ph_angle)))/abs(B_eq)-(abs(A_eq)*V_recieving**2*math.cos(thetaB_eq-thetaA_eq))/abs(B_eq)

print("Practical line loadability: " + str(p_max_real_comp) + " (MW)")

#Increasning loadability by setting series capacitive compensation to 100%

C_series_new = 100

X_dash = Z.imag
Z_cap = complex(0,-0.5*X_dash*C_series_new/100)

A_eq = A + C*Z_cap
B_eq = C*(Z_cap**2) + (A+D)*Z_cap + B

thetaA_eq = cmath.phase(A_eq)
thetaB_eq = cmath.phase(B_eq)

V_base = 500
V_sending_pu = 1.02
V_sending = V_sending_pu*V_base
V_recieving_pu = 0.98
V_recieving = V_recieving_pu*V_base
p_max_real_comp = (V_sending*V_recieving*math.cos(thetaB_eq-math.radians(ph_angle)))/abs(B_eq)-(abs(A_eq)*V_recieving**2*math.cos(thetaB_eq-thetaA_eq))/abs(B_eq)

print("Practical line loadability (Max): " + str(p_max_real_comp) + " (MW)")
