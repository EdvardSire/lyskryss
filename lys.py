north = [100, 101, 102]
east = [108, 112, 116]
# red, yellow, green

red_north = 100
yellow_north = 101
green_north = 102
red_east = 108
yellow_east = 112
green_east = 116

time_red = 3000
time_redyellow = 3000
time_beforegreen = 2000
time_green = 6000


def on_forever():
    # north, east
    # green, red
    pins.digital_write_pin(green_north, 1)
    pins.digital_write_pin(red_east, 1)
    basic.pause(time_green)

    # yellow, red
    pins.digital_write_pin(green_north, 0)
    pins.digital_write_pin(yellow_north, 1)
    basic.pause(time_redyellow)

    # red, red
    pins.digital_write_pin(yellow_north, 0)
    pins.digital_write_pin(red_north, 1)
    basic.pause(time_red)

    # red, yellow red
    pins.digital_write_pin(yellow_east, 1)
    basic.pause(time_beforegreen)

    # red, green
    pins.digital_write_pin(red_east, 0)
    pins.digital_write_pin(yellow_east, 0)
    pins.digital_write_pin(green_east, 1)
    basic.pause(time_green)

    # red, yellow
    pins.digital_write_pin(green_east, 0)
    pins.digital_write_pin(yellow_east, 1)
    basic.pause(time_redyellow)

    # red, red
    pins.digital_write_pin(yellow_east, 0)
    pins.digital_write_pin(red_east, 1)
    basic.pause(time_red)

    # yellow red, red
    pins.digital_write_pin(yellow_north, 1)
    basic.pause(time_beforegreen)


def on_received_string(receivedString):
    if receivedString == "start":
        # set all pins low
        for i in range(3):
            pins.digital_write_pin(north[i], 0)
            pins.digital_write_pin(east[i], 0)
        basic.forever(on_forever)
                

radio.set_group(70)
radio.on_received_string(on_received_string)
