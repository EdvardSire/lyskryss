red_light = 108
green_light = 112
# servo P0/100
# button P1/101

time_red = 3000
time_redyellow = 3000
time_beforegreen = 2000
time_green = 6000

cross = 0
test = 0

angle = 25


def on_forever():
    # north, east
    # green, red
    basic.pause(time_green)

    # yellow, red
    basic.pause(time_redyellow)

    # red, red
    basic.pause(time_red)

    # red, yellow red
    basic.pause(time_beforegreen)

    # red, green
    if cross == 1:
        pins.digital_write_pin(red_light, 0)
        pins.digital_write_pin(green_light, 1)
        zero()

    basic.pause(time_green)
    pins.digital_write_pin(red_light, 1)
    pins.digital_write_pin(green_light, 0)
        

    # red, yellow
    basic.pause(time_redyellow)

    # red, red
    basic.pause(time_red)

    # yellow red, red
    basic.pause(time_beforegreen)


def zero():
    global cross
    cross = 0


def on_received_string(receivedString):
    if receivedString == "start":
        pins.digital_write_pin(red_light, 1)
        pins.digital_write_pin(green_light, 0)
        servos.P0.set_angle(angle)
        basic.forever(on_forever)
        
    elif receivedString == "cross":
        global cross
        cross = 1

    elif receivedString == "open":
        button()


### servo ###
def button():
    servos.P0.set_angle(80)
    basic.pause(6000)
    servos.P0.set_angle(angle)


radio.set_group(70)
radio.on_received_string(on_received_string)
input.on_pin_pressed(TouchPin.P1, button)
