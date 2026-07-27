import boto3
from datetime import datetime

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

VOLUME_ID = "vol-0cad49179c2f6581c"
BUCKET_NAME = "mayank-backup-project-2026"

def lambda_handler(event, context):

    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description=f"Automated Backup {current_time}"
    )

    snapshot_id = snapshot['SnapshotId']

    report = f"""
Backup Successful

Snapshot ID : {snapshot_id}

Volume ID : {VOLUME_ID}

Time : {current_time}
"""

    file_name = f"backup-report-{current_time}.txt"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=report
    )

    return {
        "statusCode": 200,
        "body": {
            "SnapshotId": snapshot_id,
            "ReportFile": file_name
        }
    }
