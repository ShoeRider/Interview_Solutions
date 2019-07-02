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

class DB():
    def __init__(self,Location):
        self.Location = Location
    def Add(self):
        return 0
    def Remove(self):
        return 0
    def Check(self):
        return 0

#TODO:
class _BloomFilter():
    def __init__(self,**kwargs):
        #(self,Location,HashMap_Length,Hashes,Set_Length,ExpectedEntries=1000,FalsePositiveRate=0.01,EReference=10)
        #DataDepth,DataKeyWords- in Order to create HashGuides
        RuntimeParameters = {
                    'Type'             : type(1),
                    'ExpectedEntries'  : 1000,
                    'FalsePositiveRate': 0.01,
                    'Location'         : "",
                    'HashGuides'       : ["int"],
                    'HashBitLocations' : self.HashBitLocations,
                    }

        RuntimeParameters.update(kwargs)
        #print(RuntimeParameters)

        self.StoredElements = {}
        self.Type              = RuntimeParameters["Type"]
        self.ExpectedEntries   = RuntimeParameters["ExpectedEntries"]
        self.FalsePositiveRate = RuntimeParameters["FalsePositiveRate"]
        self.EnteredElements   = 0
        self.FalsePositives    = 0

        self._ConfigureBloomFilterValues(self.ExpectedEntries,self.FalsePositiveRate)

        self.HashGuides = {}
        for X in range(self.Hashes):
            self.HashGuides[X] = {}
            for HashGuide in kwargs['HashGuides']:
                self.HashGuides[X][HashGuide] = random.randint(1,sys.maxsize)

        self.HashBitLocations   = RuntimeParameters["HashBitLocations"]

        self.HashMap_To_HashKey = []
        for X in range(self.Hashes):
            self.HashMap_To_HashKey.append(random.randint(1,sys.maxsize))

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

    def HashBitLocations(self,Item):
        print("Please Redirect 'HashBitLocations' in kwargs.")
        print("This function will be used on any newly added item to get the Bit_Locations")
        #self.FalsePositiveList = []


    #_ConfigureBloomFilterValues Takes:
    #(ExpectedEntries:int,FalsePositive,Print=False)
    #Returns list of Suggested:

    # [0] = Suggested Size
    # [1] = Suggested HashFunctions
    def _ConfigureBloomFilterValues(self,ExpectedEntries,FalsePositive,Print=False):
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
        self.HashMap_Length = int(abs(Suggested_HashMap_Size))
        self.HashMap        = bitstring.BitArray(self.HashMap_Length)
        self.Hashes         = int(abs(Suggested_HashFunctions))
        #return [int(abs(Suggested_HashMap_Size)),int(abs(Suggested_HashFunctions))]

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
        print(len(BitLocations))
        for Index in range(len(BitLocations)):
            Sum += self.HashMap_To_HashKey[Index]*BitLocations[Index]
        return Sum
    #Returns
    # [0] = Entry Exists
    # [1] = UniqueHash
    # [2] = BitLocations
    def Check_Item(self,Item):
        Exists        = 0
        BitLocations  = self.HashBitLocations(Item)
        UniqueHash    = self.BitLocations_To_Hash(BitLocations)
        BitHashExists = self.Check_BitLocations(BitLocations)

        self.Add_BitLocations(BitLocations)

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

                    self.FalsePositives+=1
                    Exists = 1

        # Image definately does not exist Continue to add image
        return (Exists,UniqueHash,BitLocations)

    #Returns
    # [0] = Entry added
    def Add(self,Item):
        if(type(Item) != self.Type):
            return False

        GrayScale_List = self.Check_Item(Item)
        if (not GrayScale_List[0]):
            self.StoredElements[GrayScale_List[1]] = []

        self.StoredElements[GrayScale_List[1]].append(Item)
        self.EnteredElements+=1
        return not GrayScale_List[0]

def V2():
            Reference_List  = [x for x in range(1000)]
            RandomNumber = []
            for X in range(1000-1,-1,-1):
                Index = random.randint(0,X)
                Value = Reference_List.pop(Index)
                RandomNumber.append(Value)

            self.CharacterValues = {}
            for Index,Character in enumerate(string.printable):
                print(RandomNumber[Index])
                self.CharacterValues[Character] = RandomNumber[Index]


