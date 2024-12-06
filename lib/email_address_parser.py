# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        potential_emails = re.split(r'[,\s]+', self.email_addresses.strip())
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        valid_emails = [email for email in potential_emails if email_pattern.match(email)]
        return sorted(valid_emails)

