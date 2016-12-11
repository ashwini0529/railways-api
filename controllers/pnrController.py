from modules import *
from bs4 import BeautifulSoup


class pnrHandler(tornado.web.RequestHandler):

    def get(self):
        pnr = self.get_argument('pnr', '')
        if(len(pnr) != 10):
            self.write({
                    'message': 'Please enter valid PNR',
                    'status': 'OK'
                    })
        else:
            url = "http://www.indianrail.gov.in/pnr_Enq.html"
            browser = mechanize.Browser()
            browser.open(url)
            browser.select_form(nr=0)
            browser.form['lccp_pnrno1'] = pnr
            browser.submit()
            soup = BeautifulSoup(browser.response().read())
            h3Tags = soup.findAll('h3')
            if(h3Tags[0].getText() == "Please Try Again"):
                self.write({
                        'message': 'Servers are busy. Please try again later.',
                        'status': 'OK'
                        })
