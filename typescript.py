# TypeScript for TV-class

class TV:
    #Constructor
    def __init__(self, brand):
        self.volume = 75
        self.channel = 1
        self.inches = 32
        self.brand = brand
        self.price = 10000
        # OnOFF state
        self.on = False
# method to increase Volume
    def volume_increase(self):
        if self.volume < 60:
            self.volume += 1
# Method to decrease Volume

    def volume_decrease(self):
        if self.volume > 0:
            self.volume -= 1
# Method fpr channel set

    def channel_set(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel
# Method for Tv reset
    def tv_reset(self):
        self.channel = 1
        self.volume = 50
#Method for status check
    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


# LED-TV Class
class LedTV(TV):
    def __init__(self, brand, screenThickness, energyUsage, lifespan, refreshRate):
        super().__init__(brand)
        self.viewingAngle = 0
        self.lifespan = lifespan
        self.refreshRate = refreshRate
        self.screenThickness = screenThickness
        self.energyUsage = energyUsage
        self.backLight = False

    def display_details(self):
        return f"Screen Thickness: {self.screenThickness} inches\n" \
               f"Energy Usage: {self.energyUsage} W\n" \
               f"Lifespan: {self.lifespan} years\n" \
               f"Refresh Rate: {self.refreshRate} Hz\n" \
               f"Viewing Angle: {self.viewingAngle} degrees\n" \
               f"Backlight: {'On' if self.backLight else 'Off'}"


# PART-B
class PlasmaTV(TV):
    def __init__(self, brand, screenThickness, energyUsage, lifespan, refreshRate):
        super().__init__(brand)
        self.screen_thickness = screenThickness
        self.energy_usage = energyUsage
        self.lifespan = lifespan
        self.refresh_rate = refreshRate
        self.viewing_angle = 0
        self.backlight = False

    def display_details(self):
        return f"Screen Thickness: {self.screen_thickness} inches\n" \
               f"Energy Usage: {self.energy_usage} W\n" \
               f"Lifespan: {self.lifespan} years\n" \
               f"Refresh Rate: {self.refresh_rate} Hz\n" \
               f"Viewing Angle: {self.viewing_angle} degrees\n" \
               f"Backlight: {'On' if self.backlight else 'Off'}"


led_tv = LedTV("Panasonic", 2.0, 200, 7, 132)
led_tv.volume_increase()
led_tv.channel_set(8)
print(led_tv.status())
print(led_tv.display_details())






