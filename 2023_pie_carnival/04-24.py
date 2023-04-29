motor_drive = "6_1313670031817441648"
motor_lift = "6_8847060420572259627"

up    = Gamepad.get_value("dpad_up")
down  = Gamepad.get_value("dpad_down")
left  = Gamepad.get_value("dpad_left")
right = Gamepad.get_value("dpad_right")
drive = Gamepad.get_value("joystick_right_y")
turn  = Gamepad.get_value("joystick_right_x")

# def teleop_setup():
def teleop_main():
    Robot.set_value(motor_drive,"invert_b",True)
    Robot.set_value(motor_lift,"invert_a",True)

def autonomous_actions():
    # Driving commands
    Robot.set_value(motor_drive,"velocity_b", max(min(drive + turn,1),-1))
    Robot.set_value(motor_drive,"velocity_a", max(min(drive - turn,1),-1))
    # Lifting the arm
    Robot.set_value(motor_lift,"velocity_a",max(min(  up - down,-1),1))
    Robot.set_value(motor_lift,"velocity_b",max(min(  up + down,1),-1))
    Robot.set_value(motor_lift,"velocity_a",max(min(left + right,1),-1))
    Robot.set_value(motor_lift,"velocity_b",max(min(left - right,1),-1))
    
    if Gamepad.get_value("dpad_down"):
        Robot.set_value(motor_lift,"velocity_b",0.5)
        
    if Gamepad.get_value("dpad_up"):
        Robot.set_value(motor_lift,"velocity_b",1.0)