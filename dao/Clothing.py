from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Clothing Attributes: AgeCategory, Size

# getAll: gets all clothing tuples

# getByResourceID: gets tuple with the specified ResourceID

# getAllByAgeCategory/Size/Cost: Obtains all the clothing items, ordered by the attribute given

# getByUserID: gives tuple ordered by specific user

# getByUserIDAndAgeCategory: gives the tuples ordered by the user and with the specified ageCategory

# insert: adds a new tuple

class ClothingDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothing(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,agecategory,size from  clothing natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true order by agecategory;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getClothingByresourceID(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,agecategory,size,googlemapurl  from  clothing natural inner join resources natural inner join supplies natural inner join location  natural inner join purchase_type natural inner join resource_type  where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllClothingByAgeCategory(self, age):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,agecategory,size from  clothing natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and agecategory = %s order by size;"
        cursor.execute(query, (age,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingBySize(self, size):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,agecategory,size from  clothing natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and size = %s order by agecategory;"
        cursor.execute(query, (size,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,agecategory,size from  clothing natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and cost <= %s order by agecategory;"
        cursor.execute(query, [cost])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,agecategory,size from  clothing natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s order by agecategory;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingByUserIDAndAgeCategory(self, uid, age):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,agecategory,size from  clothing natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s and agecategory = %s order by size;"
        cursor.execute(query, ([uid], age,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insert(self, resourceid, agecategory, size):
        cursor = self.conn.cursor()
        query = "insert into clothing(resourceid,agecategory,size) values(%s,%s,%s) returning clothingid;"
        cursor.execute(query, (resourceid, agecategory,size))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result
