from io import StringIO
import os
import pymysql
import json
import boto3
import datetime
import csv
import pandas as pd

# import requests

#config file containing credential for RDS
host = "ao-dai-gia-bach.crke4zwh11p2.ap-northeast-1.rds.amazonaws.com"
username = "root"
password = "Nguoibuongio3k"
db = "ao_dai_gia_bach"

connection = pymysql.connect(host=host, user=username, passwd=password,db=db)
s3 = boto3.client('s3')

#def lambda_handler(event,context):
def lambda_handler():
    try:
        tableName = "customer"
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM {}'.format(tableName))
        rows = cursor.fetchall()
        
        bucket = "ao-dai-gia-bach"
        todayString = datetime.datetime.now().strftime("%Y/%m/%d/")
        csvFileName = tableName + ".csv"
        fileObject = todayString + csvFileName

        #handle csvfile local

        #csvFile = open(csvFileName, mode='w+', newline='',encoding='utf-8')
        #fileWriter = csv.writer(csvFile)
        #fileWriter.writerows(rows)
        #csvFile.close()

        #load data to dataFrame
        df = pd.DataFrame.from_records(rows)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False, header=None)
        s3.put_object(Body=csv_buffer.getvalue(),Bucket=bucket,Key=fileObject)
        print(csv_buffer.getvalue)


        # with open(csvFileName, mode='r', encoding='utf-8') as file:
        #     s3.upload_file(csvFileName,bucket, fileObject)


        print('put seccessfully!')
    except Exception as exception:
        raise exception
    finally:
        connection.close

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": str(df)
        })
    }
lambda_handler()