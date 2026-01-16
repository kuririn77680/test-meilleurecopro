from django.test import TestCase

from code_review.reworked.file import Tank, ArmorType

class TankTestCase(TestCase):
    t1 = Tank(600, 670, ArmorType.CHOBHAM, "Test1")
    t2 = Tank(620, 670, ArmorType.COMPOSITE, "Test2")
    t3 = Tank(620, 1000, ArmorType.CERAMIC, "Test3")


    def test_effective_armor(self):
        assert self.t1.effective_armor == 700
        assert self.t2.effective_armor == 670
        assert self.t3.effective_armor == 670

    def test_is_vulnerable_to(self):
        assert not self.t1.is_vulnerable_to(self.t2)
        assert self.t1.is_vulnerable_to(self.t3)

    def test_swap_armor(self):
        self.t1.swap_armor(self.t2)
        assert self.t1.armor == 620
        assert self.t2.armor == 600
