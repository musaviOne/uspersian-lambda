Useful Commands:

    aws configure
        allow you to setup
            'AWS Access Key ID' and 
            'AWS Secret Access Key'
            

To start SAM project:

    sam build
    sam local start-api

Path setting:

    export PATH=/home/david/pear/bin:$PATH:/Users/sayedmusavi/Library/Python/3.7/bin:/usr/local/bin/aws


To Deploy the project:
    
    sam package \
  --template-file template.yaml \         
  --output-template-file package.yaml \
  --s3-bucket lambda-send-email-from-website
  
    sam deploy \
  --template-file package.yaml \
  --stack-name my-sam-application \
  --capabilities CAPABILITY_IAM
