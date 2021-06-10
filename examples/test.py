#!/usr/bin/env python3.8
import Robot_API

def main():

        robot = Robot_API.createRobot()

        count = 0
        on_off = 0

        while True:
                previous_time = robot.getTimestamp()
                print("Left encoder:  " + str(robot.getEncoder("left")))
                print("Right encoder: " + str(robot.getEncoder("right")))

                if (on_off==0):
                        robot.setMotorSpeed("left", 100)
                        robot.setMotorSpeed("right",100)
                else:
                        robot.setMotorSpeed("left", -100)
                        robot.setMotorSpeed("right", -100)

                #robot.setDigitalPinValue(9, int(on_off))
                distance = robot.getDistance("front")
                robot.setLED(int(distance))
                current_time = robot.getTimestamp()

                while (current_time - previous_time < 1):
                        current_time = robot.getTimestamp()

                count = count + 1
                print(count)
                print("On/Off = " + str(on_off))
                print("Button = " + str(robot.getDigitalPinValue(3)))
                print("Distance = " + str(distance))
                print("-----------------------------------")

                if (on_off == 1):
                        on_off = 0
                else:
                        on_off = on_off + 1

if __name__=="__main__":
        main()