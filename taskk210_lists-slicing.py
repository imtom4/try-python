#  https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-2-python-lists?ex=10
#  my_list[begin:end]
#  However, it's also possible not to specify these indexes. 
#  If you don't specify the begin index, Python figures out that you want 
#  to start your slice at the beginning of your list. If you don't specify the end index, 
#  the slice will go all the way to the last element of your list. 

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6] 

# Alternative slicing to create upstairs
upstairs = areas[-4:] 
