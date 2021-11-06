using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Substract_With_Out_Substratc

/*
* Subtract two numbers without using the subtract property.
*/

{
	class Program
	{
		static void Main(string[] args)
		{
			int numero1 = 5;
			int numero2 = 1;

			Console.WriteLine($"The substract without substract is: {numero1} + {numero2} = {Math.Abs(numero1) + (Math.Abs(numero2) * (-1))}") ;
			Console.ReadLine();
		}
	}
}
