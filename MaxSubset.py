class Array():
    def __init__(self,Array):
        self.Array      = Array
        
        #self.Kadane_Max()
    def Prep_1D_QuickRange(self):
        self.QuickRange = [0 for X in range(len(self.Array)+1)]
        for X in range(1,len(self.QuickRange),1):
            self.QuickRange[X] = self.QuickRange[X-1] + self.Array[X]
        return 0
    def Get_QuickRange(self,From,To):
        return self.QuickRange[To]-self.QuickRange[From]
    
    def SetZero(self):
        self.Array = [0 for X in range(len(self.Array))]
    def AddArray(self,Array):
        for X in range(len(self.Array)):
            self.Array[X] += Array[X]
    def Kadane_Max(self):
        IndexSolution = [0 for X in range(len(self.Array)+1)]
        StartingPoint = [0 for X in range(len(self.Array)+1)]
        IndexSolution[0] = self.Array[0]
        
        RunningBest = -1 #set to - system.max
        BestRange   = (-1,-1)
        #previousReference =
        
        for Index in range(1,len(self.Array),1):
            if(IndexSolution[Index-1] > 0):
                IndexSolution[Index] = IndexSolution[Index-1]+self.Array[Index]
                StartingPoint[Index] = StartingPoint[Index-1]
            else:
                IndexSolution[Index] = self.Array[Index]
                StartingPoint[Index] = Index

            if(IndexSolution[Index] > RunningBest):
                RunningBest = IndexSolution[Index]
                BestRange = (StartingPoint[Index],Index)
        print(self.Array,":",BestRange,":",RunningBest)
        return (BestRange,RunningBest)
            #Temp[Index] =
            
    #def Recursive_Kadane

Test = Array([0,-3,1,2,3,-6])

class Matrix():
    def __init__(self,Matrix):
        self.Matrix   = Matrix
        self.X_Length = len(self.Matrix)
        self.Y_Length = len(self.Matrix[0])
        self.Kadane_2D_Max()
    def Prep_Matrix_QuickSum(self):
        return 0
    def Get_QuickSum(self,X1,Y1,X2,Y2):
        return 0
    #O(Colums**2 * Rows)
    def Kadane_2D_Max(self):
        RunningBest = -100 #set to - system.max
        #              X1 Y1 X2 Y2
        BestRange   = (-1,-1,-1,-1)

        for X_Index in range(self.X_Length):
            RowSums = [0 for X in range(self.X_Length)]
            for Xi_Index in range(X_Index,self.X_Length,1):
                for Y_Index in range(self.Y_Length):
                    RowSums[Y_Index] += self.Matrix[Xi_Index][Y_Index]

                Temp_Array = Array(RowSums)
                Tuple = Temp_Array.Kadane_Max()
                if(Tuple[1]>RunningBest):
                    BestRange = (X_Index, Tuple[0][0],
                                 Xi_Index,Tuple[0][1])
        print(BestRange)
        return BestRange
Test2 = Matrix([[0, 1, 2],
                [-1,-8, 5],
                [9,4,-1]])
print(type(0))
