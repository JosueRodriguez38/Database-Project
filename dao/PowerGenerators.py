from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Power Generators Attributes: generatorFuel, capacity, size

class PowerGeneratorDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerGenerators(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,generatorfuel,capacity,size from  power_generator natural inner join resources natural inner join purchase_type natural inner join resource_type  ;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getPowerGeneratorByResourceID(self,resourceID):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,generatorfuel,capacity,size,googlemapurl  from  power_generator natural inner join resources natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where resourceid=%s;"
        cursor.execute(query,[resourceID])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getPowerGeneratorByGeneratorFuel(self,generatorfuel):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,generatorfuel,capacity,size from  power_generator natural inner join resources natural inner join purchase_type natural inner join resource_type  where generatorfuel ~* %s order by generatorfuel;"
        cursor.execute(query,(generatorfuel))
        result = cursor.fetchone()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insert(self, resourceid, generatorfuel, capacity, size):
        cursor = self.conn.cursor()
        query = "insert into power_generator(resourceid,generatorfuel,capacity,size) values(%s,%s,%s,%s) returning powergeneratorid;"
        cursor.execute(query, (resourceid, generatorfuel, capacity, size))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