import string
class String_BF(_BloomFilter,object):
    def __init__(self,*args, **kwargs):
        kwargs["Dimentions"]       = 1
        kwargs["Type"]             = type("String")
        kwargs["HashGuides"]       = string.printable
        kwargs["HashBitLocations"] = self.String_HashBitLocations
        #super(Image_BF, self).__init__(*args,**kwargs)
        super(String_BF, self).__init__(**kwargs)

    def String_HashBitLocations(self,String):
        BitLocations = []

        for Hash in self.HashGuides:
            Sum = 0
            for Set in self.HashGuides[Hash]:
                for Character in String:
                    #print(self.HashGuides[Hash][Character])
                    Sum += self.HashGuides[Hash][Character]
            BitLocations.append(Sum%self.HashMap_Length)
        #EReference - Expenential reference ~number of referenced points per image
        return BitLocations

if(True):
    print("String_BF Tests")
    TestBF = String_BF()
    print(TestBF.Add("SomeThing"))
    print(TestBF.Add("SomeThing NEw"))


class _RGB_Image(_BloomFilter,object):
    def __init__(self,*args, **kwargs):
        kwargs["Dimentions"]       = 2
        kwargs["Type"]             = type(0)
        kwargs["HashGuides"]       = ["R","G","B","Intercept"]
        kwargs["HashBitLocations"] = self.Matrix_Hash
        #super(Image_BF, self).__init__(*args,**kwargs)
        super(Image_BF, self).__init__(**kwargs)

    def Matrix_Hash(self,Item):
        BitLocations = []

        for Hash in self.HashGuides:
            Sum = 0
            for Set in self.HashGuides[Hash]:
                for Character in String:
                    #print(self.HashGuides[Hash][Character])
                    Sum += self.HashGuides[Hash][Character]
            BitLocations.append(Sum%self.HashMap_Length)
        #EReference - Expenential reference ~number of referenced points per image
        return BitLocations

class RGB_Image_BF(_BloomFilter,object):
    def __init__(self,*args, **kwargs):
        kwargs["Dimentions"]       = 2
        kwargs["Type"]             = type(0)
        kwargs["HashGuides"]       = ["R","G","B","Intercept"]
        kwargs["HashBitLocations"] = self.RGB_Hash
        #super(Image_BF, self).__init__(*args,**kwargs)
        super(Image_BF, self).__init__(**kwargs)

    def RGB_Hash(self,Item):
        print("it worked")
        #EReference - Expenential reference ~number of referenced points per image
        return 0

class _MD_BloomFilter(object):
    def __init__(self,*args, **kwargs):
        RuntimeParameters = {
                    'ExpectedEntries'  : 1000,
                    'FalsePositiveRate': 0.01,
                    'Location'         : "",
                    'HashGuides'       : ["int"],
                    'HashBitLocations' : self.HashBitLocations,
                    }

        RuntimeParameters.update(kwargs)

        self.Sources = {}
        for Source in RuntimeParameters['Sources']:
            self.Sources[Source]=_BloomFilter

    def _Declare_RGB(self):
        Parameters={}
        Parameters["Dimentions"]       = 2
        Parameters["Type"]             = type(0)
        Parameters["HashGuides"]       = ["R","G","B","Intercept"]
        Parameters["HashBitLocations"] = self.RGB_Hash
if(False):
    print("_MD_BloomFilter Tests")

class Full_Image_BF(_BloomFilter,object):
    def __init__(self,*args, **kwargs):
        kwargs["Dimentions"]       = 2
        kwargs["Type"]             = type(0)
        kwargs["HashGuides"]       = ["R","G","B","Intercept"]
        kwargs["HashBitLocations"] = self.RGB_Hash
        #super(Image_BF, self).__init__(*args,**kwargs)
        super(Image_BF, self).__init__(**kwargs)

    def RGB_Hash(self,Item):
        print("it worked")
        #EReference - Expenential reference ~number of referenced points per image
        return 0

class Video_MD_BloomFilter(_MD_BloomFilter):
    def __init__(self,Location,*args, **kwargs):

        super(Video_MD_BloomFilter, self).__init__(,*args, **kwargs)
