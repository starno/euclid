#G33 command runs a homing routine that calculates the build platform plane
#this script can be used to calculate vertical offset of end effector at given (x,y) location to be parallel with build platform

#G33 measured output button heights
z_Z = -3.27; #(mm) measured height of Z_TOWER button 
z_X = -3.38; #(mm) measured height of X_TOWER button
z_Y = -3.19; #(mm) measured height of Y_TOWER button 

#NiuB Platform Configuration
#button height offset
button_z = -3.3; #(mm) distance between top of buttons to build platform surface
#homing button locations
x_Z = -4.5; #(mm) x-coordinate of Z_TOWER button
y_Z = 95.0; #(mm) y-coordinate of Z_TOWER button
x_X = -79.0; #(mm) x-coordinate of X_TOWER button
y_X = -39.0; #(mm) y-coordinate of X_TOWER button
x_Y = 79.0; #(mm) x-coordinate of Y_TOWER button
y_Y = -39.0; #(mm) y-coordinate of Y_TOWER button

#arbitrary (x,y) location to check z-error
x = -4.5;
y = 95;

#button coordinates
Z_TOWER_button = (x_Z, y_Z, z_Z);
X_TOWER_button = (x_X, y_X, z_X);
Y_TOWER_button = (x_Y, y_Y, z_Y);

#calculating vectors from button coordinates to define platform plane
XY = str(x_Y - x_X) + "i + " + str(y_Y - y_X) + "j + " + str(z_Y - z_X) + "k"
XZ = str(x_Z - x_X) + "i + " + str(y_Z - y_X) + "j + " + str(z_Z - z_X) + "k"
#vector components
#XY
XYi = (x_Y - x_X);
XYj = (y_Y - y_X);
XYk = (z_Y - z_X);
#XZ
XZi = (x_Z - x_X);
XZj = (y_Z - y_X);
XZk = (z_Z - z_X);

#Find normal vector from build plane using cross product
#notation: (a1, a2, a3) X (b1, b2, b3) = (a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1)
normal_vector = (XYj*XZk - XYk*XZj, XYk*XZi - XYi*XZk, XYi*XZj - XYj*XZi);
alpha_x = XYj*XZk - XYk*XZj;
alpha_y = XYk*XZi - XYi*XZk;
alpha_z = XYi*XZj - XYj*XZi;

#Calculate Z-error
z = ((alpha_x*(x - x_Z) + alpha_y*(y - y_Z))/alpha_z) + z_Z; #magnitude of error

print
print "Button Locations:"
print "Z_TOWER_button = " + str(Z_TOWER_button)
print "X_TOWER_button = " + str(X_TOWER_button)
print "Y_TOWER_button = " + str(Y_TOWER_button)
print 
print "Calculated Build Platform Vectors:"
print "vector YX = " + str(XY)
print "vector XZ = " + str(XZ)
print 
print "Calculated Normal Vector:"
print "n = " + str(normal_vector)
print
print "Vertical Offset at Location (" + str(x) + ", " + str(y) + ", z) to be Parrallel with Build Platform:"
print "z = z - " + str(z - button_z)
print