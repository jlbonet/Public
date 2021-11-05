using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Hexadecimal_256

/*
 * Initialize a variable of type int with a value of 256 in hexadecimal format (256 is 100 in a numeral system with base 16).
 */

{
	class Program
	{
		static void Main(string[] args)
		{
			int number256 = 256;
			
			string hexa = number256.ToString("x");
			
			Console.WriteLine(hexa);
			Console.ReadLine();

		}
	}
}
