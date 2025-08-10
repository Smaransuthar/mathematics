#include <stdio.h>

double modulus(double dividend, double divisor)
{
        int quotient = (int)(dividend / divisor);
        return dividend - quotient * divisor;
}

double square_root(double n)
{
	double i;
	
	for(i = 0.001; i*i < n; i = i + 0.001);

	return i;
}

int round_off(double n)
{
	if((n + 0.5) >= ((int)(n)))
	{
		return (n = (int)(n));
	}
	
	else
	{
		return n = (int)(n);
	}
}

int factorial(int n)
{
	
	int counter = 1;
	int factorial = 1;

	if(n == 0)
	{
		return 1;
	}
	
	else
	{
		while(counter <= n)
		{
			factorial = factorial * counter;		
			counter++;
		}
	}
	
	return factorial;
}

double periodicity(double angle)
{
        if((modulus(angle, 180.0)) > 90)
        {
                return(180.0 - (modulus(angle, 180.0)));
        }

        else
        {
                return(modulus(angle, 180.0));
        }
}


double power(double base, int exponent)
{
	if(exponent == 0)
	{	
		return 1;
	}
	
	else
	{
		return(power(base, exponent - 1) * base);
	}
}

double degree(double angle)
{
        float radian;
        radian = ((3.1415926538979323846)/180) * angle;
        return radian;
}

float sine(double x)
{ 	
	int upper_limit = 11;
	int lower_limit = 0;
	double taylor_series = 0;	

	while(lower_limit <= upper_limit)
	{
		taylor_series = taylor_series + ((power(-1, lower_limit)) / factorial(((2 * (lower_limit)) + 1))) * (power(degree(periodicity(x)), (2*(lower_limit) + 1)));
		lower_limit++;
	}
	return taylor_series;
} 		

float cosine(double x)
{
        int upper_limit = 11;
        int lower_limit = 0;
        double taylor_series = 0;

        while(lower_limit <= upper_limit)
        {
                taylor_series = taylor_series + ((power(-1, lower_limit)) / factorial(((2 * (lower_limit)))) * (power(degree(periodicity(x)), (2*(lower_limit)))));
                lower_limit++;
        }
        return taylor_series;
}

float tangent(double x)
{
        return sine(x)/cosine(x);
}

float cotangent(double x)
{
	return 1/tangent(x);
}

float secant(double x)
{
	return 1/cosine(x);
}

float cosecant(double x)
{
	return 1/sine(x);
}

float logarithm(double x)
{
	double upper_limit = 1000;
	double lower_limit = 1;
	double taylor_series = 0;	

	x = x - 1;

	while(lower_limit <= upper_limit)
	{
		taylor_series = taylor_series + ((power(-1, (lower_limit + 1))) * (power(x, lower_limit) / (lower_limit)));
		lower_limit++;
	}
	return taylor_series;
}

int flr(double x)
{
	return (int)(x);
}

int ceiling(double x)
{
	return ((int)(x)) + 1;
}

int main()
{
	return 0;
}
