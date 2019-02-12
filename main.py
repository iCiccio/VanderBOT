from __future__ import print_function
from Vanderbilt import Vanderbilt

"""
Main module that starts the VanderBOT experiment.
"""


def main():
    robot_ip = "pepper.local"
    experiment = Vanderbilt(robot_ip=robot_ip, simulation=True, demo_number=2, mature=True, withUpdate=True)
    experiment.help_setup()
    experiment.start()


if __name__ == "__main__":
    main()
