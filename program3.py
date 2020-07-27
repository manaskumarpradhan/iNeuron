def find_volume_of_sphere(diameter=12):
    D = diameter
    #raduis of the sphere
    r = D/2
    #pi value
    pi = 3.14
    #volume of sphere
    V = (4/3) * pi * (r*r*r)
    print("Volume of sphere is " ,V)
    return V
if __name__ == "__main__":
    find_volume_of_sphere()