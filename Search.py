def search(unordered_list,term):
    for i, item in enumerate(unordered_list):
        #print(i,term)
        if term ==unordered_list[i]:
            return i
    return None

list1=[60,1,88,10,11,600]

search_term=11
index_position=search(list1, search_term)
print(index_position)

list2=['packet','publish','data']
index_position2=search(list2,'data')
print(index_position2)

def search_ordered(ordered_list,term):
    ordered_list_size=len(ordered_list)
    for i in range(ordered_list_size):
        if term ==ordered_list[i]:
            return i
        elif ordered_list[i]>term:
            return None
    return Node
list1=[2,3,4,6,7]
index_position1=search_ordered(list1,5)

if index_position1 is None:
    print(None)
    
    
def binary_search_iterative(ordered_list,term):
    size_of_list=len(ordered_list)-1
    index_of_first_element=0
    index_of_last_element=size_of_list
    
    while index_of_first_element<=index_of_last_element:
        mid_point=(index_of_first_element+index_of_last_element)//2
        if ordered_list[mid_point]==term:
            return mid_point
        elif term>ordered_list[mid_point]:
            index_of_first_element = mid_point+1
        else:
            index_of_last_element=mid_point-1
    if index_of_first_element> index_of_last_element:
        return Node
    
def binary_search_recursive(ordered_list,first_element_index,last_element_index,term):
    if(last_element_index < first_element_index):
        return None
    else:
        #mid_point=first_element_index+(last_element_index-first_element_index)//2
        mid_point=(first_element_index+last_element_index)//2
        
        if ordered_list[mid_point]> term:
            return binary_search_recursive(ordered_list,first_element_index,mid_point-1,term)
        elif ordered_list[mid_point]<term:
            return binary_search_recursive(ordered_list,mid_point+1,last_element_index,term)
        else:
            return mid_point
        
def nearest_mid(input_list,low_index,upper_index,search_value):
    mid = low_index +(upper_index-low_index)/(input_list[upper_index]-input_list[low_index])*(search_value-input_list[low_index])
    return int(mid)

def interpolation_search(ordered_list,search_value):
    low_index=0
    upper_index=len(ordered_list)-1
    
    while low_index <=upper_index:
        mid_point=nearest_mid(ordered_list,low_index,upper_index,search_value)
        #print(mid_point)
        if mid_point>upper_index or mid_point<low_index:
            return None
        elif ordered_list[mid_point]==search_value:
            return mid_point
        elif search_value>ordered_list[mid_point]:
            low_index=mid_point+1
        else:
            upper_index=mid_point-1
    if low_index>upper_index:
        return None
        
   
        
      
        
        

#list=[10,30,100,120,500]
list=[44, 60, 75, 100, 120, 230, 250]
#x=binary_search_iterative(list,100)
#x=binary_search_recursive(list,0,4,1200)
x=interpolation_search(list,120)
print(x)