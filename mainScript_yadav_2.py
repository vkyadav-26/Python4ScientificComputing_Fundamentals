import os
os.chdir("C:\Users\vipinkmr0808\Desktop\energy engg")

import wallCalculation_yadav_1 as FC
print "calculation for stud resistance"
R_atStud=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","woodStud_90mm","gypsum_13mm","insideSurface"]


Rtot_stud= FC.wallcalculation_parallel(R_atStud)

Ustud = 1/Rtot_stud["R total"]
fstud = 0.25
Ustud_tot = fstud*Ustud

print "The total heat transfer coefficient at stud is " + str(Ustud) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"

print "calculation for insulation resistance"
R_betweenStud=["outsideSurfaceWinter","woodBevelLappedsliding_200mm","woodFiberBoard_13mm","glassFibreInsulation_25mm","gypsum_13mm","insideSurface"]


Rtot_betweenStud= FC.wallcalculation_parallel(R_betweenStud)

U_betweenstud = 1/Rtot_betweenStud["R total"]
f_insu = 0.75
Ub_stud_tot = f_insu*U_betweenstud

print "The total heat transfer coefficient at insulation is " + str(U_betweenstud) + " (W/m^2 deg C)"
print "The total heat transfer coefficient at insulation stud with 0.75 fraction area is " + str(Ub_stud_tot) + " (W/m^2 deg C)"

U_tot=Ustud+U_betweenstud
print "the overall heat transfer coefficient is " + str(U_tot)+ "(W/m^2 deg C)" 


print "calculation for door"
door_layer = ["wood50mm","outsideSurfaceWinter","insideSurface"]
    
Rtot_door = FC.wallcalculations_series(door_layer)

U_door = 1/Rtot_door["R total"]
print "The total heat transfer coefficient for door " + str(U_door) + " (W/m^2 deg C)"

print " calculation for ceiling"
The_ceiling = ["Added_insulation"]
    
Rtot_ceiling = FC.wallcalculations_series(The_ceiling)

U_ceiling = 1/Rtot_ceiling["R total"]
print "The total heat transfer coefficient for ceiling " + str(U_ceiling) + " (W/m^2 deg C)"

Tin = 20
Tout = -4.8

T_diff=Tin-Tout

print "The differential temperature between inside and outside of the wall is " + str(T_diff) + " (Deg C)"


A_wall = 105.8
A_door = 2.2
A_ceiling = 200

print "The total area of the wall is " + str(A_wall) + " (m^2)"
print "*********************************************************"

# Q total

Q_wall = U_tot*A_wall*T_diff
Q_door= U_door*A_door*T_diff
Q_ceiling= U_ceiling*A_ceiling*T_diff

Q= Q_wall+Q_door+Q_ceiling

# change from Watt to KWatt

Qtot = Q/1000


