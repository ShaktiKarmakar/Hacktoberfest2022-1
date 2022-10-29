def MaxActivities(arr, n):
    selected = []
     
    # Sort jobs according to finish time
    arr.sort(key = lambda x : x[1])
     
    i = 0
    selected.append(arr[i])
 
    for j in range(1, n):
      if arr[j][0] >= arr[i][1]:
          selected.append(arr[j])
          i = j
    return selected

#main
activity = []
n = int(input("Enter number of activities to be scheduled. "))
for i in range(n):
  start,end =(int (x) for x in input("Enter the start and end time.").split())
  activity.append([start,end])
selected = MaxActivities(activity, n)
print("\nNumber of activities selected : %d"%(len(selected)))
print("Following activities are selected :")
print(selected)
