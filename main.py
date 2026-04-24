'''We gonna imagine that there are two computer's here'''
'''One belons to commission,other belongs to voter'''
import yagmail
from commission import cmsn
from public import voter
'''commission logs in'''
c=cmsn()
'''Voter logs in '''
v=voter()
def main():
    yag = yagmail.SMTP(c.commission_mail(),c.password())
    receiver = v.email_public()
    subj = "OTP"
    body = c.online_voter_vrfctn()
    yag.send(to=receiver, subject=subj, contents=body)
main()




