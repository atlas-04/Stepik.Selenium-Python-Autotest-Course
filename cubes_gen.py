def cube_numbers(nums):  
    for i in nums:
        yield(i**3)

cubes = cube_numbers([1, 2, 3, 4, 5])

print(cubes)