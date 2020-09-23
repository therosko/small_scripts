# Autograding homeworks with personalised datasets using `nbgrader`

This example describes a case, in which you might expect **different submissions of the same homework to produce different results** (see Example bellow). In this case a traditional approach using only the *asser_equal* function (comparing student function to an expected output) would not be sufficient for the task. 

As a solution, we **write and import a python module**. In order to find the correct/expected answer for the individual students' notebooks, we call a function from the created **python module** and receive the matching/expected output. 

## Example:

Let us imagine that we want all students in a course to receive their **individual dataset** to work with. In this case, it may occur that even if all tasks, given to the students, are the same, the received outputs of the individual students may differ. In this case, we would want to match the *students answer* to a *correct answer we expect to receive*. We receive this correct answer by calling the created python module for each individual submision using the corresponding dataset input. 

Based on nbgraders setup the sources of all assignments are located in a folder called `source`. 

We create an additional folder called `eval_files`, in which all **python modules** are stored. 