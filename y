version = 0.1
[y]
[y.deploy]
[y.deploy.parameters]
stack_name = "lambda-fetch-rds"
s3_bucket = "aws-sam-cli-managed-default-samclisourcebucket-kgunfkf8sxw7"
s3_prefix = "lambda-fetch-rds"
region = "ap-northeast-1"
confirm_changeset = true
capabilities = "CAPABILITY_IAM"
disable_rollback = true
image_repositories = ["HelloWorldFunction=052244742307.dkr.ecr.ap-northeast-1.amazonaws.com/lambdafetchrdsad4edd9d/helloworldfunction19d43fc4repo"]
