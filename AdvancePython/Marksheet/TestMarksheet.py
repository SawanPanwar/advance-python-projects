import MarksheetBean
from MarksheetBean import *
import MarksheetModel
from MarksheetModel import *

class TestMarksheet:
    def testAdd(self):
        bean = MarksheetBean()
        bean.setId(10)
        bean.setRollNo(110)
        bean.setName('rahul')
        bean.setPhysics(70)
        bean.setChemistry(80)
        bean.setMaths(90)

        model = MarksheetModel()
        model.add(bean)

    def testUpdate(self):
        bean = MarksheetBean()
        bean.setId(10)
        bean.setRollNo(110)
        bean.setName('rahu')
        bean.setPhysics(77)
        bean.setChemistry(80)
        bean.setMaths(90)

        model = MarksheetModel()
        model.update(bean)

    def testDelete(self):
        model = MarksheetModel()
        model.delete(10)

    def testSearch(self):
        model = MarksheetModel()
        t = model.search()
        for row in t:
            print(row[0], ' ',row[1], ' ',row[2],' ',row[3],' ',row[4],' ',row[5])

    def testFindById(self):
        model = MarksheetModel()
        t = model.findById(9)
        for row in t:
            print(row[0], ' ',row[1], ' ',row[2],' ',row[3],' ',row[4],' ',row[5])


test = TestMarksheet()
#test.testAdd()
#test.testUpdate()
#test.testDelete()
#test.testSearch()
test.testFindById()