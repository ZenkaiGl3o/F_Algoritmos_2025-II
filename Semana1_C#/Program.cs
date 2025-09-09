using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Semana1_C_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer2();
            Console.ReadKey();
        }
        static void ejer1()  //Metodos: pedacitos de codigo que pueden llamarse a la rama principal
        {
            String nombre, carrera; //Declarando variables

            Console.Write("Ingrese su nombre completo: ");
            nombre = Console.ReadLine(); //readline para asignar lo escrito a la variable   
            Console.Write("Ingrese la carrera que estudia: ");
            carrera = Console.ReadLine();

            Console.WriteLine($"\nHola {nombre}, bienvenido a Fundamentos de Algoritmos de {carrera}"); 
            //El "$" es una concatenacion por interpolacion al inicio del texto para poner varias mierditas en vez del "+"
            // para bajar de linea usar altGR + ? y n: \n
        }
        static void ejer2()
        {
            Console.WriteLine("\"Leonardo\"");  //Como colocar comillas en un writeline(si quieres más comillas solo aumentas las barras :)
        }

        static void ejer3()
        {
            Console.Write("Ingrese el 1er numero: ");
            int x = int.Parse(Console.ReadLine()); //Otro metodo para convertir a numero el texto :)
            Console.Write("Ingrese el 2do numero: ");
            int y = Convert.ToInt32(Console.ReadLine());

            double resu = x / y;

            Console.WriteLine("Suma: " + (x + y));
            Console.WriteLine("Resta: " + (x - y));
            Console.WriteLine("Multiplicacion: " + (x * y));
            Console.WriteLine("Division: " + resu);
        }
        static void ejer4()
        {

        }
        static void ejer5()
        {

        }
        static void ejer6()
        {

        }
    }
}
