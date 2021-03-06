from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# CannedFood Attributes: (CannedFoodID, ResourceID, Primary ingredient, ounces, Expiration Date)

# getAllCannedFood: extracts the canned food attributes plus
# the resource id and typename of every tuple in the canned food table

# getCannedFoodByResourceID: obtains the attributes of a specific tuple as specified by a resource id

# getAllCannedFoodByFlavor/UserID/Cost/Primary ingredient: These methods obtain the canned Food tuples
# that have the specified attribute

# insert: inserts a new canned food tuple with the information specified
class CannedFoodDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insert(self ,resourceid, primaryingredient, ounces, expirationdate):
        cursor = self.conn.cursor()
        query = "INSERT INTO canned_food(resourceid, primaryingredient, ounces, expirationdate) values(%s,%s,%s,%s) returning cannedfoodid"
        cursor.execute(query,(resourceid, primaryingredient, ounces, expirationdate))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFood(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename , primaryingredient , ounces, expirationdate from canned_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true order by primaryingridient;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getCannedFoodByResourceID(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename , primaryingredient , ounces, expirationdate,googlemapurl  from canned_food natural inner join resources natural inner join supplies natural inner join location  natural inner join purchase_type natural inner join resource_type  where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllCannedFoodByFlavor(self, flavor):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename , primaryingredient , ounces, expirationdate from canned_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and primaryingridient = %s order by expirationdate;"
        cursor.execute(query, (flavor,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFoodByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename , primaryingredient , ounces, expirationdate from canned_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s order by primaryingridient;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFoodByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename , primaryingredient , ounces, expirationdate from canned_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and cost <= %s order by primaryingridient;"
        cursor.execute(query, [cost])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFoodByUserIDAndPrimaryIngredient(self, uid, ingredient):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename , primaryingredient , ounces, expirationdate from canned_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s and primaryingridient = %s;"
        cursor.execute(query, (uid, ingredient,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result
