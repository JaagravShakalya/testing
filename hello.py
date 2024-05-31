import random

def game():
    p1 = 0
    p2 = 0

    for i in range(101):
        number = random.randint(1,10000)
        if number % 2:
          p1 += 1
        else:
          p2 += 1

    print("player1 :", p1)
    print("player2 :", p2)

    if p2 > p1:
      print("p2 is the winner")
    else:
      print("p1 is the winner")


    print("game is now over, thanks for playing")

def main():
   times = int(input("how many times: "))
   for i in range(times):
      game()
  

if __name__ == "__main__":
    main()


