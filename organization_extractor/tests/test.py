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
        self.assertEqual(organization, "Mars University")
 
    def test2(self):
        text = "Before she joined the Outerspace Group and then Mars University, she worked for NASA and ..."
        organizations = extract_organizations(text)
        self.assertTrue("Outerspace Group" in organizations)
        self.assertTrue("Mars University" in organizations)
        
    def testArabic1(self):
        text = """
        ويقول ماتياز من الأكاديمية السلوفينية للعلوم والفنون بالعاصمة ليوبليانا، والذي عكف على دراسة هذا النوع من العناكب منذ اكتشافه، إن "طول جسم أنثى عنكبوت لحاء داروين لا يزيد على 1.5 سنتيمتر، أما الوزن فيصل إلى نصف غرام، في حين يكون الذكور أصغر حجما بكثير، إذ تقل أوزانها عن أوزان الإناث بواقع عشر مرات". كما أن أجساد هذه العناكب مموهة، لكي تحاكي شكل لحاء الأشجار، التي تعيش بالقرب منها.
        """.decode("utf-8")
        organization = extract_organization(text)
        self.assertEqual(organization, """الأكاديمية السلوفينية للعلوم والفنون""".decode("utf-8"))

    def testArabicWal(self):
        # translates to army of the thing and the thing
        # we use this to test wal
        text = u"\u062c\u064a\u0634 \u0627\u0644\u0634\u064a\u0621 \u0648\u0627\u0644\u0634\u064a\u0621"
        organization = extract_organization(text)
        self.assertEqual(organization, text)

    def testFlag(self):
        text = "Flag of Pluto Group"
        organization = extract_organization(text)
        self.assertEqual("Pluto Group", organization)

    def testStartLower(self):
        text = "amount of Cool Party"
        organization = extract_organization(text)
        self.assertEqual("Cool Party", organization)

    def testArabicEndings(self):
        text = u"""
 (\u0627\u0644\u062d\u0631\u0643\u0629 \u0627\u0644\u0648\u0637\u0646\u064a\u0629 \u0627\u0644\u0634\u0639\u0628\u064a\u0629 \u0627\u0644\u0644\u064a\u0628\u064a\u0629\u200e)" src
        """
        organization = extract_organization(text)
        self.assertEqual(u"\u0627\u0644\u062d\u0631\u0643\u0629 \u0627\u0644\u0648\u0637\u0646\u064a\u0629 \u0627\u0644\u0634\u0639\u0628\u064a\u0629 \u0627\u0644\u0644\u064a\u0628\u064a\u0629", organization)
        
    def testSlash(self):
        text = u"""He was a member of the Non-Aligned Movement."""
        organization = extract_organization(text)
        self.assertEqual("Non-Aligned Movement", organization)

    def testOn(self):
        text = u"The Court on Transitional Issues is located somewhere."
        organization = extract_organization(text)
        self.assertEqual("The Court on Transitional Issues", organization)

    def testFor(self):
        text = u"I work for the International Institute for Migration."
        organization = extract_organization(text)
        self.assertEqual("International Institute for Migration", organization)

if __name__ == '__main__':
    unittest.main()
