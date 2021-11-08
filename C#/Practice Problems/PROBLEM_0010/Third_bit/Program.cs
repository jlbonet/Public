using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Third_Digit

/*
 *Write an expression that checks whether the third bit in a given integer is 1 or 0
 */
{
	class Program
	{
		static void Main(string[] args)
		{
			Random aleatorio = new Random();

			for (int contador = 0; contador < 50; contador++)
			{
				ulong numero = (ulong)aleatorio.Next(1500000);
				numero[]
				//string cadena = numero.ToString();
				//byte numeroBit = ((byte)numero);
				
				//numeroBit.
				//char caracter;
				//caracter = cadena[2];
				if (caracter == '7')
				{
					Console.WriteLine($"This number {numero} contains a 7 in third psotion");
				}

				else
				{
					Console.WriteLine($"This number {numero} NOT is valid");
				}
			}
			Console.ReadLine();
		}
	}
}
