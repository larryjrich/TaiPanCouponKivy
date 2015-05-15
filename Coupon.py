class Coupon(object):
    url = None
    coupon_link = None
    coupon_file = None

    def fetch_coupon(self):
        return None  # override in subclasses

    def save_coupon(self):
        pass  # override in subclasses