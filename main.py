import yagmail
import os

sender= "pintilei92@gmail.com"
receiver= "radoyov923@kahase.com"
subject= "This is the subject!"

contents= " Here is the content of the email! \n Hii!!!"

yag= yagmail.SMTP (user= sender, password= os.environ['PASSWORD'])
yag.send(to= receiver, subject= subject, contents= contents)
print("Email sent!")
                   
