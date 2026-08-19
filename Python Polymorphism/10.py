class andriod:
    def showfeatures(self):
        return "Android features: Customizable UI, Google Play Store, Multi-tasking"
class iphone:
    def showfeatures(self):
        return "iPhone features: Smooth performance, App Store, Face ID"
class windowsphone:
    def showfeatures(self):
        return "Windows Phone features: Live Tiles, Microsoft Store, Cortana"
andriod = andriod()
iphone = iphone()
windowsphone = windowsphone()
print(andriod.showfeatures())
print(iphone.showfeatures())
print(windowsphone.showfeatures())