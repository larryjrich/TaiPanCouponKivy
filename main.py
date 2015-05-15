from kivy.app import App
from kivy.uix.widget import Widget


#TODO Write base Coupon class and TaiPanCoupon subclass. Keep MVC seperate.

class TaiPanRootWidget(Widget):
    pass


class TaiPanCouponApp(App):
    def build(self):
        return TaiPanRootWidget()


if __name__ == '__main__':
    TaiPanCouponApp().run()