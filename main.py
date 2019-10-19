import triad_openvr
import time
import sys
import numpy as np
import math
import pdb


def vive_tracker():
    deviceCount = 0

    try:
        v = triad_openvr.triad_openvr()
    except Exception as ex:
        if (type(ex).__name__ == 'OpenVRError' and ex.args[0] == 'VRInitError_Init_HmdNotFoundPresenceFailed (error number 126)'):
            print('Cannot find the tracker.')
            print('Is SteamVR running?')
            print('Is the Vive Tracker turned on, connected, and paired with SteamVR?')
            print('Are the Lighthouse Base Stations powered and in view of the Tracker?\n\n')
        else:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        print(ex.args)

    v.print_discovered_objects()

    while True:
        for deviceName in v.devices:

            # Publish a topic as euler angles
            [x,y,z,roll,pitch,yaw] = v.devices[deviceName].get_pose_euler()
            y_rot = math.radians(pitch)

            if deviceName == 'tracker_1':
                print(deviceName, x,y,z,roll,pitch,yaw)

        time.sleep(0.1)


if __name__ == '__main__':
    try:
        vive_tracker()
    except Exception as e:
        print(e)
