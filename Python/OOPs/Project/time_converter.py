class time:
    def sec_min(self,sec):
        self.sec = sec
        print(f"Time : {self.sec//60}min and {self.sec%60}sec")
    
    def hour_min(self,hour):
        self.hour = hour
        print(f"Time hour to min : {self.hour*60}")
    
    def min_hour(self,min):
        self.min = min
        print(f"Time min to hour : {self.min//60}hrs and {self.min%60}min")
    
    def hour_sec(self,hour):
        self.hour = hour
        print(f"Time hour to sec : {self.hour*60*60}")    
    # def sec_hour(self,sec):
    #     self.sec = sec
    #     print(f"Time sec to hour : {self.sec//3600}:{(self.sec%3600)//60}:{self.sec%60}")
        
    
        
    # def min_sec(self,min):
    #     self.min = min
    #     print(f"Time min to sec : {self.min * 60}sec")
        
    
    
sec = eval(input("Enter time in seconds : "))
min = eval(input("Enter time in minutes : "))
hour = eval(input("Enter time in hour : "))

s = time()
m = time()
h = time()

# s.sec_hour(sec)
s.sec_min(sec)
# m.sec_hour(min)
m.sec_min(min)
h.hour_min(hour)
# h.hour_sec(hour)