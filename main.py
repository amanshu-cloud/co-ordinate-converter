from cartesian_to_cylindrical import *
from cartesian_to_spherical import *

val = str(input("enter input co-ordinate name: "))
output =str(input("enter output co-ordinate required: "))
list1 = input("enter the magnitude of that co-ord: ").split()
one,two,three = int(list1[0]),int(list1[1]),int(list1[2])

if val=="cartesian" and output=="cylindrical":
    print(convert_to_cylindrical(one,two,three))
elif val=="cylindrical" and output=="cartesian":
    print(reverse_1(one,two,three))

elif val=="cartesian" and output=="spherical":
    print(convert_to_spherical(one,two,three))
elif val=="spherical" and output=="cartesian":
    print(reverse_2(one,two,three))

elif val=="cylindrical" and output=="spherical":
    one_1,two_2,three_3=reverse_1(one,two,three)
    print(convert_to_spherical(one_1,two_2,three_3))
elif val=="spherical" and output=="cylindrical":
    one_1,two_2,three_3 = reverse_2(one,two,three)
    print(convert_to_cylindrical(one_1,two_2,three_3))
