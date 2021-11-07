using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace odd_even

/*
 * Write an expression that checks whether an integer is odd or even.
 */
{
	class Program
	{
		static void Main(string[] args)
		{
			Random aleatorio = new Random();
			
			for (int contador = 0; contador <= 50; contador++)
			{
				ulong numero = ((ulong)aleatorio.Next(1500000));
				if (numero % 2 == 0)
				{
					Console.WriteLine($"The number {numero} is odd");
				}

				else Console.WriteLine($"The number {numero} is even");
			}

			Console.ReadLine();
		}
	}
}
