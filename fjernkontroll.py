def on_button_pressed_a():
    radio.send_string("start")


def on_button_pressed_b():
    radio.send_string("cross")


def on_button_pressed_ab():
    radio.send_string("open")

    
radio.set_group(70)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
