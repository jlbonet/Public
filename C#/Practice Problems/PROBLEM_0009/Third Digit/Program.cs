using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Third_Digit

/*
 * Write an expression that looks for a given integer if its third digit (right to left) is 7.
 */
{
	class Program
	{
		static void Main(string[] args)
		{
			Random aleatorio = new Random();

			for (int contador = 0; contador < 50; contador++)
			{
				ulong numero = (ulong)aleatorio.Next(1000000,1500000);
				string cadena = numero.ToString();
				char caracter;
				caracter = cadena[4];
				if (caracter == '7')
				{
					Console.WriteLine($"This number {numero} contains a 7 in third psotion" );
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
