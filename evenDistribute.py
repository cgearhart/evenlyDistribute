

from string import replace

iStr = "a bc def g"
width = 15
#len(output) == width
# of spaces is evenly distributed
#output = "a   bc   def  g" # is ok: 3 spaces, 3 spaces, 2 spaces
#output = "a      bc def g" # is not ok: 6 spaces, 1 space, 1 space

def evenDistribute(inputStr, width):
    num_partitions = inputStr.count(' ') # 3
    total_spaces = width - (len(iStr) - num_partitions)  # 15 - 7 = 8
    min_num_spaces = total_spaces/num_partitions
    remaining_spaces = total_spaces - min_num_spaces*num_partitions
    spaces_between = [min_num_spaces]*num_partitions
    for idx, s in enumerate(spaces_between):
        s = s+1 if idx < remaining_spaces else s
        spaces_between[idx] = ' '*s
    return replace(inputStr, ' ', '%s') % tuple(spaces_between)
