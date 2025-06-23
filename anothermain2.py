from threading import Thread
class returningThread(Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs={}):
        Thread.__init__(self,group,target,name,args,kwargs)
        self._returnit=None
    def run(self):
        if self._target is not None:
            self._returnit=self._target(*self._args,**self._kwargs)
    def join(self, timeout = None):
        Thread.join(self)
        return self._returnit
class A:
  def bro(self,a,b):
    print("xyz")
    pass
def main():
    dk=[]
    t1=returningThread(target=A.bro,args=(None,"Hello","World"))
    t1.start()
    a=t1.join()
    print(a)
main()