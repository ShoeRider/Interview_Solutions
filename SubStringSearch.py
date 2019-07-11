

#def FindPrePostFix(String)
#Short: Takes String and returns the ending index of the longest Prefix with a matching PostFix
#Long: This is used by KMP_SubStringSearch to provide repeating PrePostFix Strings inorder to shorten the Substring search, by removing repeated strings.
#Big O(N)
#Example: FindPrePostFix("69696986969")
#Returns:
def FindPrePostFix(String):
    #print("Given:",String)
    String_Length = len(String)
    half = int(String_Length/2)
    if(String_Length ==0):
        return 0

    
    if len(String)%2 == 0:
        #print("\t",String[0:half],":",String[half:String_Length])
        for X in range(half+1,0,-1):
            if (String[0:X] == String[X:String_Length]):
                #print("\tReturning",X)
                return (X)
    else:
        #print("\t",String[0:half],":",String[(half+1):String_Length])
        for X in range(half+1,0,-1):
            #print(X)
            if (String[0:X] == String[X+1:String_Length]):
                #print("\tReturning",X)
                return (X)
    return 0
    
    print("\t")

if False:
    String = "aab"
    PrePost_List = [FindPrePostFix(String[0:X]) for X in range(len(String)+1)]
    print(PrePost_List)
if False:
    String = "6969"
    PrePost_List = [FindPrePostFix(String[0:X]) for X in range(len(String)+1)]
    print(PrePost_List)

    
    
def SubStringSearch_BF(String,SubString):
    Locations = []
    if (len(String) == 0 or len(SubString)==0):
        return Locations
    for String_Slide in range(len(String)-len(SubString)+1):
        for SubString_Slide in range(len(SubString)):
            #print("not String[String_Slide+SubString_Slide] == SubString[SubString_Slide] :",not String[String_Slide+SubString_Slide] == SubString[SubString_Slide])
            if not String[String_Slide+SubString_Slide] == SubString[SubString_Slide]:
                break

            if(SubString_Slide == len(SubString)-1):
                Locations.append(String_Slide)
    return Locations


def KMP_SubStringSearch(String,SubString):
    print("Given:",String, " and ",SubString)
    
    
    Locations = []
    PrePost_SubStrings = [FindPrePostFix(SubString[0:X]) for X in range(len(SubString)+1)]
    print(PrePost_SubStrings)
    if (len(String) == 0 or len(SubString)==0):
        return Locations
    
    
    Slide_To         = len(String)
    SubString_Slide  = 0
    SubString_Length = len(SubString)-1
    print("Slide_To:",Slide_To)
    for X in range(Slide_To):
        if String[X] == SubString[SubString_Slide]:
            if SubString_Slide==SubString_Length:
                Locations.append(X-SubString_Length)
                
                SubString_Slide = PrePost_SubStrings[SubString_Slide]
            else:
                SubString_Slide+=1
        else:
            SubString_Slide = PrePost_SubStrings[SubString_Slide-1]
            
            
        
    return Locations

def Test_SubStringSearch(Function):
    String    = "aaaaab"
    SubString = "aab"
    print(Function(String,SubString))
    String    = "696969"
    SubString = "69"
    print(Function(String,SubString))
    String    = "6969269"
    SubString = "69"
    print(Function(String,SubString))

#Test_SubStringSearch(SubStringSearch_BF)
Test_SubStringSearch(KMP_SubStringSearch)

if True:
    SubString = "6969"



    
if False:
    Temp = "asdasd"
    print(Temp[0:1])
    print(Temp[0:1])

    print(FindPrePostFix("asdasd"))
