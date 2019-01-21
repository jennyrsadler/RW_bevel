Sys.setenv(USE_CXX14 = 1)
library("rstan")
rstan_options(auto_write = TRUE)
options(mc.cores = parallel::detectCores())

library(hBayesDM)

#run Probabilistic Selection Task -- Q-learning with two learning rates from M. J. Frank et al. (2007)

output <-- pst_gainloss_Q(data = '/Users/jennygilbert/Documents/RW_bevel/all_clean.txt',niter = 2000,nwarmup = 1000,nchain = 1,ncore = 1,nthin = 1,inits = "random",indPars = "mean",saveDir = NULL,modelRegressor = FALSE,vb = FALSE,inc_postpred = FALSE,adapt_delta = 0.95, stepsize = 1,max_treedepth = 10)



###EXAMPLE
## Not run: 
# Run the model and store results in "output"
#output <- pst_gainloss_Q(data = "example", niter = 2000, nwarmup = 1000, nchain = 4, ncore = 4)

# Visually check convergence of the sampling chains (should like like 'hairy caterpillars')
#plot(output, type = 'trace')

# Check Rhat values (all Rhat values should be less than or equal to 1.1)
#rhat(output)

# Plot the posterior distributions of the hyper-parameters (distributions should be unimodal)
#plot(output)

# Show the WAIC and LOOIC model fit estimates
#printFit(output)

## End(Not run)