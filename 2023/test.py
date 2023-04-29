# This robot has 2 motors:
motor_drive = "6_1313670031817441648"
motor_lift = "6_8847060420572259627"
hand_servo = "4_12516659289215747898"
def teleop_setup():
    Robot.set_value(motor_drive,"invert_a",True)
    Robot.set_value(motor_lift,"invert_a",True)

def teleop_main():
    #Game pad controls
    up    = Gamepad.get_value("dpad_up")
    down  = Gamepad.get_value("dpad_down")
    left  = Gamepad.get_value("dpad_left")
    right = Gamepad.get_value("dpad_right")
    #Not working yet
    drive = Gamepad.get_value("joystick_right_y")
    turn  = Gamepad.get_value("joystick_right_x")
    Open = Gamepad.get_value("r_bumper")

    # Driving commands
    Robot.set_value(motor_drive,"velocity_b", max(min(drive + turn,1),-1))
    Robot.set_value(motor_drive,"velocity_a", max(min(drive - turn,1),-1))
    # Lifting the arm
    Robot.set_value(motor_lift,"velocity_a",max(min(  up - down,1),-1))
    Robot.set_value(motor_lift,"velocity_b",max(min(  up + down,1),-1))
    #Robot.set_value(motor_lift,"velocity_a",max(min(left + right,1),-1))
    #Robot.set_value(motor_lift,"velocity_b",max(min(left - right,1),-1))
    #hand
    
    if Robot.set_value(hand_servo,0):
        print("the hand_servo is at 0")
    else:
        print("the hand_servo is NOT at 0")
       
    
    
    
  
 