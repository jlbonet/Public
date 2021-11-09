using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Third_Digit

/*
 * Write an expression that checks whether the third bit in a given integer is 1 or 0.
 */
{
	class Program
	{
		static void Main(string[] args)
		{
			Random aleatorio = new Random();

			for (int contador = 0; contador < 50; contador++)
			{
				byte numero = (byte)aleatorio.Next(256);
				string cadena = numero.ToString();
				char caracter;
				caracter = cadena[1];
				/*if (caracter == '1')
				{
					Console.WriteLine($"This number {numero} contains a 1 in third psotion from rigth");
				}

				else
				{
					Console.WriteLine($"This number {numero} contains a 0 in third psotion from rigth");
				}
			}
			Console.ReadLine();
		}
	}
}
