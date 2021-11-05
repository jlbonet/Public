using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEQUENCE_NUMBERS

/*
 * Write a program that prints the first 100 members of the sequence 2, -3, 4, -5, 6, -7, 8.
 */

{
	class Program
	{
		static void Main(string[] args)
		{
			int contador;

			for (contador = 2; contador < 102; contador++)
			{
				Console.WriteLine(Math.Abs(contador));
				contador++;
				Console.WriteLine((Math.Abs(contador) * (-1)));
			}

			Console.ReadLine();
		}
	}
}
