def is_symmetric(lst):
  '''
  Parameter: lst; matrix
  This function is used to check if a matrix, or
  a list of lists, is symmetric according to the
  mathematical definition.
  '''
    for row_index in range(len(lst)):   ### iterates through row
        for col_index in range(len(lst[0])):   ### iterates through column
            if lst[row_index][col_index] != lst[col_index][row_index]:
            ### checks the value
                return False
    return True
