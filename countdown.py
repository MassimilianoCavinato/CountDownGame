"""
Python 3.5

https://www.youtube.com/watch?v=pfa3MHLLSWI

run from shell: python countdown.py n1 n2 n3 n4 n5 n6 n7

with n7 as target number

"""

import sys

class CountDownGame: 
    
    inputs = None
    rand = None
    operators = ["+","-","*","/"]
    
    result = None
    absolute_difference = None
    expression = None
    
    best_result = None   
    best_absolute_difference = None     
    best_expression = None
    
    exact_found = False
    brute_force_iteration = 0
    
    #INIT####################################
    def __init__(self, arguments):        
        self.validate_arguments(arguments)
        self.bruteforce()        
       
    #VALIDATE ARGUMENTS#######################  
    def validate_arguments(self, arguments):      
        #check if list
        if type(arguments).__name__ !=  'list':
            print(type(arguments).__name__)
            sys.exit('The arguments are not being passed in a list')
            
        #check if 7 arguments
        if len(arguments) != 7:
            sys.exit("The requires 7 arguments in total")
            
        #check if all type int, catch error
        try:
            arguments = [int(arg) for arg in arguments]
        except ValueError:
            sys.exit("It seems that one ore more of the arguments can't be interpreted  as integer")       
                
        #check all arguments are > 0    
        for arg in arguments:
           if arg <= 0:
               sys.exit("One ore more of the arguments is a number <= 0")
        
        #Setting class values for inputs and random number by using slice operations on list argument
        self.rand = arguments[-1]
        self.inputs = arguments[:-1]
    
    #BRUTE FORCE################################
    def bruteforce(self):  
       
        import itertools
        import pprint
        inputs_length = len(self.inputs)
        
        for i in range(inputs_length):
            
            self.brute_force_iteration += 1
            input_permutations = list(itertools.permutations(self.inputs, i+1))
            operator_product = list(itertools.product(self.operators, repeat = i))
             
            for permutation_set in input_permutations: 
                self.brute_force_iteration += 1
                for operator_set in operator_product:
                    
                    """
                    Here is the tricky part, the number of operators are always
                    1 less than the numbers variable in the equation
                    so I will just set the expression to start with the first number
                    and i will keep adding each time 1 operator and 1 number
                    
                    """
                    expression = [permutation_set[0]]
                    expression_result = permutation_set[0]
                    
                    """
                    This valid_expression variable is set in case the specs of the program include also 0 and negative numbers,
                    It shouldn't really do anything since I am excluding that case in the argument validation
                    """
                    valid_expression =  True
                   
                    for operator_index, operator in enumerate(operator_set):                                               
                        
                        self.brute_force_iteration += 1
                        if valid_expression == True:
                            
                            expression.append(operator)
                            expression.append(permutation_set[operator_index+1])
                            
                            if(operator == '+'):
                                expression_result += permutation_set[operator_index+1]
                            elif(operator == '-'):
                                expression_result -= permutation_set[operator_index+1]
                            elif(operator == '*'):
                                expression_result *= permutation_set[operator_index+1]
                            elif(operator == '/'):
                                """
                                I ecluded zeroes from the inputs 
                                but in case I want to change the validation of the arguments
                                this will still work making this simple check when trying to divide by 0
                                """
                                if(permutation_set[operator_index+1] == 0):
                                    valid_expression =  False
                                    break
                                else:
                                    expression_result /= permutation_set[operator_index+1]
                            else:
                                valid_expression =  False
                             
                        
                    if valid_expression == True:
                        self.update_results(expression_result, expression)
                        
                    if self.exact_found == True:                        
                        return;
    
    #update current expression result and best result ############################    
    def update_results(self, result, expression):
               
        self.result = result
        self.absolute_difference =  abs(result - self.rand)   
        self.expression = expression
        
        if self.best_result is None :
            self.best_result = result
            self.best_absolute_difference = abs(result - self.rand)
            self.best_expression = expression
            
        elif self.absolute_difference < self.best_absolute_difference:
            self.best_absolute_difference = abs(result - self.rand)
            self.best_result = result
            self.best_expression = expression
         
          
        self.check_exact()     
    
    #CHECK EXACT###############################
    def check_exact(self):
        
        if self.result == self.rand and self.absolute_difference == 0:
            self.exact_found = True
            return self.exact_found
      
    
    #FINAL CHECK################################
    def debug(self):
        
        print("**************************")
        print("DEBUG")
        print('inputs', self.inputs)
        print('rand',self.rand)
        print('operators', self.operators)
        print('BESTS')
        print('best_result', self.best_result)
        print('best_absolute_difference', self.best_absolute_difference)
        print('best_expression', self.best_expression)
        print("---------------------------")
        print('Brute force iteration ', self.brute_force_iteration)
        print('exact_found', self.exact_found)
        print("**************************")
    
                        
    def print_best_solution(self):    
        solution = ''
        for i in self.best_expression:
            i = str(i)+' '
            solution += i
        solution += '= '+str(self.best_result)
        print(solution)
    


#exclude script name from argv
arguments = sys.argv[1:]
CountDownGame(arguments).print_best_solution()

#Uncomment debug() below if required
#test.debug()
