using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PROBLEM_01

	/*
	 * Write a program that prints 
	 * the following numbers on the 
	 * console 1, 101, 1001, each on 
	 * a new line, up to total of 10 numbers.
	 */

{
	class Program
	{
		static void Main(string[] args)
		{
			int numero = 1;
			int numeroExponente = 10;
			int contador;

			Console.WriteLine($"The first number is {numero}");

			for (contador = 2; contador < 12; contador++)
			{
				Console.WriteLine($"The next number is: {numero + Math.Pow(numeroExponente,contador)}");
				
			}

			Console.ReadLine();
		}
	}
}
