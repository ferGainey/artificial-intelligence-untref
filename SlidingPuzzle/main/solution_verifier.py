class SolutionVerifier:

    def is_solution(self, matrix):
        solution = False
        if len(matrix) == 3:
            if matrix == [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]:
                solution = True
        elif len(matrix) == 4:
            if matrix == [['0', '1', '2', '3'], ['4', '5', '6', '7'], ['8', '9', '10', '11'], ['12', '13', '14', '15']]:
                solution = True
        return solution

    def has_solution(self, numbers_matrix):
        numbers_list = []
        for i in range(0, len(numbers_matrix)):
            for j in range(0, len(numbers_matrix[i])):
                numbers_list.append(int(numbers_matrix[i][j]))
        suma = 0 #the correct name is sum, but this word is reserved and can make confusions
        for position in range(0, len(numbers_list)):
            number = numbers_list[position]
            for i in range(position, len(numbers_list)):
                if number > numbers_list[i] and numbers_list[i] != 0:
                    suma += 1
        if suma % 2 == 0:
            return True
        else:
            return False