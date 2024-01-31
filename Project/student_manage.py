class student:
    def display_details(self,info):
        self.info = info
        print('*'*105)
        print("\t\t\t\t\tSTUDENTS DETAIL")
        print('*'*105)
        print(f"{'Sr.no.':<15}{'Name':<15}{'Roll no.':<15}{'Course':<15}{'Branch':<15}{'Year':<15}{'CPI'}")

        for i,j in self.info.items():
            print(f"{i:<15}{j['Name']:<15}{j['Roll no.']:<15}{j['Course']:<15}{j['Branch']:<15}{j['Year']:<15}{j['CPI']}")
        print('*'*105)
            
    
    
std = student()    
 
details = {
    1:{"Name":"Ravi","Roll no.":12,"Course":"B-Tech","Branch":"Electrical","Year":2023,"CPI":8},
    2:{"Name":"Saket","Roll no.":32,"Course":"Diploma","Branch":"CSE","Year":2023,"CPI":7.4},
    3:{"Name":"Neha","Roll no.":21,"Course":"B-Tech","Branch":"mechanical","Year":2023,"CPI":6}
    
    }
std.display_details(details)