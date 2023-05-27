radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(3)
})
radio.setGroup(3)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
basic.showIcon(IconNames.Heart)
basic.forever(function () {
	
})
