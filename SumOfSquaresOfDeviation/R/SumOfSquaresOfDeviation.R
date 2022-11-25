#' Provides function to find sum of squares of deviation from mean
#' @param vector1 A distribution vector.
#' @return z A sum of squares of deviation - scalar.
#' @examples
#'
#' SSD(c(1,2,3,4,5))
#'
#'
#Function to find sum of squares of deviation from mean

SSD <- function(vector1){
  su=sum(vector1**2)
  me=mean(vector1)
  n=length(vector1)
  z= su-(n*(me^2))
  return(z)
}

#Example
#function- SSD(c(1,2,3,4,5))
#Answer -  10

roxygenise()
getwd()
