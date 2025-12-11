class Mark():
   def __init__(self, sid, cid, mark):
        self.sid = sid
        self.cid = cid
        self.mark = mark

   def __str__(self):
       return f"{self.sid} | {self.cid} | {self.mark}"