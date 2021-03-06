from all_scrapers.Scraper_Controller import AbstractScraperClass


class Stopkova(AbstractScraperClass):
    def __init__(self):
        self.index_file = "centrum"
        self.url = f'https://www.kolkovna.cz/cs/stopkova-plzenska-pivnice-16/denni-menu'
        self.rep = "STOPKOVAREPLACEME"
        self.name = "Stopkova Pivnice"
        self.part_we_want = ['div', {'class': 'dailyMenuWeek'}]
        super().__init__(self.name, self.url, self.rep, self.part_we_want, self.index_file)

    def do_cleanup_html(self, cleaned_object):
        cleaned_object = cleaned_object.replace('<h2', '<h2 style="color:red; font-size:1.6em"')
        return cleaned_object

Stopkova().do_scraping()
