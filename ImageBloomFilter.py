import sys

import cv2
import numpy as np
import math
import bitstring
import random
random.seed(0)


# Image Hash Requirements:
#Needs to work with:
#   different image sizes,
#   should be
class Image():
    def __init__(self,Path,QuickSum=False):
        self.GS_Matrix   = cv2.imread(Path,0)
        self.RGB_Matrix  = cv2.imread(Path,1)
        self.Height      = len(self.GS_Matrix)
        self.Length      = len(self.GS_Matrix[0])
        self.Ratio       = self.Height/self.Length
        #BitColorDepth
        #HashFunction/Method


    #TODO: IMPLEMENT CV2 Quick Matrix compairison
    #Returns :
    # 0 (False): Images are different
    # 1 (True): Images are the same
    def SameImage(self,Image2,GrayScale=True):
        if (Image2.Height != self.Height or Image2.Length != self.Length):
            return 0
        AbsoluteDistance = 0
        for X in range(self.Height):
            for Y in range(self.Length):
                if(self.GS_Matrix[X][Y] != Image2.GS_Matrix[X][Y]):
                    return 0
        return 1

    def _Print_Dimensions(self):
        print("Height: "+str(self.Height))
        print("Length: "+str(self.Length))
        print("H/L Ratio: "+str(self.Ratio))

    def _Get_RegionSum(self,Height,L,R):
        return 0

    #Get RED GREEN BLUE Number Points Simple
    #Returns List with Dimentions: [self.Height][self.Length][3]
    def _GetRGB_NPS(self,N):
        List = []
        _HStepDistance = int(self.Height/(N+1))
        _LStepDistance = int(self.Length/(N+1))
        for X in range(N):
            for Y in range(N):
                List.append(self.RGB_Matrix[_HStepDistance*X][_LStepDistance*Y])
        return List

    #Get Gray Scale Number Points Simple
    def _GetGS_NPS(self,N):
        List = []
        _HStepDistance = int(self.Height/(N+1))
        _LStepDistance = int(self.Length/(N+1))
        for X in range(N):
            for Y in range(N):
                List.append(self.GS_Matrix[_HStepDistance*X][_LStepDistance*Y])
        return List

#TODO Hash by:
# 1. Ratio Points
# 2. Quadtrees

#img = cv2.imread(,1)

if False:
    Cat_Image = Image('25.jpg')
    print(type(cv2.imread('25.jpg',1)))
    Cat_Image._Print_Dims()
    print(Cat_Image._Get_NPS(4))
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if True:
    Cat_Image = Image('25.jpg')
    print(Cat_Image.SameImage(Image('25.jpg')))


if True:
    list = bitstring.BitArray(10)
    print(list)
    list[2] = bitstring.BitArray(bin='1')
    list[3] = '0b1'
    print(list)

class _BloomFilter:
    def __init__(self,HashMap_Length,Hashes,Set_Length):
        self.StoredElements = {}



#class String_BloomFilter(_BloomFilter):
#    def __init__(self):



