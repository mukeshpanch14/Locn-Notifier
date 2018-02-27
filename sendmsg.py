from twilio.rest import Client

account_sid = "AC771e278df6a3ab92af76aaceab0855f1"
auth_token = "8968237e4ba957f9ef3d7819f6073afe"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+14249992305",
    from_="+12062036452",
    body="1st Python Message")