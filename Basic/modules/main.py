import cal
import vehicle

print(cal.sum(2, 5))

owner = input()
car1 = vehicle.Car(owner)
car1.getStatus()

print("Accelerate:", end=" ")
value = int(input())
car1.accelerate(value)
car1.getStatus()

print("Decelerate:", end=" ")
value = int(input())
car1.decelerate(value)
car1.getStatus()
