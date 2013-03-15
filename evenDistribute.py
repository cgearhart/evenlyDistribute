

from string import replace

iStr = "a bc def g"
width = 15
#len(output) == width
# of spaces is evenly distributed
#output = "a   bc   def  g" # is ok: 3 spaces, 3 spaces, 2 spaces
#output = "a      bc def g" # is not ok: 6 spaces, 1 space, 1 space

def evenDistribute(inputStr, width):
    num_partitions = inputStr.count(' ') # 3
    total_spaces = width - sum(len(item) for item in inputStr.split(' '))  # 15 - 7 = 8
    min_spaces_between = total_spaces/num_partitions
    total_spaces -= min_spaces_between*num_partitions
    spaces_between = [min_spaces_between]*num_partitions  # [2, 2, 2]
    print spaces_between
    outputStr = replace(inputStr, ' ', '%s')
    spaces_between = [' '*(s+1) if idx < total_spaces else ' '*s for idx, s in enumerate(spaces_between)]
    print spaces_between
    return outputStr % tuple(spaces_between)


print evenDistribute(iStr, width)