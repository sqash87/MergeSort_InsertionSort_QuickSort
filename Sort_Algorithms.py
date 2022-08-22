

#Merge Sort
def Merge(array_list,left_half,right_half):
    left_index=0
    right_index=0
    sorted_index=0

    #Whenever either the left_half or the right_half of the array_list is done with 
    #coping data their data into the sorted list, (array_list), the while loop breaks.
    while left_index < len(left_half) and right_index<len(right_half):
        if left_half[left_index]<right_half[right_index]:
            array_list[sorted_index]= left_half[left_index]
            left_index= left_index+1
            sorted_index= sorted_index+1
        else:
            array_list[sorted_index]= right_half[right_index]
            right_index=right_index+1
            sorted_index=sorted_index+1
    
    #if any elements of the left_half is left without being copied into the sorted list,
    #copy those elemnets in the sorted list.
    while left_index < len(left_half):
        array_list[sorted_index]= left_half[left_index]
        left_index= left_index+1
        sorted_index= sorted_index+1
    
    #if any elements of the right_half is left without being copied into the sorted list,
    #copy those elemnets in the sorted list.
    while right_index<len(right_half):
        array_list[sorted_index]= right_half[right_index]
        right_index=right_index+1
        sorted_index=sorted_index+1

def Divide(array_list):
    if len(array_list)>1:
        mid= len(array_list)//2
        #[index 0, midpoint)
        left_half= array_list[:mid]
        #[midpoint, last index]
        right_half= array_list[mid:]
        Divide(left_half)
        Divide(right_half)
        Merge(array_list,left_half, right_half)


#List1= [2,8,3,17,23,56,34,39,14,18,9]

#Divide(List1)

#print("The sorted list: ")

#print(List1)

        


#Insertion sort
def InserSort(array_list):
    primary_index=1
    sorted_List=[]
    sorted_List.append(array_list[0])
    
    #tarversing the primary lsit from left to right.
    while primary_index<len(array_list):
        sorted_last_index= len(sorted_List)-1
        
        #tarversing the sorted_list from right to left and compare each primary list item with it.
        while sorted_last_index>0:
            #if the primary list element is less than the sorted list item, keep tarversing left by sorted_last_index-1. 
            if array_list[primary_index]<sorted_List[sorted_last_index]:
                sorted_last_index= sorted_last_index-1
            
            #if the primary list element is greater than the sorted list item, insert that item in sorted_last_index+1
            else:
                sorted_List.insert(sorted_last_index+1, array_list[primary_index])
                break
        #Special condition when insertinge element to the fist index.
        if sorted_last_index==0:
            if array_list[primary_index]<sorted_List[sorted_last_index]:
                sorted_List.insert(sorted_last_index,array_list[primary_index])
            else:
                sorted_List.insert(sorted_last_index+1,array_list[primary_index])

        
        primary_index=primary_index+1
    
    return sorted_List

        
#list1= [6,8,19,14,9,29,26,97,65,78,84,36,33]

#list2= InserSort(list1)

#print(list2)


#QuickSort

#first Quick sort function will take an arry with left and right index.

def QuickSort(array_list, left, right):
    
    if left<right:
        partition_index= partition(array_list, left, right)
        QuickSort(array_list, left, partition_index -1 )
        QuickSort(array_list, partition_index + 1, right)
    
#Finding the pivit index.
def partition(array_list, left, right):
    i = left
    j= right-1
    pivot= array_list[right]

    while i<j:

        while i < right and array_list[i]<pivot:
            i = i+1
        while j> left and array_list[j]>=pivot:
            j = j-1
            
        #after i finding the element larger than pivot and j finding the element samller than the pivot:
        # swap i's value with j's
        if i<j:
            array_list[i], array_list[j] = array_list[j], array_list[i]
        #Since, j traverse from right to left to find an element that is smaller than the pivot, 
        # so when J passes over i, array_list[i] will be samller than pivot.
    if array_list[i]>pivot:
        array_list[i], array_list[right]= array_list[right], array_list[i]
    return i

list1= [6,8,19,14,9,29,26,97,65,78,84,36,33]
length= int(len(list1))
QuickSort(list1, 0, length-1)

print(list1)
























    
