import numpy as np 
import matplotlib as plt

def simulateQueue(T_final, lambda_arrival, mu_service, C, runs=1):
    time_step = 0.01
    N = T_final/time_step + 1 
    Q = np.zeros(N)
    for i in range(0,runs):
        for j in range(0,N):
            Q[j] = Q[j-1] + (lambda_arrival - mu_service * (min(Q[j-1],C))) * time_step + 1 * np.sqrt(time_step) * np.random.normal(loc = 0, scale = 1)