from pico2d import *
import random

ground_width, ground_height = 1280, 1024
running = True
frame = 0
hand_x, hand_y = 0, 0
cha_x, cha_y = 0, 0

open_canvas(ground_width, ground_height)

ground = load_image('TUK_GROUND.png')
character = load_image('character.png')
hand = load_image('hand_arrow.png')

def handle_events() :
    global running

    events = get_events()
    for event in events :
        if(event.type == SDL_QUIT) :
            running = False
        elif(event.type == SDL_KEYDOWN) :
            if(event.key == SDLK_ESCAPE) :
                running = False
    

while(running) :
    clear_canvas()

    ground.draw(ground_width // 2, ground_height // 2)
    character.clip_draw(frame * 100, 0, 100, 100, ground_width // 2, ground_height // 2)

    if((hand_x, hand_y) == (cha_x, cha_y)) :
        hand_x, hand_y = random.randint(0, ground_width), random.randint(0, ground_height)
    hand.draw(hand_x, hand_y)

    update_canvas()
    handle_events()
    
    frame = (frame + 1) % 8

    delay(0.1)

close_canvas()
