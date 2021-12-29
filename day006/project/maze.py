#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#doesn't work in all cases :(
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        if wall_in_front() and right_is_clear():
            turn_right()
            while front_is_clear():
                move()
            turn_right()
        elif wall_in_front() and wall_on_right():
            turn_left()
            if front_is_clear():
                move()
            else:
                turn_left()

sound(True)