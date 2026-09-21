data=read.table('./poidsnaissance.txt',header = T,sep=',')
sexe=data$SEXE+1
poids=data$POIDNAIS
agegest=data$AGEGEST
tailmere=data$TAILMERE
cigjour=data$CIGJOUR
data <- list(
  poids=poids, sexe=sexe, agegest=agegest, tailmere=tailmere, cigjour=cigjour, N=length(poids)
)

inits <- list(list(moyennes=c(2600,4000), sigma=500),
              list(moyennes=c(4500,2700), sigma=700),
              list(moyennes=c(4000,4000), sigma=300))




m1 <- jags.model('./modelepoidsnaissance.txt', data=data,
                 inits=inits, n.chains=3)

update(m1, 3000)

mcmc1 <- coda.samples(m1, variable.names=c("moyennes","sigma"),
                      n.iter=2000)

dic.samples(m1,n.iter=1000)




m2 <- jags.model('./modelepoidsnaissance2.txt', data=data,
                 inits=inits, n.chains=3)

update(m2, 3000)

mcmc2 <- coda.samples(m2, variable.names=c("moyennes","sigma"),
                      n.iter=2000)

dic.samples(m2,n.iter=1000)

# mean(mcmc1[[1]][, "moyennes[1]"])
#
# plot(mcmc1)
# gelman.diag(mcmc1)
# gelman.plot(mcmc1)
# autocorr.plot(mcmc1)
# summary(mcmc1)