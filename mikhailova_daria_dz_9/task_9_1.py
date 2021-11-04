from time import sleep


class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in range(len(TrafficLight.color)):
            print(TrafficLight.color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)


traffic = TrafficLight()
traffic.running()
