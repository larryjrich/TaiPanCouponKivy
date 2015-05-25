from kivy.app import App
from kivy.uix.widget import Widget
from TaiPanCoupon import TaiPanCoupon

__version__ = 0.8


class TaiPanRootWidget(Widget):

    def search_taipan_coupon(self):
        tai_pan_coupon = TaiPanCoupon(days=int(self.text_days.text))
        coupon_results = tai_pan_coupon.fetch_coupon()
        if coupon_results:
            self.coupon_image.source = coupon_results[0]


class TaiPanCouponApp(App):
    def build(self):
        return TaiPanRootWidget()

if __name__ == '__main__':
    TaiPanCouponApp().run()