using System;
using System.Text;

namespace Test {
    class Program {
        static void Main(string[] args) {

            int number = 500;

            if (number >= 10 && boolOutput(number)) {
                Console.WriteLine("Awesome");
            } else {
                Console.WriteLine("Not Awesome");
            }

            Console.WriteLine("Hello world" + number);

            int a = 43;

            switch (a) {
                default:
                    Console.WriteLine("Default Value");
                    break;
                case 1:
                    Console.WriteLine("Case 1");
                    break;
                case 5:
                    Console.WriteLine("Case 5");
                    break;
            }

            int[] intArray = new int[5];
            int[] intArray2 = new int[] { 1, 2, 3, 4, 5 };

            list<int> intList = new list<int>() {};
        }

        static void noOutput() {
        }

        static bool boolOutput(int i) {
            return i > 100;
        }
    }
}
