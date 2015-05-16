import requests
from BeautifulSoup import BeautifulSoup
from datetime import datetime, timedelta
from Coupon import Coupon


class TaiPanCoupon(Coupon):

    def __init__(self, days=7):
        self.url = 'http://www.taipantrading.com/'
        # get date ranges for last 7 days
        self.date_range = [datetime.today() - timedelta(day) for day in range(0, days)]
        self.save_file = False

    def fetch_coupon(self, save_file):
        self.save_file = save_file
        # loop through days and find coupon
        print 'Looking for coupons...'
        for date in self.date_range:
            month = date.month
            day = date.day
            year = str(date.year)[-2:]
            if month < 10:
                month = '0%s' % (month)
            if day < 10:
                day = '0%s' % (day)

            date_str_url = 'coupon-%s%s%s' % (month, day, year)

            # call pages and process results
            page_result = requests.get('%s%s' % (self.url, date_str_url))

            if page_result.status_code == 200:
                # parse page.  image should be inside anchor tag with slug href
                bs_content = BeautifulSoup(page_result.content)
                bs_coupon_link = bs_content.find('a', attrs={'href': '/%s' % date_str_url})

                if bs_coupon_link:
                    print 'Coupon has been found for %s/%s/%s!' % (date.month, date.day, date.year)
                    print 'Location: %s ' % bs_coupon_link.img['src']

                    # set link and filename
                    self.coupon_link = bs_coupon_link.img['src']
                    self.coupon_file = 'Tai-Pan-%s.jpg' % (date_str_url)

                    if self.save_file:
                        #write image file
                        coupon_result = requests.get(bs_coupon_link.img['src'], stream=True)

                        temp_file = open(self.coupon_file, 'w')
                        temp_file.write(coupon_result.content)
                        temp_file.close()
                    print 'Complete!'
                    return self.coupon_link, self.coupon_file
                    break
                else:
                    print 'Error finding image.'
            elif page_result.status_code == 404:  # doesn't exist
                print 'There are no coupons available for %s/%s/%s.' % (date.month, date.day, date.year)
            else:
                print 'Error connecting to the web page.'  # err 500 or other
        else:
            print 'No coupons found for the last %i days.' % (len(self.date_range))