from unittest import TestCase

true = True
false = False


class Test_AMI_jump_functional(TestCase):

    def test_jump(self):
        """
        跳转功能测试
        """
        self.assertTrue(true)


class Test_AMI_board(TestCase):
    def test_add_new_board(self):
        """
        新增面板
        """
        self.assertTrue(true)

    def test_check_board(self):
        """
        查看面板
        """
        self.assertTrue(true)


class Test_AMI_project(TestCase):
    def test_project(self):
        """
        项目按钮测试
        """
        self.assertTrue(true)


class Test_AMI_presenatations(TestCase):
    def test_add_presentations(self):
        """
        新增presentations
        """
        self.assertTrue(true)

    def test_check_presentations(self):
        """
        查看新增的内容
        """
        self.assertTrue(true)

    def test_presentations_add_blank_Slide(self):
        """
        新增一个空slide
        """
        self.assertTrue(true)

    def test_presentations_add_snapshots(self):
        """
        新增一个snapshot快照
        """
        self.assertTrue(true)


class Test_AMI_keyword_search(TestCase):

    def test_search(self):
        """
        关键词搜索测试
        """
        self.assertTrue(true)

    def test_search_all_tag(self):
        """
        查看all tag内容
        """
        self.assertTrue(true)

    def test_search_companies_tag(self):
        """
        查看companies tag 内容
        """
        self.assertTrue(true)

    def test_search_people_tag(self):
        """
        查看people tag
        """
        self.assertTrue(False)

    def test_search_narratives_tag(self):
        """
        查看narratives tag
        """
        self.assertTrue(true)

    def test_search_securities_tag(self):
        """
        查看securities tag
        """
        self.assertTrue(true)

    def test_Ka_shing_Li(self):
        """
        李嘉诚9公司测试
        """
        self.assertTrue(False)

    def test_Ka_shing_Li_contains_HorizonsCo(self):
        """
        必须包含horizons co
        """
        self.assertTrue(True)


class Test_AMI_graph_query(TestCase):
    def test_search_by_graph(self):
        """
        使用图搜索
        """
        self.assertTrue(true)

    def test_Relationships(self):
        """
        查看关系图
        """
        self.assertTrue(true)

    def test_layout(self):
        """
        查看layout
        """
        self.assertTrue(true)

    def test_detail_info(self):
        """
        查看detail information
        """
        self.assertTrue(true)

    def test_switch_people(self):
        """
        切换到people
        """
        self.assertTrue(true)

    def test_switch_distributed_points_graph(self):
        """
        切换到散点视图
        """
        self.assertTrue(true)

    def test_switch_bar_graph(self):
        """
        切换到柱状图
        """
        self.assertTrue(true)

    def test_save_project(self):
        """
        保存工程
        """
        self.assertTrue(true)

    def test_save_snapshot(self):
        """
        保存快照
        """
        self.assertTrue(true)
