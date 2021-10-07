import numpy as np


def test():
    newList = np.random.rand(10,10)
    print(newList,"\n")
    print("this is how to print coloums:",newList[4,:])


def main():
    test()

if __name__ == "__main__":
	main()
