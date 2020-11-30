import scrapy
import re

class Bikes(scrapy.Spider):

    name = 'Bikes'

    def start_requests(self):
        # This url was changed everytime for every new brands of bikes
        url = 'https://hamrobazaar.com/search.php?do_search=Search&order=popularad&way=&searchword=&catid_search=129&city_search=&e_2=&e_1_from=&e_1_to=&e_4=&e_105_from=&e_105_to=&e_64_from=&e_64_to=&e_65_from=&e_65_to=&e_66_from=&e_66_to='
        yield scrapy.Request(url, callback=self.parsepage)

    def parsepage(self, response):
        # with open("bikes.html",'wb') as f:
        #     f.write(response.body)
        # print(response.css('table')[30].css('i::text').get())
        data = {}
        try:
            for i in range(28,50):
                x = response.css('table')[i].css('b::text').get()
                if x != None:
                    data['Name'] = x
                    a = response.css('table')[i].css('i::text').get()
                    c = re.findall('Lot No.*', a)
                    if c != []:
                        data['Lot No.'] = c[0][8:10]
                    else:
                        data['Lot No.'] = ''
                    d = re.findall('Kilometers:.*', a)
                    if d != []:
                        data['Kilometers'] = d[0][12:]
                    else:
                        data['Kilometers'] = ''
                    data['Price'] = response.css('table')[i].css('b::text')[2].get()
                yield data
            next = response.css('table')[50].css('a::attr(href)')[-1].get()
            yield scrapy.Request(url="https://hamrobazaar.com/search.php"+next, callback=self.parsepage)
        except:
            pass


    