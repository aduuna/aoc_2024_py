
def read_data(file="input.txt"):
    with open(file) as f:
        data = f.readlines()
    # basic clean up here
    data = [x.strip() for x in data]

    return data
    
def find_word(data, word, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    results = []
    if data[row][col] != word[0]:
        return None
    for direction in directions:
        for i in range(len(word)):
            new_row = row + direction[0] * i
            new_col = col + direction[1] * i
            if new_row < 0 or new_row >= len(data) or new_col < 0 or new_col >= len(data[0]):
                break
            if data[new_row][new_col] != word[i]:
                break
        else:
            results.append(direction)

    # print(row, col, "results", results)
    return results

def find_word_diag_x(data, word, row, col):
    left_diag = [(-1, -1), (1, 1)]
    right_diag = [(-1, 1), (1, -1)]
    results = []
    if row + 1 >= len(data) or col + 1 >= len(data[0]) or row - 1 < 0 or col - 1 < 0:
        return None
    left_diag_results = [(row+shift[0], col+shift[1]) for shift in left_diag]
    right_diag_results = [(row+shift[0], col+shift[1]) for shift in right_diag]

    left_diag_results = [data[r][c] for r,c in left_diag_results]
    right_diag_results = [data[r][c] for r,c in right_diag_results]

    left_diag_word = left_diag_results[0] + data[row][col] + left_diag_results[1]
    right_diag_word = right_diag_results[0] + data[row][col] + right_diag_results[1]

    if (left_diag_word == word or left_diag_word == word[::-1]) and (right_diag_word == word or right_diag_word == word[::-1]):
        return True
    else:
        return False



def part_1(data):
    search_word = "XMAS"
    results = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == search_word[0]:
                results += len(find_word(data, search_word, row, col))

    return results

def part_2(data):
    search_word = "MAS"
    results = 0
    for row in range(1, len(data)-1):
        for col in range(1, len(data[row])-1):
            if data[row][col] == search_word[1]:
                results += 1 if find_word_diag_x(data, search_word, row, col) else 0

    return results



if __name__ == '__main__':

    part_1 = part_1(read_data())
    print("Part 1 answer =>", part_1)

    part_2 = part_2(read_data())
    print("Part 2 answer =>", part_2)