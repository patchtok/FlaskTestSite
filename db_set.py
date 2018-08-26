import sqlite3

db_name = "coffee_shop.db"


def load_file(my_path):
    data = []
    file = open(my_path, "r")
    for line in file:
        line = line.strip()
        line = line.rstrip('\n')
        temp =line.split(",")
        # single line
        # data.append((line , ))
        data.append(tuple(temp))
    return data


def query(sql, data, db_name):
    with sqlite3.connect(db_name) as db:
        cursor =db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

def output_query(sql, db_name):
    with sqlite3.connect(db_name) as db:
        cursor =db.cursor()
        cursor.execute(sql)
        output = cursor.fetchall()
        db.commit()
        return output




def create_table(table_name, sql, db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {} already exists, do you wish to delete it ? (y/n)".format(table_name))
            if response == "y":
                keep_table = False
                print("The table {} will be recreated and all existing data will be lost".format(table_name))
                cursor.execute("drop table if it exists {}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            print("The table {} has been created".format(table_name))
            db.commit()


def create_product_table():
    table_name="Product"
    sql = """create table Product
    (ProductID integer,
    Name text,
    Price real,
    ProductTypeID,
    primary key(ProductID),
    foreign key(ProductTypeID) references ProductType(ProductTypeID) )
    """
    create_table(table_name, sql, db_name)


def create_product_type_table():
    table_name = "ProductType"
    sql="""create table ProductType
    (ProductTypeID integer,
    ProductDescription text,
    primary key(ProductTypeID) )
    """
    create_table(table_name, sql, db_name)


def get_table_list(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select * from sqlite_master")
        result = cursor.fetchall()
        for item in result:
            print(item[1])


def insert_product_type_data(records):
    sql = "insert into ProductType (ProductDescription) values (?)"
    for record in records:
        query(sql, record, db_name)
    print("Product type data was entered")


def insert_product_data(records):
    sql = "insert into Product (Name, Price, ProductTypeID) values (?,?,?)"
    for record in records:
        query(sql, record, db_name)
    print("Product data was entered")


def print_table():
    sql = "select * from Product"
    temp = output_query(sql, db_name)
    for item in temp:
        my_string = "{} {} ${:.2f}".format(*item)
        print(my_string)


def find_product():
    name = input("Please enter product name: ")
    sql = "select * from Product where Name like '%{}%'".format(name)
    temp = output_query(sql,db_name)
    if len(temp) == 0:
        print("We could not find your product")
    else:
        for item in temp:
            my_string = " - ".join(map(str, item))
            print(my_string)


def find_exact_product(name):
    sql = "select * from Product where Name='{}'".format(name)
    temp = output_query(sql, db_name)
    if len(temp) == 0:
        print("We could not find your product")
    else:
        for item in temp:
            my_string = " - ".join(map(str, item))
            print(my_string)








def main():
    print_table()
    #find_product()
    find_exact_product("Mocha")
    # records = load_file("extras/coffeedatabase_ProductTypeID.csv")
    # insert_product_type_data(records)
    # records = load_file("extras/coffeedatabase_Product.csv")
    # insert_product_data(records)
    # get_table_list(db_name)
    # create_product_type_table()
    # create_product_table()


if __name__ == "__main__":
    main()
