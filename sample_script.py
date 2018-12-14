#!/usr/local/lib/python3.7

#import the optimizer framework
from evolution_env import EvolutionEnv


#create a new optimizer environment and initialize data structure
optimizer1 = EvolutionEnv(session_file ='mario-SCORE-chromosome.p')

#run the optimizer for the desired number of times
#optimizer1.run_generations(1, 'fitness--gen.csv')
#serialize the data structure to a file. Pickle for effeciency 
#optimizer1.save_optimizer('mario-1-chromosome.p')

#optimizer2 = EvolutionEnv(max_steps = 3000, num_chromosomes = 40, fitness_strategy="score")
#optimizer2.run_generations(100, 'fitness-values_SCORE.csv')
#optimizer2.save_optimizer('mario-SCORE-chromosome.p')

#optimizer3 = EvolutionEnv(max_steps = 3000, num_chromosomes = 40, fitness_strategy="time")
#optimizer3.run_generations(100, 'fitness-values_TIME.csv')
#optimizer3.save_optimizer('mario-TIME-chromosome.p')

#optimizer4 = EvolutionEnv(max_steps = 3000, num_chromosomes = 40, fitness_strategy="coins")
#optimizer4.run_generations(100, 'fitness-values_COINScsv')
#optimizer4.save_optimizer('mario-COINS-chromosome.p')

#see how the top performing chromosome looks in the simulator 
optimizer1.run_top_chromosome(render=True)


#To load a previous environment, either create a new optimizer with the filename,
#or call the load optimizer function directly. Note this will overwrite the current state

#load the previous session and keep training
#optimizer2 = EvolutionEnv(session_file ="mario-4-chromosome.p")
# optimizer2.run_generations(1, 'fitness-values2.csv')
# optimizer2.save_optimizer('mario-4-chromosome2.p') #save to an updated file 
#optimizer2.run_top_chromosome(render=True)
