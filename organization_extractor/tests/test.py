#-*- coding: utf-8 -*-
import unittest
from organization_extractor import extract_organization, extract_organizations
from bnlp import *

class TestMethods(unittest.TestCase):

    #def test_year(self):
    #    self.assertEqual(str(g("2015-11-21")),'2015-01-01 00:00:00+00:00')

    def test1(self):
        text = "In the year of 2050, he attended the Mars University."
        organization = extract_organization(text)
        print "extracted orgnization is", organization
        self.assertEqual(organization, "Mars University")
 
    def test2(self):
        text = "Before she joined the Outerspace Group and then Mars University, she worked for NASA and ..."
        print "\ntext is", text
        organizations = extract_organizations(text)
        print "extracted orgnizations is", organizations
        self.assertTrue("Outerspace Group" in organizations)
        self.assertTrue("Mars University" in organizations)
        
    def testArabic1(self):
        text = """
        ويقول ماتياز من الأكاديمية السلوفينية للعلوم والفنون بالعاصمة ليوبليانا، والذي عكف على دراسة هذا النوع من العناكب منذ اكتشافه، إن "طول جسم أنثى عنكبوت لحاء داروين لا يزيد على 1.5 سنتيمتر، أما الوزن فيصل إلى نصف غرام، في حين يكون الذكور أصغر حجما بكثير، إذ تقل أوزانها عن أوزان الإناث بواقع عشر مرات". كما أن أجساد هذه العناكب مموهة، لكي تحاكي شكل لحاء الأشجار، التي تعيش بالقرب منها.
        """.decode("utf-8")
        organization = extract_organization(text)
        self.assertEqual(organization, """الأكاديمية السلوفينية للعلوم والفنون""".decode("utf-8"))

if __name__ == '__main__':
    unittest.main()
