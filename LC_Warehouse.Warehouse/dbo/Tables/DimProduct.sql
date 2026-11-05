CREATE TABLE [dbo].[DimProduct] (
    [ProductID]   INT             NOT NULL,
    [ProductName] VARCHAR (100)   NOT NULL,
    [Category]    VARCHAR (50)    NULL,
    [ListPrice]   DECIMAL (10, 2) NULL
);


GO