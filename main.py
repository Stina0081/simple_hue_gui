
import tkinter as tk
from phue import Bridge

# your bridge ip
HUE_BRIDGE_IP = 'your bridge ip'


bridge = Bridge(HUE_BRIDGE_IP)


bridge.connect()

def turn_on_lights():
    
    bridge.set_group(1, 'on', True)

def turn_off_lights():
    
    bridge.set_group(1, 'on', False)

def set_brightness(brightness):
    
    brightness = int((brightness / 100) * 254)
    
    bridge.set_group(1, 'bri', brightness)


window = tk.Tk()
window.title("hue lights controler")

on_button = tk.Button(window, text="Turn On", command=turn_on_lights)
on_button.pack(pady=10)

off_button = tk.Button(window, text="Turn Off", command=turn_off_lights)
off_button.pack(pady=10)

brightness_label = tk.Label(window, text="Brightness:")
brightness_label.pack(pady=5)

brightness_scale = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
brightness_scale.set(30)  
brightness_scale.pack(pady=5)

def update_brightness(brightness):
    
    set_brightness(int(brightness))

brightness_scale.config(command=update_brightness)



window.mainloop()
