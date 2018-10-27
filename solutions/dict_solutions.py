class PythonDict(object):
    def __init__(self, new_value):
        # so when you initialize this class make sure you pass a value in 
        # class brackets
        """these both are this class instance variables"""
        self.new_value = new_value 
        # this below variable is another class variable which is not passed
        # instead it is created by another class instnace function 
        self.adict = self.create_new_dict()
        # note that the above two variables can be accessed from anywhere 
        # inside class

    def create_new_dict(self):
        mydict = {}
        # assuming the dict length would be 10
        heroes = ['allu', 'ntr', 'mahesh', 'chiru','bala', 'venky', 'nag',
                'nani', 'rajni', 'kamal']
        movies = [3,4,5,6,7,8,9,1,2,3]
        for i in range(10):
            mydict[heroes[i]] = movies[i]
        return mydict

if __name__=="__main__":
    obj = PythonDict(20) # if you do not pass one value to the class 
    # intalization it will throw an argument error
    # print the class variables
    print(obj.new_value) # these are variables not functions, so do not use 
    # obj.new_value() is wrong
    print(obj.adict)
