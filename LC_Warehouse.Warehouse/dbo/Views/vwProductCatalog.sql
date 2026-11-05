CREATE VIEW dbo.vwProductCatalog
AS
SELECT ProductID, ProductName, Category, ListPrice
FROM dbo.DimProduct;

GO