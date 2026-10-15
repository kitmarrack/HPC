import numpy as np 
import matplotlib as plt
import time

def simulateQueue(T_final, lambda_arrival, mu_service, C, runs=1):
    time_step = 0.01
    N = T_final/time_step + 1
    N = int(N)
    R = runs
    Q = np.zeros((R,N))
    Q[0] = 0

    start = time.time()
    for r in range(0,R):
        for t in range(0,N-1):
            Q[r,t+1] = Q[r,t] + (lambda_arrival - mu_service * (min(Q[r,t],C))) * time_step + 1 * np.sqrt(time_step) * np.random.normal(loc = 0, scale = 1)
            if Q[r,t+1] < 0:
                Q[r,t+1] = 0

    MQL = round(np.mean(np.mean(Q, axis = 0)),2)
    SDQL = round(np.mean(np.std(Q, axis = 0)),2)
    MO = round(np.mean(np.mean(Q/C,axis = 0))*100,2)

    end = time.time()
    run_time = round(end - start,4)
    print(f'''
    Queue statistics over {R} runs
    ---------------------------------
    Mean queue length:  {MQL}
    Stdev queue length: {SDQL}
    Mean occupancy:     {MO}%
    Total run time:     {run_time} seconds

    ''')


simulateQueue(160, 4., 0.4, 16, 100)