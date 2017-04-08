# encoding=utf-8
import MySQLdb
from settings import MYSQL_HOST,MYSQL_DBNAME,MYSQL_USER,MYSQL_PASSWD
from items import InformationItem, TweetsItem
class DBPipleline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=MYSQL_USER, passwd=MYSQL_PASSWD, db=MYSQL_DBNAME, host=MYSQL_HOST, charset="utf8",use_unicode=True)
        self.cursor = self.conn.cursor()
        # # 清空表：
        # self.cursor.execute("truncate table material;")
        # self.conn.commit()


    def process_item(self, item, spider):

        if isinstance(item, InformationItem):
            try:
                self.cursor.execute("""INSERT INTO information2 ( id,tweets_num, follows_num, fans_num)
            							VALUES (%s, %s, %s, %s)""",
                                    (
                                        item['_id'],
                                        item['tweets_num'],
                                        item['follows_num'],
                                        item['fans_num'],

                                    )
                                    )
                self.conn.commit()
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
        elif isinstance(item, TweetsItem):
            try:
                self.cursor.execute("""INSERT INTO tweets2 (userid, content, like_num, comment, transfer)
            							VALUES (%s, %s,%s,%s, %s)""",
                                    (
                                        item['ID'],
                                        item['Content'],
                                        item['Like'],
                                        item['Comment'],
                                        item['Transfer'],
                                    )
                                    )
                self.conn.commit()
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])

        return item

