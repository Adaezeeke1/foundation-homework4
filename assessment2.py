# Section 2
# Question 2.1


def is_isogram(new_word):
    new_word = new_word.lower()
    unique_letters = set()

    for letter in new_word:
        if letter in unique_letters:
            return False
        else:
            unique_letters.add(letter)

    return True


# Examples
word = "isogram"
result = is_isogram(word)
print(result)

word = "level"
result = is_isogram(word)
print(result)


# Question 2.2- Please see test file for question 2.2

# Section 3
def calculate_class_allocation(number_of_students):
    number_of_classes = (number_of_students // 30) + 1 if number_of_students % 30 != 0 else number_of_students // 30
    num_students_per_class = number_of_students // number_of_classes

    remaining_students = number_of_students % number_of_classes

    class_allocation = {}

    for i in range(1, number_of_classes + 1):
        if i <= remaining_students:
            class_allocation[f"Class {i}"] = num_students_per_class + 1
        else:
            class_allocation[f"Class {i}"] = num_students_per_class

    print(f"Proposed Allocation: {number_of_classes} classes")
    print(class_allocation)


# Inputs/Outputs:
calculate_class_allocation(31)


calculate_class_allocation(59)


calculate_class_allocation(87)


# Section 4
# Please see sql file for Section 4
