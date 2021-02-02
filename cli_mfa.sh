#!/bin/bash
# $1
evars=$(~/vscode/aws_cli_mfa/.env/bin/python ~/vscode/aws_cli_mfa/cli_mfa.py $1)
eval $evars