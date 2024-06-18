import LinkedList

def test_solution(solution_function):
    test_cases = [
        {"input": [1], "output": [1]},
        {"input": [1,2], "output": [2, 1]},
        {"input": [1, 2, 3], "output": [3, 2, 1]},
        {"input": [1,2,3,4,5], "output": [5,4,3,2,1]},
    ]
    
    print(str(solution_function))

    for i in range(len(test_cases)):
        print(
            "Test",
            i + 1,
            "Pass:",
            LinkedList.compare_linked_list(
                solution_function(LinkedList.create_linked_list(test_cases[i]["input"])),
                LinkedList.create_linked_list(test_cases[i]["output"]),
            )
        )
