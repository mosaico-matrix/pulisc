from mosaico import widget

# Vacuum
vacuum = widget.createImage()
vacuum.setImage(widget.widgetAsset("vacuum.ppm"))
vacuum.moveTo(70, 30)
# vacuum.flipHorizontally()
vacuum.animateTo(-40, 30, 4000)

# Name
name = widget.createText()
name.setText("Monoa")
name.setFont("10x20")
name.moveTo(3, 7)

# Called once each frame
flipped = False

def loop():
    global flipped
    if vacuum.isAnimating():
        return
    elif flipped:
        flipped = False
        vacuum.flipHorizontally()
        vacuum.animateTo(-40, 30, 4000)
    else:
        flipped = True
        vacuum.flipHorizontally()
        vacuum.animateTo(80, 30, 4000)
