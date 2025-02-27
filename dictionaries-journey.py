# def merge_dictionaries(dict1, dict2):
#     merged_dict = dict1.copy()
#     merged_dict.update(dict2)
#     return merged_dict


# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 10, "d": 4}

# result = merge_dictionaries(dict1, dict2)
# print(result) 




# def word_count(sentence):
#     words = sentence.split()
#     word_dict = {}
#     for word in words:
#          if word in word_dict:
#             word_dict[word] += 1
#          else:
#             word_dict[word] = 1
#     return word_dict    

# sentence = input("Enter a sentence: ")
# result = word_count(sentence)
# print(result)




def count_total_employees(company_employees):
    total_employees = 0
    for department in company_employees.values():
        total_employees += len(department)
    return total_employees

company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "Develops Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}

print(company_employees)
