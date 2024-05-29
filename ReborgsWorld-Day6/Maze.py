def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != 1:
    if right_is_clear() == 1 and front_is_clear() != 1:
        turn_right()
        move()
    elif right_is_clear() != 1 and front_is_clear() == 1:
        move()
    elif right_is_clear() == 1 and front_is_clear() == 1:
        move()
    elif right_is_clear() != 1 and front_is_clear() != 1:
        turn_left()
