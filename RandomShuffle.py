class _IntegerList(list):
    def __init__(self,*args, **kwargs):
        self.List = list(*args, **kwargs)

#RandomShuffle_ByRefference(4)
class _List(list):
    import random

    def __init__(self,*args, **kwargs):
        self.List = list(*args, **kwargs)
        if (type(self.List[0])== int):

    def Shuffle(self):
        return 0
    def GetShuffled(self):
        Reference_List  = [x for x in range(len(self.List))]
        RandomList = []

        List_Length = len(List)
        for X in range(List_Length-1,-1,-1):
            Index      = random.randint(0,X)
            List_Index = Reference_List.pop(Index)
            RandomList.append(List[List_Index])
        return RandomList
    def GetShuffledRefference(self,List_Length):
        Reference_List  = [x for x in range(List_Length)]
        RandomReference = []

        for X in range(List_Length-1,-1,-1):
            Index = random.randint(0,X)
            Value = Reference_List.pop(Index)
            RandomReference.append(Value)
        return RandomReference

    #Returns 0 if Value not in List.
    def Quantity(self,Value):
        Left  = self.BinarySearch(Value)
        Right = self.BinarySearch(Value)
        if (Left == -1):
            return 0
        if (Left == Right):
            return 1
        return Left - Right
    def BinarySearch(self,SearchValue):
        return self._RecursiveBinarySearch(self,SearchValue,0,len(self.List),0)
    #Returns -1 if Value not in List.
    def _RecursiveBinarySearch(self,SearchValue,Left,Right,SearchType="Right"):
        if(len(self.List) == 0 || Left > Right):
            return -1
        if(Left == Right):
            return Left

        Pivot = Left + (Right-Left)/2
        if (self.List[Pivot] == SearchValue):
            if (SearchType = "Right"):
                if(self.List[Pivot] >= SearchValue):
                    return self._RecursiveBinarySearch(self,SearchValue,0,Pivot,SearchType)
                else:
                    return self._RecursiveBinarySearch(self,SearchValue,Pivot,Right,SearchType)

            else if(SearchType = "Left"):
                if(self.List[Pivot] > SearchValue):
                    return self._RecursiveBinarySearch(self,SearchValue,0,Pivot,SearchType)
                else:
                    return self._RecursiveBinarySearch(self,SearchValue,Pivot,Right,SearchType)
        else:
            if(self.List[Pivot] >= SearchValue):
                return self._RecursiveBinarySearch(self,SearchValue,0,Pivot,SearchType)
            else:
                return self._RecursiveBinarySearch(self,SearchValue,Pivot,Right,SearchType)
    def _RightBinarySearch(self,SearchValue,Left,Right,SearchType):
        return 0
    def _LeftBinarySearch(self,SearchValue,Left,Right,SearchType):
        return 0
        #self.List

class _Test_List():
    def __init__(self):
        import random
        self.Test_RandomShuffle(100)
        self.Test_RandomShuffle(100)
    def Print_Results(self):
        print("_List Tests:")
        return 0
    def Test_RandomShuffle(Length):
        TestList = _List([1,2,3])
        #Shuffled_Reference = RandomShuffle_ByRefference(10)
        return 0
    def Test_RandomShuffle(Length):
        SortedList = [x+1 for x in range(Length)]

        UnsortedList = RandomShuffle(SortedList)
        print(SortedList)
        print(UnsortedList)

Test_List = _Test_List()
Test_List.Print_Results()
