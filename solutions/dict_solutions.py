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
            # unfortunately this is the only you can build the dictionary map
            mydict[heroes[i]] = movies[i]
        return mydict

    def iterate_and_print_using_keys(self):

        pass

    def get_key(self, movie_count):
        """Note that multiple keys can have same value. If you find mutiple 
        keys with same value then return list of all matching keys
        Example: If I pass movie_count as 3, it should return a list [
        'allu','kamal'] . If I pass value as 7, it should return only a 
        string 'bala'. Ideally, a function should return same type. It is 
        bad programming to return different types in different cases. As 
        this for learning purposes, we can ignore"""
        pass

    def get_value(self):
        pass
    

if __name__=="__main__":
    obj = PythonDict(20) # if you do not pass one value to the class
    # intalization it will throw an argument error
    # print the class variables
    print(obj.new_value) # these are variables not functions, so do not use
    # obj.new_value() is wrong
    print(obj.adict)
