import heapq
def selection(arr):
  n=len(arr)
  for i in range(n):
    minindex=i
    for j in range(i+1,n):
        if arr[j]<arr[minindex]:
           minindex=j
    arr[i],arr[minindex]=arr[minindex],arr[i]
  return arr   

def selec_input():
   n=int(input("\n\nEnter no of elements"))
   arr=[]
   for i in range(n):
      arr.append(int(input()))
   print("\n\nsoretd eleemsta are ", selection(arr))
  
def prim(graph,n):
   mst=[]
   visited=[False]*n
   minheap=[(0,0)]
   total_weight=0
   while minheap:
      weight,u=heapq.heappop(minheap)
      if visited[u]:
       continue
      visited[u]=True
      total_weight+=weight

      if weight!=0:
         mst.append((u,weight))
      for v,w in graph[u]:
         if  not visited[v]:
            heapq.heappush(minheap,(w,v))
   return mst,total_weight

def takeinput():
   n=int(input("\nenter no of vertices"))
   graph={i:[] for i in range(n)}
   m=int(input("\nEnter number of edges "))
   print("\nenter the edgdes in format v1 v2 weight")   
   for _ in range(m):
      u,v,w=map(int,input("\nEnter edges").split())
      graph[u].append((v,w))
      graph[v].append((u,w))
   return graph,n



def main():
   print("\n1. selection sort")
   print("\n2.prims alsgorithm")
   ch=int(input("\nEnter your choice"))
   if ch==1:
      selec_input()
   elif ch==2:
      graph,n=takeinput()
      mst,total_weight=prim(graph,n)
      for u,weight in mst:
         print(f"\nvertex {u} with weight {weight}")

      print(f"\n Total weigth is {total_weight}")
   else:
      print("\nInvalid choice")
if __name__=="__main__":
   main()
      