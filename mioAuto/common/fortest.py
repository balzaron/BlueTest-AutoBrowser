from unittest import TestCase


class caseTemplate(TestCase):
    _browser = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._browser = self.browser(kwargs.get('cookie'), kwargs.get('domain'))

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, cookie='', domaim=''):
        self._browser = cookie+domaim

    def tool1(self):
        print('tool1')



class case1(caseTemplate):

    # def __init__(self, cookie, domain):
    #     super().__init__(*args, **kwargs)

    def testM1(self):
        self.browser('cookie', 'domain')
        print(self.browser)

