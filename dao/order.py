from config.dbconfig import pg_config
from config.tuple_config import order,user_cons
import psycopg2

# The purpose of the order DAO is to extract the information of an order that has been requested

class OrderDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # returns all the orders, the items and amounts bought, via a natural join from
    # the tables Resources, Consumer, and User, and the relationship Belongs

    def getAllOrders(self):
       # cursor = self.conn.cursor()
       # query = "select oid, rname, firstname, ammountbought, ammountsreserved, date from order natural join belongs natural join resources natural join consumer natural join user;"
       # cursor.execute(query)
        result = []
        r = []
        for row in order:
            r.append(row)
        result.append(r)
        return result

    #   not used in phase 1
    #def getConsumerIdByName(self, firstname, lastname):
        # cursor = self.conn.cursor()
        # query = "select cid from consumer where firstname = %s and lastname = %s;"
        # cursor.execute(query, (firstName, lastName))
        #result = cursor.fetchone()
        #return result

    # Returns an order if its id matched the input

    def getOrderById(self, oid):

        if oid == order[0]:
            return order
        else:
            return

    # Returns the orders that have the resource specified by the input
    def getOrderByResourceName(self, rname):

        result = []
        if rname['name'] == 'water':
            for row in order:
                result.append(row)
        return result

    # inserts an order, linked to a consumer's id

    def insert(self, cid,rname, ammountReserved, ammountBought, date):
        if cid == user_cons[0]:
            print("HEREEEEEEEEEEEEEE")
            return 2
        else:
            return

    # updates a consumer's order

    def update(self, oid, cid,rname,  ammountReserved, ammountBought, date):
        if oid == order[0] and cid == order[1]:
            return oid
        else:
            return

    # deletes an order identified by an input order id
    def delete(self, oid):
        if oid == order[0]:
            return oid
        else:
            return