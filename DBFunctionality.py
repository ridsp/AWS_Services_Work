import boto3
import os


os.environ["AWS_ACCESS_KEY_ID"] = "AKIA6ENWLUGEQRDQKSEU"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"

os.environ["AWS_DEFAULT_REGION"] = "us-east-2"


__Table__ = "Employee"
client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
table = db.Table(__Table__)

##Read the Data
response = table.get_item(
            Key={
               "EmpId":"Emp1"
          }
        )

print(response["Item"])

##Write the Data
response = table.put_item(
    Item = { "EmpId":"Emp3",
            "EmpName": "Ruchika",
            "Dept": "QA",
            "Salary":int(30000)
        }
)
response["ResponseMetadata"]["HTTPStatusCode"]

##Delete Item
response = table.delete_item( Key={ "EmpId": "Emp1" } )

print(response)

