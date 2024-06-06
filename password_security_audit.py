'''
Password security checker

Instructions for use:
1. start the program.
2. enter the password you want to check.
3. the program will check if the password meets the security requirements.
4. if the password is incorrect, a report with recommendations will be generated.
5. if the password is secure, a confirmation message will be displayed.
'''


import re

class PasswordSecurityReport:
    def __init__(self, password):
        self.password = password
        self.recommends = [] # recommendations on meeting the requirements of the password

    def check_complexity(self):
        self.recommends.clear()
        
        if len(self.password) < 8:
            self.recommends.append("The password must have a minimum length of 8 characters.")
        
        if not re.search(r'[a-z]', self.password):
            self.recommends.append("The password must contain at least one lowercase letter.")
        
        if not re.search(r'[A-Z]', self.password):
            self.recommends.append("The password must contain at least one uppercase letter.")
        
        if not re.search(r'[\W_]', self.password):
            self.recommends.append("The password must contain at least one special character.")
        
        if re.search(r'\s', self.password):
            self.recommends.append("The password cannot contain spaces.")
        
        return len(self.recommends) == 0

    def generate_report(self):
        if self.check_complexity():
            return "The password meets all safety requirements."
        else:
            report = "Password does not meet the following safety requirements:\n"
            for recommendation in self.recommends:
                report += f"- {recommendation}\n"
            return report

def main():
    print("Welcome to the Password Security Audit")
    password = input("Please enter a password to audit: ")
    
    audit = PasswordSecurityReport(password)
    report = audit.generate_report()
    
    print("\nAudit Report:")
    print(report)

if __name__ == "__main__":
    main()
