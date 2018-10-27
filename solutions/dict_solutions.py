class PythonDict(object):
    def __init__(self, new_value):
        self.new_value = new_value
        self.adict = self.create_new_dict()

    def create_new_dict(self):
        mydict = {}
        # assuming the dict length would be 10
        heroes = ['allu', 'ntr', 'mahesh', 'chiru','bala', 'venky', 'nag',
                'nani', 'rajni', 'kamal']
        movies = [3,4,5,6,7,8,9,1,2,3]
        for i in range(10):
            mydict[heroes[i]] = movies[i]
        return mydict

