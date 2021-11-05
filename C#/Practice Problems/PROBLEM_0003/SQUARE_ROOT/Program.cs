using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SQUARE_ROOT
/*
 * Write a program that prints the square root of 12345.
 */


{
	class Program
	{
		static void Main(string[] args)
		{
			float squareRoot = 12345f;

			Console.WriteLine($"The square root of 12345 is: {Math.Sqrt(squareRoot)}");
			Console.ReadLine();
		}
	}
}
