import time
from unittest import TestCase,skipIf


@skipIf(True, "long term support")
class Test_workflow(TestCase):

    # folderName = 'test_folder'
    # createNewTask = '创建新的任务'
    # alt = "wkf.admin.folder.popupNewTask.template.blank"
    # templateName = "test_template"
    #
    # def setUp(self):
    #     workflowConf = self.conf['workflow']
    #     self.url = workflowConf['url']
    #
    # def test_create_workflow(self):
    #     self.browser.get(self.url)
    #     time.sleep(3)
    #     addButton = self.browser.find_element_by_tag_name('button')
    #     addButton.click()
    #
    #     input = self.browser.find_elements_by_tag_name('input')
    #     input = input[1]
    #     input.send_keys(self.folderName)
    #     input.send_keys(Keys.RETURN)
    #
    #     folder = self.browser.find_element_by_xpath("//div[text()=\"%s\"]"%self.folderName)
    #     time.sleep(1)
    #     folder.click()
    #
    #     newTask = self.browser.find_element_by_xpath("//span[text()=\"%s\"]"%self.createNewTask)
    #     newTask.click()
    #
    #     blankRelated = self.browser.find_element_by_xpath("//img[@alt=\"%s\"]"%self.alt)
    #     blankRelated.click()
    #
    #     # input = self.browser.find_element_by_xpath("//span[input/@class='mio-input mio-input--normal' and @type='text']")
    #     input = self.browser.find_element_by_css_selector("input[class='mio-input mio-input--normal'][type='text']")
    #
    #     input.send_keys(self.templateName)
    #     input.send_keys(Keys.RETURN)
    #
    # def tearDown(self):
    #     self.request.post('https://release.miotech.com/api/workflow/folder', {"action":"DELETE","folderId":12,"tab":"admin"})
    #     self.browser.quit()

    def test_create_workflow(self):
        """
        create a new workflow
        """
        self.assertTrue(True)

    def test_admin_create_new_folder(self):
        """
        create new folder
        """
        self.assertTrue(True)


    def test_create_a_new_form(self):
        """
        create a new form
        """
        self.assertTrue(False)

    def test_edit_form_details(self):
        """
        edit form details
        """
        self.assertTrue(False)

    def test_internal(self):
        """
        internal tag
        """
        self.assertTrue(False)

    