#!/usr/bin/env python3
# encoding: utf-8

__copyright__ = "Copyright 2022, AAIR Lab, ASU"
__authors__ = ["Abhyudaya Srinet", "Rushang Karia", "Naman Shah"]
__credits__ = ["Siddharth Srivastava"]
__license__ = "MIT"
__version__ = "1.3"
__maintainers__ = ["Pulkit Verma", "Naman Shah"]
__contact__ = "aair.lab@asu.edu"
__docformat__ = 'reStructuredText'


def get_goal_string(object_dict, obj_list, obj_loc_list, goal_list, 
    goal_loc_list, env):
    """
        Returns
        ========
            str:
                A generic goal condition that will place every object based on
                its type and size at the correct goal.
    """
    
    goal_string = "(:goal (and "

    if env == "bookWorld":
        # For bookWorld: Each book must be placed at a bin with matching obj_type and size
        # object_dict has structure: {'object': {book_name: {...}}, 'goal': {bin_name: {...}}}
        for i, book in enumerate(obj_list):
            book_data = object_dict['object'][book]
            book_type = book_data['obj_type']
            book_size = book_data['size']
            
            # Find the matching bin for this book
            for j, bin_name in enumerate(goal_list):
                bin_data = object_dict['goal'][bin_name]
                bin_type = bin_data['obj_type']
                bin_size = bin_data['size']
                
                # Check if book and bin match on both type and size
                if bin_type == book_type and bin_size == book_size:
                    # Get the bin location
                    bin_loc = goal_loc_list[j]
                    # Goal: book should be at the bin location
                    goal_string += "(book_at %s %s) " % (book, bin_loc)
                    break

    elif env == "cafeWorld":
        # For cafeWorld: Each food must be placed at a table with matching obj_type and size
        for i, food in enumerate(obj_list):
            food_data = object_dict['object'][food]
            food_type = food_data['obj_type']
            food_size = food_data['size']
            
            # Find the matching table for this food
            for j, table in enumerate(goal_list):
                table_data = object_dict['goal'][table]
                table_type = table_data['obj_type']
                table_size = table_data['size']
                
                # Check if food and table match on both type and size
                if table_type == food_type and table_size == food_size:
                    # Get the table location
                    table_loc = goal_loc_list[j]
                    # Goal: food should be at the table location
                    goal_string += "(food_at %s %s) " % (food, table_loc)
                    break
    
    goal_string += "))\n"
    
    return goal_string


def sample_goal_condition(object_dict, obj_list, obj_loc_list, goal_list, 
    goal_loc_list):
    """
        Returns
        ========
            str:
                A generic goal condition that moves the robot to any one of
                the object locations.

        
        .. note ::

            You can replace the contents of get_goal_string() with the text below
            to get an idea of what is expected.
            
            The goal condition in the stock task here is VASTLY different from the
            expectation from you. Please review the homework documentation to identify
            your task.
            
            Here are some instructions to run this in Gazebo.
            1. Replace the content of get_goal_string() with this method.
            2. rosrun hw2 refinement.py \
                --objtypes <object types> \
                --objcount <number of objects> \
                --seed <seed>
            3. rosrun hw2 gazebo.py

            The generic goal condition here is to move the robot to a object location.
            
            The stock task below generates a generic goal condition that moves the
            robot to a random object location and this is independent of the total 
            number of locations and objects. 
            
    """

    import random
    assert len(obj_loc_list) > 0
    i = random.randint(0, len(obj_loc_list) - 1)
    
    goal_string = "(:goal (and "
    goal_string += "(Robot_At tbot3 %s)" % (obj_loc_list[i])
    goal_string += "))\n"
    
    return goal_string
