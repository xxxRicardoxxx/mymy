#chapter1
from robodyno.components import Motor
from robodyno.interfaces import Webots
from robodyno.components import SliderModule
from controller import VacuumGripper

webots = Webots()
slider = SliderModule(webots, 0x10)
motor1 = Motor(webots, 0x11)
motor2 = Motor(webots, 0x12)
motor3 = Motor(webots, 0x13)
vacuum_gripper = webots.robot.getDevice("0x21")

slider.enable()

motor1.position_track_mode(2,1,1)
motor2.position_track_mode(2,1,1)
motor2.position_track_mode(2,1,1)

motor1.enable()
motor2.enable()
motor3.enable()

print(slider.get_pos())

motor1.set_pos(1.57)
webots.sleep(4)
slider.set_max_vel(2)
slider.set_pos(-0.1)

motor2.set_pos(-1.57)
webots.sleep(4)

motor1.set_pos(0)
webots.sleep(4)
slider.set_pos(0)
motor3.set_pos(2)

motor2.set_pos(0)
webots.sleep(4)


#chapter2
# import numpy as np
# import matplotlib.pyplot as plt

# theta_min = -1.57
# theta_max = 1.55
# step = 0.02

# theta1 = np.arange(theta_min, theta_max, step)
# theta2 = np.arange(theta_min, theta_max, step)
# theta3 = np.arange(theta_min, theta_max, step)

# L1 = 0.2
# L2 = 0.2
# L3 = 0.2

# points = []

# for t1 in theta1:
#     for t2 in theta2:
#         for t3 in theta3:
              
#             x = L1*np.cos(t1) + L2*np.cos(t1+t2) + L3*np.cos(t1+t2+t3)
#             y = L1*np.sin(t1) + L2*np.sin(t1+t2) + L3*np.sin(t1+t2+t3)
#             z = 0
            
#             points.append([x, y, z])

# points = np.array(points)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.scatter(points[:,0], points[:,1], points[:,2], s=1)

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# plt.show()