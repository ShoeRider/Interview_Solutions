def MergeSort_ByValue(UnsortedList):
    if(len(UnsortedList)==0):
        return []
    if(len(UnsortedList)<=1):
        return UnsortedList
    Pivot = int(len(UnsortedList)/2)
    List0 = UnsortedList[0:Pivot]
    List1 = UnsortedList[Pivot+1:]

    PrePivot = []
    PostPivot = []
    for List in [List0,List1]:
        for Integer in List:
            if(Integer <= UnsortedList[Pivot]):
                PrePivot.append(Integer)
            else:
                PostPivot.append(Integer)

    SortedList = MergeSort_ByValue(PrePivot)
    SortedList.append(UnsortedList[Pivot])
    SortedList.extend(list(MergeSort_ByValue(PostPivot)))
    #print(SortedList)
    #input()
    return SortedList

def Test_MergeSort(Length):
    import random
    UnsortedList=[random.randint(0,100) for x in range(Length)]
    print(UnsortedList)
    print(MergeSort_ByValue(UnsortedList))
#Test_MergeSort(22)



def MergeSort_ByReference(UnsortedList):
    Reference_List = [x for x in range(len(UnsortedList))]
    return MergeSort_ByReference_Helper(UnsortedList,Reference_List)

def MergeSort_ByReference_Helper(UnsortedList,Reference_List):
    if(len(Reference_List)==0):
        return []
    if(len(Reference_List)<=1):
        return Reference_List


    Pivot = int(len(Reference_List)/2)
    List0 = Reference_List[0:Pivot]
    List1 = Reference_List[Pivot+1:]

    PrePivot = []
    PostPivot = []
    for List in [List0,List1]:
        for Location in List:
            Integer = UnsortedList[Location]
            if(Integer <= UnsortedList[Reference_List[Pivot]]):
                PrePivot.append(Location)
            else:
                PostPivot.append(Location)

    SortedList = MergeSort_ByReference_Helper(UnsortedList,PrePivot)
    SortedList.append(Reference_List[Pivot])
    SortedList.extend(list(MergeSort_ByReference_Helper(UnsortedList,PostPivot)))
    print(SortedList)
    #input()
    return SortedList

def getListByReference(List,ReferenceList):
    ListByReference = []
    for X in ReferenceList:
        ListByReference.append(List[X])
    return ListByReference


def Test_MergeSort_ByReference(Length):
    import random
    UnsortedList=[random.randint(0,100) for x in range(Length)]
    print(UnsortedList)
    ReferenceList = MergeSort_ByReference(UnsortedList)
    print(getListByReference(UnsortedList,ReferenceList))
#Test_MergeSort_ByReference(22)


print(type([1,2]))


#Todo Create Sort with Passed Comparison Method
