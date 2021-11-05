using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DATE_TIME

/*
 * Write a program that prints on the console the current date and time
 */


{
	class Program
	{
		static void Main(string[] args)
		{
			var fechaHora = DateTime.Now;
			
			Console.WriteLine($"The current date is: {fechaHora.ToShortDateString()}");
			Console.WriteLine($"The current time is: {fechaHora.ToShortTimeString()}");
			Console.ReadLine();
		}
	}
}
