class voter:
    def welcome(self):
        '''Whenever the user will log in for voting purpose,male/female/transgender will find this '''
        ''''''
        print("Your contribution to this democracy matters !:")
        '''Since we dont have database,we have created a short one here for demo purpose'''
        print("choose among ELE45786,ELE45693,ELE45201,ELE45101,ELE45999,ELE45789,ELE46790")
        self.id =input("Please enter your ID: ")
        self.id=self.id.upper()
        return self.id

    def otp(self):
        '''OTP sent is needed to be filled for verification purpose'''
        self.OTP_vrfctn=int(input("Please enter your OTP: "))
        return self.OTP_vrfctn

    def vote(self):
        '''Here Voters will cast their votes'''
        print("Choose your fortune")
        print("Choose between :")
        print("L",":","liberal")
        print('C',':','conservative')
        print('X',':','communist')
        print('S'':','socialist')
        self.choice=input("Please enter the character as recommended above:")
        self.choice=self.choice.upper()
        return self.choice

    def email_public(self):
        self.email_public=input("Voter email: ")
        return self.email_public







