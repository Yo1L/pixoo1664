# PIXOO1664

Unofficial Divoom pixoo REST library, beer not included.

To install
```bash
pip install pixoo1664
```

To use:
```python
from pixoo import Pixoo

pixoo = Pixoo("192.168.16.64")
```
## Text

To send text:
```python
pixoo.send_text("Hello there !")
```

To clear text:
```python
pixoo.clear_text()
```

## Image
To create and send an image:
```python
from PIL import Image, ImageDraw

img = Image.new("RGB", size=(64,64))

draw = ImageDraw.Draw(img)
draw.text(text="Who's the", xy=(3, 10), fill=(255, 43, 43, 255))
draw.text(text="BOSS NOW ??", xy=(3, 20), fill=(43, 255, 43, 255))
draw.line(xy=((0, 20), (64, 20)))

pixoo.send_image(img)
```

Send gif frames in one call (60ms btw frames)
```python
# list of Image
pixoo.send_images(images, speed=60)
```

## Brightness

Get brightness
```python
pixoo.get_brightness()
# => 0.8
```

Set brightness 0~100
```python
pixoo.set_brightness(0.9)
# => 0.8
```

Set screen on/off
```python
pixoo.set_screen(True)
pixoo.set_screen(False)
```

## Time

Set system time
```python
pixoo.set_system_time(1672416000)
```

## Temperature mode

Set temperature in Celsius
```python
pixoo.set_temperature_mode(celsius=True)
```

Set temperature in Fahrenheit
```python
pixoo.set_temperature_mode(celsius=False)
```

## Screen rotation

Set rotation angle in degree 0, 90, 180 and 270
```python
pixoo.set_rotation_angle(90)
```
