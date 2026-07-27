# AWS Backup & Disaster Recovery Automation

## Overview

AWS Backup & Disaster Recovery Automation is a serverless cloud project that automatically creates EBS snapshots, uploads backup reports to Amazon S3, and monitors the backup process using Amazon CloudWatch. In case of backup failures, Amazon SNS sends email notifications to the administrator.

This project demonstrates how AWS services can be integrated to build an automated and reliable backup solution with minimal manual intervention.

---

## Project Architecture

![Architecture](architecture/architecture.png)

---

## Features

- Automated EBS Snapshot Creation
- Automated Backup Report Generation
- Backup Report Storage in Amazon S3
- EventBridge Scheduled Execution
- AWS Lambda (Python) Automation
- CloudWatch Monitoring
- CloudWatch Alarm for Backup Failures
- Amazon SNS Email Notifications
- Fully Serverless Automation

---

## AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon EC2 | Host application and EBS volume |
| Amazon EBS | Store application data |
| AWS Lambda | Execute backup automation |
| Amazon S3 | Store backup reports |
| Amazon EventBridge | Schedule Lambda execution |
| Amazon CloudWatch | Logging and monitoring |
| Amazon SNS | Email notifications |
| IAM | Secure permissions |

---

## Project Workflow

1. EventBridge triggers Lambda every 5 minutes.
2. Lambda creates an EBS snapshot.
3. Lambda generates a backup report.
4. The report is uploaded to Amazon S3.
5. CloudWatch stores execution logs.
6. CloudWatch Alarm monitors Lambda failures.
7. Amazon SNS sends an email if a failure occurs.

---

## Folder Structure

```text
aws-backup-disaster-recovery-automation
│
├── lambda/
├── screenshots/
├── architecture/
├── docs/
├── README.md
├── LICENSE
└── .gitignore
```

---

## Screenshots

### EC2 Instance

![EC2](screenshots/ec2.png)

---

### Lambda Function

![Lambda](screenshots/lambda.png)

---

### EventBridge Scheduler

![EventBridge](screenshots/eventbridge.png)

---

### Amazon S3

![S3](screenshots/s3.png)

---

### EBS Snapshot

![Snapshot](screenshots/snapshot.png)

---

### CloudWatch Alarm

![CloudWatch](cloudwatch.png)

---

### SNS

![Snapshot](screenshots/sns.png)

---

## Technologies Used

- Python
- AWS Lambda
- Amazon EC2
- Amazon EBS
- Amazon S3
- Amazon EventBridge
- Amazon CloudWatch
- Amazon SNS
- IAM

---

## Future Enhancements

- Automatic EC2 Recovery
- Lifecycle Policies for Snapshots
- Cross-Region Backup Replication
- Backup Encryption using AWS KMS
- AWS Backup Service Integration
- Dashboard using Amazon QuickSight

---

## Author

**Mayank Yadav**

Third Year B.Tech (Electronics and Telecommunication Engineering)

Symbiosis Institute of Technology, Pune

GitHub:
https://github.com/Mayankyadav-018

---

## License

This project is licensed under the MIT License.