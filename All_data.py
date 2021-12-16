class All_data:
    all_data={}
    All_data_STRING=""

    def __init__(self):
        pass

    def add(self,s):
        self.All_data_STRING = self.All_data_STRING + s

    def check_infut(self,check):
        list_check = check.split(" ")
        for x in list_check:
            if(self.All_data_STRING.find(x) == -1):
                return  print("Does not exist")
        print("Does is exist")

    def getAll(self):
        return self.All_data_STRING

    '''
    def add(self,all_data_list,nuberJson):
        indexY=0;
        for x in range(0,len(all_data_list)):
            temp = all_data_list[x].split(" ")
            for y in range(0,len(all_data_list)):
            if all_data_list[x] in self.all_data:
                temp=self.all_data[all_data_list[x]]
                if temp in nuberJson:
                    temp[nuberJson].add(x)
                else:
                    self.all_data_list[x].update({nuberJson:{nuberJson: set([x])}})
            else:
                self.all_data.update({all_data_list[x]:{nuberJson : set([x])}})


    def check_infut(self,check):
        if(self.All_data_STRING.find(check) == 0):
            return -1
        else:
            return self.All_data_STRING.find(check)

        temp = check.split(" ")
        for word in temp:
            fend_word = self.fend_word(word)
            Location_Json = fend_word.
        return to_stg
        
    def fend_word(self,word):
        return 0
        '''
