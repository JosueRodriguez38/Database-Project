from config.dbconfig import pg_config
import psycopg2

# This class handles requests made by users of goods that arent available at the moment

class RequestDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def insertrequest(self, userid):
        cursor = self.conn.cursor()
        query = "insert into request(userid, status) values(%s,true) returning requestid "
        cursor.execute(query, (userid,))
        result = cursor.fetchall()
        self.conn.commit()
        return result

    def getallrequest(self):
        cursor = self.conn.cursor()
        query = "select requestid,userid,firstname,lastname,status from request natural inner join users order by status "
        cursor.execute(query)
        result = cursor.fetchall()
        self.conn.commit()
        return result

    # returns requests made by user id
    def getUserRequest(self,userid):
        cursor = self.conn.cursor()
        query = "select requestid,userid,firstname,lastname,status from request natural inner join users where userid = %s order by status "
        cursor.execute(query,[userid])
        result = cursor.fetchall()
        self.conn.commit()
        return result

    # returns all resources in a request by given request id
    def getAllResourcesbyRequestID(self, requestid):
        cursor = self.conn.cursor()
        query = "select requestid,resourceid,name,resourcetypename,ammountselected,cost, purchasetypename,googlemapurl from selected natural inner join resources natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type where requestid = %s "
        cursor.execute(query, [requestid])
        result = cursor.fetchall()
        self.conn.commit()
        return result

    # returns all resources in a request by given resource name
    def getAllResourcesbyResourceName(self, name):
        cursor = self.conn.cursor()
        query = "select requestid,resourceid,name,resourcetypename,ammountselected,cost, purchasetypenumber,googlemapurl from selected natural inner join resources natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type where name = %s "
        cursor.execute(query, [name])
        result = cursor.fetchall()
        self.conn.commit()
        return result

    def get_request_by_requestid(self, requestid):
        cursor = self.conn.cursor()
        query = "select requestid, userid ,firstname, lastname,request.status from request natural inner join users where requestid = %s "
        cursor.execute(query, [requestid])
        result = cursor.fetchone()
        self.conn.commit()
        return result