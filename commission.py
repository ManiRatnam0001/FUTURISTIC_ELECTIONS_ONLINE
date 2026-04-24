import hashlib
import threading
import logging
import yagmail
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from public import voter

class cmsn:
    _inst=None
    _lock=threading.Lock()
    v=voter()
    communist = 0
    liberal = 0
    conservative = 0
    socialist = 0
    def __new__(cls):
        '''Why do we need a singleton here?'''
        '''....because you cast a vote into a specific ballot among many ballots which can be considered as one'''
        if cls._inst==None:
            with cls._lock:
                if cls._inst==None:
                    cls._inst=super().__new__(cls)
        return cls._inst
    def __init__(self):
        '''Memo to be handed to authorised officials.'''
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.file_handler = logging.FileHandler('elections.log')
        self.logger.addHandler(self.file_handler)
        self.formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        self.file_handler.setFormatter(self.formatter)
        self.file_handler.setLevel(logging.INFO)
        self.Lister=dict()

    def voter_list(self):
        '''We do not have a database so we are considering to take some fake names for the demo'''
        '''They are going to be as small as number 5'''
        self.Lister.update({"ELE45786": {"id": "ELE45786", "Elector's_name": "Vinod", "DOB": 1995, "voted": 0, "party": None}})
        self.Lister.update({"ELE45693": {"id": "ELE45693", "Elector's_name": "Mani", "DOB": 1995, "voted": 0, "party": None}})
        self.Lister.update({"ELE45201": {"id": "ELE45201", "Elector's_name": "Ratnam", "DOB": 1995, "voted": 0, "party": None}})
        self.Lister.update({"ELE45101": {"id": "ELE45101", "Elector's_name": "John", "DOB": 1995, "voted": 0, "party": None}})
        self.Lister.update({"ELE45999":{"id": "ELE45999", "Elector's_name": "Alaadin", "DOB": 1995, "voted": 0, "party": None}})
        self.Lister.update({"ELE45789": {"id": "ELE45789", "Elector's_name": "Ram Ratna", "DOB": 1995, "voted": 0, "party": None}})
        self.Lister.update({"ELE46790": {"id": "ELE46790", "Elector's_name": "Teelu", "DOB": 1995, "voted": 0, "party": None}})
        self.logger.info(self.Lister)
        return self.Lister

    def Online_voter_vrfctn(self):
        '''For mail-in_ballots ,transparency and online security through person identification is needed the most'''
        '''At this demo ,lets take OTP'''
        self.OTP=np.random.randint(1,1000000)
        self.logger.info(self.OTP)
        return self.OTP

    def receipt(self):
        '''After voting concludes ,you will get a receipt by which you can re-verify your actions'''
        filename="voter_receipt.pdf"
        self.c =canvas.Canvas(filename,pagesize=A4)
        self.pagesize=(80*mm,150*mm)
        self.y=140
        self.c.setFont("Helvetica-Bold",10)
        self.c.drawCentredString(40 * mm, self.y, "ELECTION COMMISSION OF FALANA")
        self.y -= 10
        self.c.setFont("Helvetica",8)
        self.c.drawCentredString(40 * mm, self.y, "Receipt number:"+str(self.blkchn()))
        self.y -= 15
        self.c.drawString(5,self.y,"-"*30)
        self.y -= 40
        self.c.drawString(5,self.y,"-"*30)
        self.y -=20
        self.c.drawCentredString(40*mm,self.y,"Thank you for voting,Ehssan kar gaye!!")
        self.c.save()
        return filename

    def blkchn(self):
        for self.char in self.Lister:
            if self.Lister[self.char]['voted'] ==1:
                self.Lister[self.Vote]['party'] != None
                self.enc_dt = self.char
        self.enc_dt=self.enc_dt.encode('utf-8')
        self.sha_256=hashlib.sha256()
        self.sha_256.update(self.enc_dt)
        return self.sha_256.hexdigest()

    def intrnl_vfctn(self):
        self.Vote = self.v.welcome()
        self.voting=self.v.vote()
        try:
            self.Lister[self.Vote]['voted'] = 1
            self.Lister[self.Vote]['party']=self.voting
            self.logger.info(self.Lister)
            if self.voting == "X":
                self.conservative +=1
            elif self.voting == "C":
                self.communist +=1
            elif self.voting == "L":
                self.liberal +=1
            elif self.voting == "S":
                self.socialist +=1
            else:
                print("You chose the wrong input")
                self.voting()
        except KeyError as error:
            print("Voter-id not found.Try Again or contact Falana")
            self.intrnl_vfctn()
    def classic(cls):
        return f"The stats so far ....liberal : {cls.liberal},conservative : {cls.conservative},socialist : {cls.socialist},communist:{cls.communist}"
    def commission_mail(self):
        self.from_email=""
        return self.from_email
    def main(self):
        self.yag=yagmail.SMTP(self.commission_mail(),"")  #Enter app password in string literals
        self.receiver=self.v.email_public()
        self.logger.info(self.receiver)
        self.subj="OTP"
        self.body=str(self.Online_voter_vrfctn())
        self.yag.send(to=self.receiver,subject=self.subj,contents=self.body)
        self.veri=str(self.v.otp())
        if self.body==self.veri:
            self.voter_list()
            self.intrnl_vfctn()
            self.blkchn()
            self.subj = "receipt"
            self.body = self.receipt()
            self.yag.send(to=self.receiver, subject=self.subj, contents="Here is your receipt",attachments=self.body)
            print(self.classic())
        else:
            print("Not a OTP")


b=cmsn()
b.main()















