#!/usr/bin/env python3

import rospy
import pre_setup_diags
from pre_setup_diags import CheckOwnHost, PingHost, Sound, Video, CheckRemoteChrony, CheckRemoteRealsense


rospy.init_node("pre_setup_tester")

tests = []

#tests.append(CheckOwnHost())
tests.append(PingHost("router","192.168.1.1"))
#tests.append(PingHost("myself","192.168.1.100", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
#tests.append(PingHost("tablet","192.168.1.101", tips=["You can also use VNC to control the tablet now. Just connect to:\n\n\thttp://192.168.1.101:5800/vnc.html?autoconnect=true&show_dot=true&192.168.1.101&port=5900 \n"]))
#tests.append(PingHost("vicon pc","192.168.1.103", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
tests.append(Sound("/srv/data/calib.wav"))


NORMAL_PC_WITH_WEBCAM = False
if NORMAL_PC_WITH_WEBCAM:
    tests.append(Video("/dev/video0", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
    ## I am maybe being a bit pedantic here, but these extra devices are not useless specially since it appears they provide better timestamping information, which we may want
    ## But even if I want to check those, which I don't think I do, the correct type of test is not implemented
    ## source https://unix.stackexchange.com/questions/512759/multiple-dev-video-for-one-physical-device
    ## more info https://linuxtv.org/downloads/v4l-dvb-apis/userspace-api/v4l/dev-meta.html and here: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=088ead25524583e2200aa99111bea2f66a86545a
    #
    #tests.append(Video("/dev/video1", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
    tests.append(Video("/dev/video2", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
    ## you can play it with gst-launch-1.0 -v v4l2src device=/dev/video2 ! videoconvert ! autovideosink

    #tests.append(Video("/dev/video3", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))

    tests.append(Video("/dev/video4", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT)) ## this is the main device
    #tests.append(Video("/dev/video5", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
    tests.append(Video("/dev/video6", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
    ## you can play it with : gst-launch-1.0 -v v4l2src device=/dev/video6 ! videoconvert ! autovideosink
    #tests.append(Video("/dev/video7", criticality=pre_setup_diags.OPTIONAL_REQUIREMENT))
else:
    ## check if we have a realsense maybe?

    pass
##yaml... we can also have different usernames
machines = {"rpi5-silver-ubuntu":"192.168.1.4", "raspberrypi":"192.168.1.5", "rpi5-ubuntu":"192.168.1.3"}
for machine, ip in machines.items():
    tests.append(PingHost(machine, ip)) ## we wont use ip here
    tests.append(CheckRemoteChrony("frederico",machine, criticality=pre_setup_diags.CRITICAL_REQUIREMENT))
    tests.append(CheckRemoteRealsense("frederico", machine))

pre_setup_diags.do(tests)