class _ImageBloomFilter():
        #k= (m/n)*ln2
        #(ax+b) mod 17
    def __init__(self,Location,HashMap_Length,Hashes,Set_Length,ExpectedEntries=1000,FalsePositiveRate=0.01,EReference=10):
        self.ExpectedEntries = ExpectedEntries
        self.EnteredElements = 0
        self.FalsePositives = 0

        #self.FalsePositiveList = []
        self.LastHundred    = []

        self.StoredElements = {}
        self.HashMap_Length = HashMap_Length
        self.HashMap        = bitstring.BitArray(self.HashMap_Length)

        self.Hashes         = Hashes
        #EReference - Expenential reference ~number of referenced points per image
        self._EReference    = EReference

        self.RGB_Primes     = {'R' : 101,'G' : 151,'B' : 191,'Gray' : 199}


        #The following Creates a set of dictionaries for each different Hash Function:
        #For RGB Images:
        #  HASH(Integer) = 'A'*Red + 'B'*Green + ''
        #For GrayScale Images:
        #  HASH(Integer) = 'A'*GrayScaleValue + 'B'
        self.HashMap_To_HashKey = []
        for X in range(self.Hashes):
            self.HashMap_To_HashKey.append(random.randint(1,sys.maxsize))

        self.HashGuides = {}
        for X in range(self.Hashes):
            R = random.randint(1,sys.maxsize) #Red
            G = random.randint(1,sys.maxsize) #Green
            B = random.randint(1,sys.maxsize) #Blue
            I = random.randint(1,sys.maxsize) #Intercept

            self.HashGuides[X] = {'R':R, 'G':G, 'B':B, 'I':I}
        self.Print_Description()

    def Print_Description(self):
        print("HashMap_Length:"+str(self.HashMap_Length))
        print("Hashes:"+str(self.Hashes))

    def CheckHealth(self):
        print("_ImageBloomFilter Health:")
        self.Print_Description()
        print(" All time false positives:",self.FalsePositives)

        #print(" Last 100 entries:",0,"% (",0,"/100)")
        print("~"+str(100*self.EnteredElements/self.ExpectedEntries)+"% Full, ("+str(self.EnteredElements)+"/"+str(self.ExpectedEntries)+")")
        print("Dictionary Keys Used: "+str(len(self.StoredElements.keys())))
        BitsSet = 0
        for X in self.HashMap:
            if X:
                BitsSet += 1
        print("Bits Set: "+str(BitsSet)+"/"+str(self.HashMap_Length))
        return 0
    #SuggestBloomFilterValues Takes:
    #(ExpectedEntries:int,FalsePositive,Print=False)
    #Returns list of Suggested:
    # [0] = Suggested Size
    # [1] = Suggested HashFunctions
    def SuggestBloomFilterValues(self,ExpectedEntries,FalsePositive,Print=True):
        #ExpectedEntries - number of items we plan to put in the list
        #FalsePositive - probability we will accept/Desire
        Suggested_HashMap_Size  = ((ExpectedEntries*np.log(FalsePositive))/(np.log(2)**2))
        Suggested_HashFunctions = abs(Suggested_HashMap_Size/ExpectedEntries)*np.log(2)
        RealChance              = math.exp((Suggested_HashMap_Size*(math.log(2)**2))/ExpectedEntries)

        if (Print):
            print("Suggested_HashMap_Size: ",abs(Suggested_HashMap_Size))
            print("Suggested # of Hashes:",Suggested_HashFunctions)
            print("The Real Chance:",RealChance)

        if (int(abs(Suggested_HashFunctions)) < 1):
            Suggested_HashFunctions = 1
        return [int(abs(Suggested_HashMap_Size)),int(abs(Suggested_HashFunctions))]

    def Reset_BitArray(self,Message="User Initiated"):
        self.HashMap         = bitstring.BitArray(HashMap_Length)
        self.ExpectedEntries += ExpectedEntries * 0.1
        self.FalsePositiveRate = self.FalsePositiveRate
        SuggestedList = self.SuggestBloomFilterValues(self.ExpectedEntries,self.FalsePositiveRate)

        print("Reset Bit Array Started by:"+Message)
        #TODO:
        # - Calculate New Optimum/Random Numbers
        # - reCalculate Image Hashes
        #
        return 0

    def StartUp_BitArray(self):
        #TODO: Read Random Preferences and preform 'setup'.
        return 0


    def Find_ArrayIndexes(self,Array):
        ArrayIndexes = [0] * self.Hashes
        return 0
    def Add_ElementsInStepSize(self,Step,Array):
        Sum = 0
        Step_From = int(self.Element_Step*Step)
        Step_To   = int(self.Element_Step*(Step+1))

        #print("\t",Step," ",Step_From,":",Step_To-1)
        for X in range(Step_From,Step_To,1):
            #print("\t Gathering from :",X)
            #print("\t  the Value: ",Array[X])
            Sum += (Array[X])
        return Sum/self.Gradient

    def Get_GS_BitLocations(self,GS_Array):
        GS_Locations = []
        #print("self.HashGuides",self.HashGuides)
        GS_Sum = sum([element for element in GS_Array])
        #RGB_MatrixSum = sum(Col for Col in sum([Row for Row in GS_Matrix]))
        ArrayIndexes = [0] * self.Hashes

        for Hash in self.HashGuides:
            #SIF = _SlopeInterceptForm
            SIF = self.HashGuides[Hash]
            GS_Locations.append(int(SIF["G"] * GS_Sum + SIF["I"])% self.HashMap_Length)
        return GS_Locations

    def Add_BitLocations(self,Bit_Locations):
        for Index in range(len(Bit_Locations)):
            #print(Bit_Locations)
            #bitstring.bitarray('1')
            self.HashMap[Bit_Locations[Index]] = '0b1'

    def Hash_Exists(self,Hash):
        #print("Exists: ",Hash in self.StoredElements.keys())
        if (Hash in self.StoredElements.keys()):
            return 1
        return 0

    def Check_BitLocations(self,Bit_Locations):
        for Location in Bit_Locations:
            if(self.HashMap[Location] == False):
                return 0
        return 1

    #Returns
    # Sum/HashValue
    def BitLocations_To_Hash(self,BitLocations):
        Sum = 0
        for Index in range(len(BitLocations)):
            Sum += self.HashMap_To_HashKey[Index]*BitLocations[Index]
        return Sum
    #Takes:
    # (ImageLocation='Location')
    # ()
    def Add_GrayScaleImage(self, **kwargs):

        if "GS_Array" not in kwargs:
            kwargs["GS_Array"] = Image(kwargs["FileLocation"])._GetGS_NPS(self._EReference)

        #GS_Array,Location
        GrayScale_List = self.Check_GrayScaleImage(kwargs["GS_Array"],kwargs["FileLocation"])
        if (not GrayScale_List[0]):
            self.StoredElements[GrayScale_List[1]] = []
        else:
            self.FalsePositives+=1

        self.StoredElements[GrayScale_List[1]].append(kwargs["FileLocation"])
        self.EnteredElements+=1
        return GrayScale_List

    #Returns
    # [0] = Entry Exists
    # [1] = UniqueHash
    # [2] = FalsePositive
    # [3] = BitLocations
    def Check_GrayScaleImage(self,GS_Array,Location):
        Exists        = 0
        BitLocations  = self.Get_GS_BitLocations(GS_Array)

        UniqueHash    = self.BitLocations_To_Hash(BitLocations)
        BitHashExists = self.Check_BitLocations(BitLocations)

        self.Add_BitLocations(BitLocations)
        FalsePositive = None

        if BitHashExists:
            Hash = self.BitLocations_To_Hash(BitLocations)
            # Image might exist, need to further check
            HashExists = self.Hash_Exists(Hash)
            if (HashExists):
                #Need to further investigate to ensure no missed unique image
                FileList = self.StoredElements[Hash]
                for File in FileList:
                    #test2Images
                    #if test2Images: FalsePositive = True
                    FalsePositive = True
                    Exists = 1

        # Image definately does not exist Continue to add image
        return (Exists,UniqueHash,FalsePositive,BitLocations)
    def Add_GS_ImageLocation(self,Location):
        Test_Image = Image(Location)

        Test_BF.Add_GrayScaleImage(Test_Image._GetGS_NPS(EReference))
        return 0





