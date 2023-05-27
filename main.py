def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(3)
input.on_button_pressed(Button.A, on_button_pressed_a)

radio.set_group(3)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)

def on_forever():
    pass
basic.forever(on_forever)
