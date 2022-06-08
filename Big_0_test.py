# Snippet 1 - Big O:

def largest(array, value):
  for item in array:
    if item > value:
      return False
  return True 

# O(N)
# Answer is Linear Time because the function will test each value in the array against the value until the test fails. 
# you could have 1000 true statements in the array and the 1001 be false and the function will search sequntially until it reaches that point




# Snippet 2 - Big O:


def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])
  
# O(n^2)
# Answer is Quadratic Time because for every new customer added to the list you must make two addtional print statements

# Snippet 3 - Big O:





def first_element_is_red(array):
  return array[0] == 'red' 

# 0(1) 
# Answer is Constant Time because no matter how large the array gets, its only ever making one check agaisnt the first element





# Snippet 4 - Big O:

def duplicates(array):
  for index1, item1 in enumerate(array):
    for index2, item2 in enumerate(array):
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False


# O(2^N)
# Answer is exponential time because for every added element and new magnitude order of combinations is added to check against





# Snippet 5 - Big O:

words = ['chocolate', 'coconut', 'rainbow']
endings = ['cookie', 'pie', 'waffle']

for word in words:
  for ending in endings:
    print(word + ending)

# O(n * m)
# each list is independently linear

# 0(log n log) - orginal thoughts:
# Answer is Log Linear because it increases slightly for each new item added., but it is not exponetially growing
# for each new item added to List 1 it adds on more combination with everything else in List 2.
# this is longer than Linear Time but it is not like the duplicates problem above that creates a new order of magnitude of combinations




# Snippet 6 - Big O:

numbers = [1,2,3,4,5,6,7,8,9,10]

def print_array(array):
  for item in array:
    print(item)


# 0(n)
# Answer is is Linear Time as you added one new print statement for each addtional array element



# Snippet 7 - Big O:


# this is insertion sort
def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : 
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 

# O(N)
# for as much as is happening in this equation for every new element added to the array it gets cycled through the same number of steps





# Snippet 8 - Big O:

for i in range(len(my_list)):
  min_idx = i
  for j in range(i+1, len(my_list)):
      if my_list[min_idx] > my_list[j]:
          min_idx = j

  my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]

# O(2^N)
# for each new element added it add a new magnitude of operations