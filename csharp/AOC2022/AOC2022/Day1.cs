namespace AOC2022
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public static class Day1
    {

        public static void Part1()
        {
            var largest = 0;
            var current = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                if(string.IsNullOrWhiteSpace(line))
                {
                    if (current > largest) largest = current;
                    current = 0;
                }
                else
                {
                    var newMeasurement = Convert.ToInt32(line);

                    current += newMeasurement;
                }
            }

            Console.WriteLine("Part 1: " + largest);
        }

        public static void Part2()
        {
            var largest = new List<int>() { 0, 0, 0 };
            var current = 0;

            foreach (string line in System.IO.File.ReadLines(@"AppData\fulldata.txt"))
            {
                if (string.IsNullOrWhiteSpace(line))
                {
                    if (current > largest[0]) largest[0] = current;
                    else if (current > largest[1]) largest[1] = current;
                    else if (current > largest[2]) largest[2] = current;
                    current = 0;

                    largest = largest.OrderBy(x => x).ToList();
                }
                else
                {
                    var newMeasurement = Convert.ToInt32(line);

                    current += newMeasurement;
                }
            }

            Console.WriteLine("Part 2: " + largest.Sum());
        }


    }
}
