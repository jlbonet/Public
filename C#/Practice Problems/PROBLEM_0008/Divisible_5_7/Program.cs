using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Divisible_5_7

/*
 * Write a Boolean expression that checks whether a given integer is divisible by both 5 and 7, without a remainder.
 */
{
	class Program
	{
		static void Main(string[] args)
		{
			Random aleatorio = new Random();

			for (int contador = 0; contador < 15; contador++)
			{
				ulong numero = ((ulong)aleatorio.Next(1500000));

				if (numero % 5 == 0 && numero % 5 == 0)
				{
					Console.WriteLine($"The number {numero} is divisible with 5 and 7");
				}
				else Console.WriteLine($"The number {numero} no its divisible with 5 and 7");
			}
			Console.ReadLine();
		}
	}

}

