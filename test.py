import numpy as np

def test_numpy():
    # Створення масиву NumPy
    arr = np.array([1, 2, 3, 4, 5])
    print("Масив NumPy:")
    print(arr)

    # Застосування математичних операцій
    print("\nМатематичні операції:")
    print("Сума:", np.sum(arr))
    print("Середнє значення:", np.mean(arr))
    print("Максимум:", np.max(arr))
    print("Мінімум:", np.min(arr))

    # Робота з багатовимірними масивами
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nБагатовимірний масив:")
    print(matrix)

    # Використання індексації та зрізів
    print("\nІндексація та зрізи:")
    print("Елемент в рядку 2, стовпчику 1:", matrix[1, 0])
    print("Зріз рядка 2:", matrix[1, :])

if __name__ == "__main__":
    test_numpy()
