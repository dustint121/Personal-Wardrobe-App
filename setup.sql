CREATE TABLE Clothing_Pieces(
    ID int IDENTITY(0,1),
    Short_Descriptor varchar(255),
    Brand varchar(255),
    Category varchar(255),
    Image_Data image,
    PRIMARY KEY (ID)
);


CREATE TABLE Fabrics(
    ID int IDENTITY(1,1),
    Name varchar(255),
    Description text,
    PRIMARY KEY (ID)
);


CREATE TABLE Fabrics_of_Clothes(
    ClothingID int,
    FabricID int,
    Percentage int,
    PRIMARY KEY (ClothingID, FabricID),
    FOREIGN Key (ClothingID) REFERENCES Clothing_Pieces(ID) ON DELETE CASCADE,
    FOREIGN Key (FabricID) REFERENCES Fabrics(ID) ON DELETE CASCADE
);