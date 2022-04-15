# dijkstra-algorithm

<img src="https://user-images.githubusercontent.com/21102151/163158612-1d5fb346-d5c4-4576-bed1-740f1afc0e48.png" width=70% height=70%>

### Intro

- animation : https://github.com/AlgorithmsMeetup/Pathfinding

![image](animation.gif)

- example

![image](https://user-images.githubusercontent.com/21102151/163220841-9ea1a414-e9db-4eb1-829d-651e4eb108b0.png)
![image](https://user-images.githubusercontent.com/21102151/163221530-db2896af-0014-4d25-94e2-daf8aeca3767.png)


### standard method (better)
   - check fichier excel file
   - ![image](https://user-images.githubusercontent.com/21102151/163026415-ac5a6173-6bed-47d3-95eb-131cefbd5f70.png)
   - source : https://youtu.be/5GT5hYzjNoo
   - ![image](https://user-images.githubusercontent.com/21102151/163024147-fb29e96e-572d-40fe-8382-dbb829409e2a.png)

### Standard method 2: take each node from the start to the end
   - ![image](https://user-images.githubusercontent.com/21102151/162724380-ec759817-e547-4c6a-9127-52fc459f4a88.png)

### My firdt method (well understood by snt students)
  - take each node, calculate best path from the origin to that node
  - ![image](https://user-images.githubusercontent.com/21102151/162714175-5406c274-6c7d-43f5-b201-6866f416092f.png)
  - ![image](https://user-images.githubusercontent.com/21102151/162715506-94150126-ac58-4f5e-b55d-1b6184e7c3e3.png)
  - ![image](https://user-images.githubusercontent.com/21102151/162716027-d7affec9-97ae-418d-8c8c-6ade494a2d65.png)

### Code
```python
max = 0
for node in graph:
  for i in graph[node].items():
    max = max + i[1]
max += 1
print(max)

list=[node for node in graph]
list2 = [[graph[node][s] for s in graph[node] ] for node in graph ]
print( list2)
```

### Best links
   - https://youtu.be/CL1byLngb5Q
       - ![image](https://user-images.githubusercontent.com/21102151/162725210-c7ba28a9-319b-484c-828e-fdcc37a3c318.png)
       - ![image](https://user-images.githubusercontent.com/21102151/162725301-d50d9565-e706-4530-8e73-d66e7be9d4dd.png)
   - `implementation in many languages` : https://github.com/mburst/dijkstras-algorithm
   - other example
   ![image](https://user-images.githubusercontent.com/21102151/163464172-dbb053c1-cb75-4594-a299-d6cf6b15898d.png)

