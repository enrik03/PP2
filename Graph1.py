import matplotlib.pyplot as plt

from stp import stp

def main():
    gr = stp(100000,100)
    print("Energy-Steps Graph")
    print(gr)

if __name__ == '__main__':
    main()

print(stp(100000, 100))