#SuggestBloomFilterValues Takes:
#(ExpectedEntries:int,FalsePositive,Print=False)
#Returns list of Suggested:
# [0] = Suggested Size
# [1] = Suggested HashFunctions
def SuggestBloomFilterValues(ExpectedEntries,FalsePositive,Print=True):
    #ExpectedEntries - number of items we plan to put in the list
    #FalsePositive - probability we will accept/Desire
    Suggested_HashMap_Size  = ((ExpectedEntries*np.log(FalsePositive))/(np.log(2)**2))
    Suggested_HashFunctions = abs(Suggested_HashMap_Size/ExpectedEntries)*np.log(2)
    RealChance              = math.exp((Suggested_HashMap_Size*(math.log(2)**2))/ExpectedEntries)

    if (Print):
        print("Suggested_HashMap_Size: ",abs(Suggested_HashMap_Size))
        print("Suggested # of Hashes:",Suggested_HashFunctions)
        print("The Real Chance:",RealChance)

    if (int(abs(Suggested_HashFunctions)) < 1):
        Suggested_HashFunctions = 1
    return [int(abs(Suggested_HashMap_Size)),int(abs(Suggested_HashFunctions))]

def Create_SuggestedBloomFilter(ExpectedEntries,FalsePositive,Array_Length,EReference=4):
    Size_HFunctions = SuggestBloomFilterValues(ExpectedEntries,FalsePositive)
    return _ImageBloomFilter("",Size_HFunctions[0],Size_HFunctions[1],Array_Length,ExpectedEntries=ExpectedEntries,EReference=EReference)




if True:
    #EReference - Exponential Reference
    EReference = 4
    Test_BF = Create_SuggestedBloomFilter(50,.01,EReference**2)
    Test_BF.Print_Description()
    PictureRange = (500,550)

    for X in range(PictureRange[0],PictureRange[1],1):
        #print('VideoSet0//frame'+str(X)+'.jpg')

        #Test_Image = Image('VideoSet0//frame'+str(X)+'.png')
        #print(Test_BF.Add_GrayScaleImage(GS_Array = Test_Image._GetGS_NPS(EReference),FileLocation='VideoSet0//frame'+str(X)+'.png'))

        print(Test_BF.Add_GrayScaleImage(FileLocation='VideoSet0//frame'+str(X)+'.png'))
    Test_BF.CheckHealth()

if(False):
    GS_Matrix = cv2.imread('25.jpg',0)
    print(GS_Matrix)
    Array_Sum = sum(Col for Col in sum([Row for Row in GS_Matrix]))
    #Array_Tottal = sum([Element for Element in GS_Matrix])
    print(Array_Sum)

if False:
    EReference = 1
    Test_BF = Create_SuggestedBloomFilter(10,.01,EReference**2)
    Test_Image_0 = Image('25.jpg')
    Test_Image_01 = Image('166.jpg')

    #print(Test_BF.HashMap)
    print(Test_BF.Add_GrayScaleImage(Test_Image_0._GetGS_NPS(EReference),"Location"))
    #print(Test_BF.HashMap)
    #ignore = input("l")
    print(Test_BF.Add_GrayScaleImage(Test_Image_01._GetGS_NPS(EReference),"Location"))
    #print(Test_BF.HashMap)
    #input()
    print(Test_BF.Add_GrayScaleImage(Test_Image_0._GetGS_NPS(EReference),"Location"))
    #print(Test_BF.HashMap)
    #input()
    #Array_BloomFilter(BF_Length,Hashes,Array_Length)
