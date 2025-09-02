# book allocation or allocate books 
# given an array "arr" of integer numbers "arr[i]" represents the number of pages in the i-th books 
# there are "m" numbers of studentsand the task is to allocate all the books to the students 
# each book to each student at least one also book should be allocated to only one student, allocation should be in contigous mannar 
# you have to allocate the books to m students such that the maximum number of pages assigned to a student is minimum

# linear approach 
def student(arr,pages):
    stu = 1
    pages_stu = 0
    for i in range(len(arr)):
        if pages_stu + arr[i] <= pages:
            pages_stu += arr[i]
        else:
            stu += 1
            pages_stu = arr[i]
    return stu 

def allocation(arr,m): 
   low = max(arr)
   high = sum(arr)
   for pages in range(low,high):
       count_student = student(arr,pages)
       if count_student == m:
           return pages 
       
def main():
    arr = [25,46,28,49,24]
    m = 4
    result = allocation(arr,m)
    print(f"the max no of pages assign to student is minmum as :{result}")
if __name__ == "__main__":
    main()

# binary search approach 
def student(arr,pages):
    stu = 1
    pages_stu = 0
    for i in range(len(arr)):
        if pages_stu + arr[i] <= pages:
            pages_stu += arr[i]
        else:
            stu += 1
            pages_stu = arr[i]
    return stu 
def allocation(arr,m): 
   low = max(arr)
   high = sum(arr)
   while low <= high:
       mid = (low+high)//2
       if student(arr,mid) > m:
           low = mid+1
       else:
           high = mid-1
   return low 
def main():
    arr = [25,46,28,49,24]
    m = 4
    result = allocation(arr,m)
    print(result)
if __name__ == "__main__":
    main()

