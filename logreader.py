


try:
    import boto3
    import os
    import sys
    import pandas as pd
    import csv
    print("All Modules are Loaded ......")
except Exception as e:
    print("Some Modules are missings {}".format(e))


class CloudWatch(object):
    def __init__(self):
        self.client = boto3.client('logs')
        self.timestamp = []
        self.message=[]

    def get_logs(self, logGroupName='/aws/lambda/RealEstStatic',logStreamName="2023/03/12/[$LATEST]cdab9f1c6db74da5b1385bb5ddbef8ef" ):
        """

        :param logGroupName: Takes String
        :param logStreamName: Takes String
        :return: Pandas Dataframe
        """
        response = self.client.get_log_events(
            logGroupName=logGroupName,
            logStreamName=logStreamName)
        for x in response.get("events"):
            self.timestamp.append(x.get("timestamp", None))
            self.message.append(x.get("message", None))

        df = pd.DataFrame({
            "TimeStamp":self.timestamp,
            "Message":self.message
        })
        return df

    def save_csv(self):
        df = self.get_logs()
        df.to_csv("Report.csv")
        print("Saved CSV FIle on your COmputer ")

    def save_json(self):
        df = self.get_logs()
        df.to_json("Report.json")
        print("Saved JSON File on your Computer ")

    def save_html(self):
        df = self.get_logs()
        df.to_html("Report.html")
        print("Saved HTML File on your Computer ")


if __name__ == "__main__":
    obj = CloudWatch()
    df1 = obj.get_logs(logGroupName='/aws/lambda/RealEstStatic',logStreamName='2023/03/12/[$LATEST]cdab9f1c6db74da5b1385bb5ddbef8ef')
    print(df1)
    print(obj.save_csv())
    obj.save_json()
    obj.save_html()











