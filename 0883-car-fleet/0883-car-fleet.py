class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = list(zip(position, speed))
        temp.sort(key = lambda x:x[0], reverse = True)
        time = [(target-car[0])/car[1] for car in temp]
        # print(time)
        fleet = 1
        temp = time[0]
        while time:
            if temp>= time[0]:
                time.pop(0)
            else:
                temp = time.pop(0)
                fleet+=1
        return fleet




        