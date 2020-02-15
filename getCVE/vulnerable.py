class vulnerable: 
    def __init__(self, cve_id, cve_type, cve_publish_date, cve_score, cve_access, cve_description):
        self.cve_id = cve_id 
        self.cve_type = cve_type
        self.cve_publish_date = cve_publish_date
        self.cve_score = cve_score 
        self.cve_access = cve_access 
        self.cve_description = cve_description 
    
    def get_info(self) :   
        print("[*] " + self.cve_id) 
        print("\t[*] Type : " + self.cve_type) 
        print("\t[*] Published Date : " + self.cve_publish_date) 
        print("\t[*] Score : " + self.cve_score) 
        print("\t[*] Access : " + self.cve_access) 
        print("\t[*] Description : " + self.cve_description )