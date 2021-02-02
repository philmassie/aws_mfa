# Python environment
```
python3 -m venv /Users/phil/vscode/aws_cli_mfa/.env
source /Users/phil/vscode/aws_cli_mfa/.env/bin/activate
pip install -r requirements.txt
ln -s ~/vscode/aws_cli_mfa/cli_mfa.sh ~/bin/awsmfa 
```


https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/
- write a little python script to do this
userarn=???
token=???
aws sts get-session-token --serial-number ${userarn} --token-code ${token}


unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN