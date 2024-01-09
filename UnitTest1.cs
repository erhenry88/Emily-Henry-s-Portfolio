//Emily Henry
// October 10,2021
//Module 7 Written Assignment
// Unit test to check the item is in stock

using Microsoft.VisualStudio.TestTools.UnitTesting;
using Moq;
using Module7MethodTest;

namespace Module7MethodTest
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void ItemIsInStockTest(string Item)
        {
            ItemInventory item = new ItemInventory();
            Assert.AreEqual(true,item.stock.Contains("soda"));
        }
        [TestMethod]

        public void inventoryMock()
        {
            ItemInventory i = new ItemInventory() ;
            var mock = new Mock<ItemInventory>();
            mock.SetupGet(m => m.name).Returns("soda");
            mock.SetupGet(m => m.price).Returns(1.50);

            Assert.AreEqual(true, ItemInventory.isItemInStock(i,mock.Object.name));
        }
    }
}
