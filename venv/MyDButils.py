#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     DBUtils
   Description :
   Author :        Mr.Zhang
   date：          2019/7/24 0024
-------------------------------------------------
   Change Activity:
                   2019/7/24 0024:
-------------------------------------------------
"""
__author__ = 'Mr.Zhang'


"""
数据库连接工具类
# """
import pymysql
from config import readConfig
from DBUtils.PooledDB import PooledDB, SharedDBConnection
from DBUtils.PersistentDB import PersistentDB, PersistentDBError, NotSupportedError
# 实例化配置文件
config = readConfig.ReadConfig()



class utils_db(object):
    """
    MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现获取连接对象：conn = utils_db.getConn()
            释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    __pool = None
    def __init__(self, param=None):
        # 数据库构造函数，从连接池中取出连接，并产生游标
        self._conn = utils_db.__getConn()
        self._cursor = self._conn.cursor(cursor=param)
        # cursor = db.cursor(cursor=pymysql.cursors.DictCursor)


    @staticmethod
    def __getConn():
        """
        @summary: 静态方法，从连接池中取出连接
        @return utils_db.connection()
        """
        if utils_db.__pool is None:
            __pool = PooledDB(
                host=config.get_mysql('host'),
                port=int(config.get_mysql('port')),
                user=config.get_mysql('user'),
                passwd=config.get_mysql('passwd'),
                database=config.get_mysql('database'),
                charset=config.get_mysql('charset'),
                # 指定数据库连接驱动
                creator=pymysql,
                # 连接池允许的最大连接数,0和None表示没有限制
                maxconnections=3,
                # 初始化时,连接池至少创建的空闲连接,0表示不创建
                mincached=2,
                # 连接池中空闲的最多连接数,0和None表示没有限制
                maxcached=5,
                # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
                maxshared=3,
                # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
                # False表示不等待然后报错
                blocking=True,
                # 开始会话前执行的命令列表
                setsession=[],
                # ping Mysql服务器检查服务是否可用
                ping=0,
                autocommit='autocommit'
            )
        else:
            __pool = PersistentDB(
                # 指定数据库连接驱动
                creator=pymysql,
                # 一个连接最大复用次数,0或者None表示没有限制,默认为0
                maxusage=1000,
                host=config.get_mysql('host'),
                port=int(config.get_mysql('port')),
                user=config.get_mysql('user'),
                passwd=config.get_mysql('passwd'),
                database=config.get_mysql('database'),
                charset=config.get_mysql('charset'),
                autocommit = 'autocommit'
            )
        return __pool.connection()

    def getAll(self, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def getOne(self, sql, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def getMany(self, sql, num, param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insertOne(self, sql, value):
        """
        @summary: 向数据表插入一条记录
        @param sql:要插入的ＳＱＬ格式
        @param value:要插入的记录数据tuple/list
        @return: insertId 最后一次插入操作生成的id,如果没有则为０
        """
        self._cursor.execute(sql, value)
        return self.__getInsertId()

    def insertMany(self, sql, values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

    def __getInsertId(self):
        """
        获取当前连接最后一次插入操作生成的id,如果没有则为０
        """
        result = self._cursor.lastrowid
        return result

    def __query(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    def update(self, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def delete(self, sql, param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要删除的条件 值 tuple/list
        @return: count 受影响的行数
        """

        return self.__query(sql, param)

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(1)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback');
        self._cursor.close()
        self._conn.close()



if __name__ == '__main__':
    # 测试
    mysql = utils_db(pymysql.cursors.DictCursor)
    # mysql = utils_db()
    # insert一条数据测试
    # value = (12311, 'test', 'test')
    # sql = "INSERT INTO `shazam`.`tb_student` (`stuNo`, `name`, `password`) VALUES (%s, %s, %s)"
    # result = mysql.insertOne(sql, value)
    # select测试
    # sql = 'select * from user where username = "test"'
    # result = mysql.getOne(sql)
    # delete测试
    # values = (4)
    # sql = "DELETE FROM `awesome`.`user` WHERE `iduser` in (%s)"
    # result = mysql.delete(sql, values)
    # update测试
    # sql = "SELECT * FROM shazam.tb_class"
    # result = mysql.getOne(sql)
    # sql = 'select coutseName,result from tb_course,tb_results where tb_course.courseId = tb_results.courseId and tb_results.stuNo=%s'
    # result = mysql.getAll(sql, '201542683')
    value = ['123', '123', '123', '身份证1', '男', '学历', '专业', '2015-9-1', '1995-3-2', '联系电话', '电子邮件', '家庭住址', '1', '123',]
    sql = "UPDATE `shazam`.`tb_student` SET `stuNo`=%s, `name`=%s, `password`=%s, `idCard`=%s, `sex`=%s, `education`=%s, `professional`=%s, `acceptanceDate`=%s, `birthday`=%s, `tel`=%s, `email`=%s, `address`=%s, `classId`=%s WHERE `stuNo`=%s"
    result = mysql.update(sql, value)
    print(result)
