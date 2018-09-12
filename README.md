# Machine_Learns

Using Normal Equation to find theta values of a linear model to find pattern between BODY WEIGHT and Brain WEIGHT of Mammals.

X: Feature matrix

X = ([[1, a, b, ., .],
	  [1, ., ., ., .],
	  [1, ., ., ., .],
	         .
			 .
			 .
	  [1, ., ., ., .]])

Y: Label/Output matrix

Y = ([[1],
	  [2],
	  [3],
	  [4],
	   .
	   .
	   .
	  [n]])

@: theta

T: Transpose

Normal Equation:

@ = ((X^T )*X)^-1 )*((X^T )*Y)

Hypothesis: h(@) = @0 + @1*x1


CONCLUSION:
The values of theta generated provides a reasonable prediction using the hypothesis.