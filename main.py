def on_forever():
    basic.show_number(sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS))
basic.forever(on_forever)
