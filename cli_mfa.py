import sys
import os
import boto3
import pipes

client = boto3.client('sts')

if len(sys.argv) > 1:
    mytoken = str(sys.argv[1])
else:
    mytoken = ""

print("echo ")
print("echo Attempting to retrieve MFA keys...")
print("echo '=================================='")
print("echo ")

try:
    response = client.get_session_token(
        SerialNumber='', # username ARN goes here - put in an ini
        TokenCode=mytoken
    )

    print("export AWS_ACCESS_KEY_ID=")
    print("export AWS_SECRET_ACCESS_KEY=")
    print("export AWS_SESSION_TOKEN=")

    print("export AWS_ACCESS_KEY_ID=" + response['Credentials']['AccessKeyId'])
    print("export AWS_SECRET_ACCESS_KEY=" + response['Credentials']['SecretAccessKey'])
    print("export AWS_SESSION_TOKEN=" + response['Credentials']['SessionToken'])


    # print("export AWS_ACCESS_KEY_ID=%s" % (pipes.quote(str(response['Credentials']['AccessKeyId']))) )
    # print("export AWS_SECRET_ACCESS_KEY=%s" % (pipes.quote(str(response['Credentials']['SecretAccessKey']))) )
    # print("export AWS_SESSION_TOKEN=%s" % (pipes.quote(str(response['Credentials']['SessionToken']))))

    print("echo Success:")
    print("echo --------")
    print("echo '> Environment variables set'")
    print("echo '> Expires: '" + str(response['Credentials']['Expiration']))
    print("echo ")
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print("echo Failure:")
    print("echo --------")
    print("echo " + message)
    print("echo ")
    print("echo '> Resetting environment variables'")
    print("echo ")
    print("export AWS_ACCESS_KEY_ID=")
    print("export AWS_SECRET_ACCESS_KEY=")
    print("export AWS_SESSION_TOKEN=")

