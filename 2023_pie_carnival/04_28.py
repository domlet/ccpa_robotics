import time
# Define stuff.
motor_drive = "6_1313670031817441648"
motor_lift = "6_8847060420572259627"

# Driver mode
def teleop_setup(): # Setup runs once:
    print("driver mode is on")
    Robot.set_value(motor_drive,"invert_b",True)
    Robot.set_value(motor_lift,"invert_a",True)
    up    = Gamepad.get_value("dpad_up")
    down  = Gamepad.get_value("dpad_down")
    left  = Gamepad.get_value("dpad_left")
    right = Gamepad.get_value("dpad_right")
    drive = Gamepad.get_value("joystick_right_y")
    turn  = Gamepad.get_value("joystick_right_x")

def teleop_main(): # Runs continuously.
    # Robot.set_value(motor_drive,"velocity_a", max(min(drive - turn,1),-1))
    # Robot.set_value(motor_drive,"velocity_b", max(min(drive + turn,1),-1))
    # # Driving commands
    # Robot.set_value(motor_drive,"velocity_b", max(min(drive + turn,1),-1))
    # Robot.set_value(motor_drive,"velocity_a", max(min(drive - turn,1),-1))

    if Gamepad.get_value("dpad_down"):
        Robot.set_value(motor_lift,"velocity_b",0.5)
        
    if Gamepad.get_value("dpad_up"):
        Robot.set_value(motor_lift,"velocity_b",1.0)

# # # # # # # # # # # # # # # # # # # #  #

def autonomous_setup(): # Setup runs once:
    print("auto mode started")
    # Robot.run(autonomous_main)
    Robot.set_value(motor_drive,"invert_a",False) 
    Robot.set_value(motor_drive,"invert_b",False)
    # Robot.set_value(motor_lift,"invert_a",True)
    
def autonomous_main():
    # Go forward 27 inches:
    t_end = time.time() + .1
    while time.time() < t_end:
        Robot.set_value(motor_drive,"velocity_a", 0.5)
        Robot.set_value(motor_drive,"velocity_b", 0.5)
    # Turn clockwise 90 degrees: 
    
    # Robot.set_value(motor_lift,"velocity_a",max(min(  up - down,-1),1))
    # Robot.set_value(motor_lift,"velocity_b",max(min(  up + down,1),-1))
    # Robot.set_value(motor_lift,"velocity_a",max(min(left + right,1),-1))
    # Robot.set_value(motor_lift,"velocity_b",max(min(left - right,1),-1))
