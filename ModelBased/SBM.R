library(MBCbook)
data(PoliticalBlogs)
xPoliticalBlogs <- as.matrix(PoliticalBlogs)

library(blockmodels)
my_model<-BM_bernoulli("SBM", xPoliticalBlogs, plotting="")
my_model$estimate()


plot(1:length(my_model$ICL),my_model$ICL,ylab="ICL",xlab='G')
G=which.max(my_model$ICL)
z <- my_model$memberships[[G]]

library(network)
plot.network(PoliticalBlogs, mode="fruchtermanreingold",
             vertex.col=max.col(z$Z))


partis=NULL
for (i in 1:196){
  partis=c(partis,PoliticalBlogs$val[[i]]$group)
}
classes=apply(z$Z,1,which.max)
table(classes,partis)


my_model$model_parameters[[10]]